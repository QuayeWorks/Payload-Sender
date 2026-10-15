"""Cancellable raw-TCP transfer. This module has no GUI dependencies."""

from __future__ import annotations

import errno
import hashlib
import ipaddress
import os
import select
import socket
import stat
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from threading import Event
from typing import BinaryIO, Callable

CHUNK_SIZE = 64 * 1024
SPOOL_MEMORY_LIMIT = 8 * 1024 * 1024
SUPPORTED_SUFFIXES = {".bin", ".elf"}


class TransferError(Exception):
    def __init__(self, message: str, phase: str = "preparing", bytes_sent: int = 0):
        super().__init__(message)
        self.phase = phase
        self.bytes_sent = bytes_sent


class OperationCancelled(TransferError):
    pass


@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int = 9090
    timeout: float = 10.0

    def validate(self) -> "Endpoint":
        try:
            address = ipaddress.ip_address(self.host.strip())
        except ValueError as exc:
            raise TransferError("Enter the console's IPv4 or IPv6 address, such as 192.168.1.100.") from exc
        if isinstance(self.port, bool) or not isinstance(self.port, int) or not 1 <= self.port <= 65535:
            raise TransferError("The port must be a number between 1 and 65535.")
        if not 0.5 <= self.timeout <= 120:
            raise TransferError("The timeout must be between 0.5 and 120 seconds.")
        return Endpoint(str(address), self.port, float(self.timeout))

    @property
    def display(self) -> str:
        host = f"[{self.host}]" if ":" in self.host else self.host
        return f"{host}:{self.port}"


@dataclass(frozen=True)
class PayloadInfo:
    path: Path
    size: int
    sha256: str
    modified_ns: int


@dataclass(frozen=True)
class TransferUpdate:
    phase: str
    completed: int
    total: int
    elapsed: float = 0.0


@dataclass(frozen=True)
class TransferResult:
    payload: PayloadInfo
    endpoint: Endpoint
    bytes_sent: int
    elapsed: float

    @property
    def speed(self) -> float:
        return self.bytes_sent / max(self.elapsed, 0.000001)


UpdateCallback = Callable[[TransferUpdate], None]


def format_bytes(value: float) -> str:
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if abs(value) < 1024 or unit == "TiB":
            return f"{value:.0f} {unit}" if unit == "B" else f"{value:.2f} {unit}"
        value /= 1024
    return "0 B"


def _check_cancel(cancel: Event, phase: str, sent: int = 0) -> None:
    if cancel.is_set():
        message = "Canceled before any payload bytes were sent."
        if sent:
            message = f"Canceled after {format_bytes(sent)} were submitted to TCP. Check the console before resending."
        raise OperationCancelled(message, phase, sent)


def _read_payload(
    path: Path, cancel: Event, update: UpdateCallback, snapshot: BinaryIO | None = None
) -> PayloadInfo:
    path = path.expanduser().resolve()
    if path.suffix.lower() not in SUPPORTED_SUFFIXES:
        raise TransferError("Choose a .bin or .elf payload supported by your console's loader.")
    if not path.is_file():
        raise TransferError("The selected payload must be an existing regular file.")
    _check_cancel(cancel, "preparing")
    with path.open("rb") as source:
        before = os.fstat(source.fileno())
        if not stat.S_ISREG(before.st_mode):
            raise TransferError("The selected payload must be a regular file.")
        if before.st_size == 0:
            raise TransferError("The selected payload is empty.")
        digest = hashlib.sha256()
        read = 0
        last_update = 0.0
        update(TransferUpdate("preparing", 0, before.st_size))
        while chunk := source.read(CHUNK_SIZE):
            _check_cancel(cancel, "preparing")
            digest.update(chunk)
            if snapshot is not None:
                snapshot.write(chunk)
            read += len(chunk)
            now = time.monotonic()
            if now - last_update >= 0.05:
                update(TransferUpdate("preparing", read, before.st_size))
                last_update = now
        after = os.fstat(source.fileno())
        if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns) or read != before.st_size:
            raise TransferError("The payload changed while it was being read. Select it again.")
    _check_cancel(cancel, "preparing")
    update(TransferUpdate("preparing", read, read))
    return PayloadInfo(path, read, digest.hexdigest(), after.st_mtime_ns)


def inspect_payload(
    path: Path | str, cancel: Event | None = None, update: UpdateCallback | None = None
) -> PayloadInfo:
    try:
        return _read_payload(Path(path), cancel or Event(), update or (lambda event: None))
    except (OSError, ValueError) as exc:
        raise TransferError(f"Cannot read the payload: {exc}") from exc


def _connect(endpoint: Endpoint, cancel: Event) -> socket.socket:
    family = socket.AF_INET6 if ":" in endpoint.host else socket.AF_INET
    sock = socket.socket(family, socket.SOCK_STREAM)
    try:
        sock.setblocking(False)
        # Literal addresses avoid an unbounded DNS lookup and keep cancellation responsive.
        result = sock.connect_ex((endpoint.host, endpoint.port))
        pending = {errno.EINPROGRESS, errno.EWOULDBLOCK, errno.EALREADY, 10035, 10036, 10037}
        if result not in pending | {0, errno.EISCONN}:
            raise OSError(result, os.strerror(result))
        deadline = time.monotonic() + endpoint.timeout
        while result not in (0, errno.EISCONN):
            _check_cancel(cancel, "connecting")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("Connection timed out")
            _, writable, exceptional = select.select([], [sock], [sock], min(0.1, remaining))
            if writable or exceptional:
                result = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
                if result:
                    raise OSError(result, os.strerror(result))
        _check_cancel(cancel, "connecting")
        return sock
    except BaseException:
        sock.close()
        raise


def transfer_payload(
    path: Path | str,
    endpoint: Endpoint,
    cancel: Event | None = None,
    update: UpdateCallback | None = None,
    expected: PayloadInfo | None = None,
) -> TransferResult:
    """Send the exact file bytes and EOF, with no header, retry, or execution claim.

    A bounded-memory snapshot guarantees that the displayed/verified hash describes
    the bytes transmitted, even if the original file is edited during a transfer.
    The timeout applies to connecting and to each period without send progress.
    """
    endpoint = endpoint.validate()
    cancel = cancel or Event()
    update = update or (lambda event: None)
    sent = 0
    phase = "preparing"
    try:
        with tempfile.SpooledTemporaryFile(max_size=SPOOL_MEMORY_LIMIT, mode="w+b") as snapshot:
            info = _read_payload(Path(path), cancel, update, snapshot)
            if expected is not None and (info.path, info.size, info.sha256) != (
                expected.path, expected.size, expected.sha256
            ):
                raise TransferError("The selected file changed. Select it again before sending.")
            snapshot.seek(0)
            phase = "connecting"
            update(TransferUpdate(phase, 0, info.size))
            with _connect(endpoint, cancel) as sock:
                phase = "sending"
                started = last_activity = time.monotonic()
                last_update = 0.0
                update(TransferUpdate(phase, 0, info.size))
                while chunk := snapshot.read(CHUNK_SIZE):
                    view = memoryview(chunk)
                    while view:
                        _check_cancel(cancel, phase, sent)
                        remaining = endpoint.timeout - (time.monotonic() - last_activity)
                        if remaining <= 0:
                            raise TimeoutError("The receiver stopped accepting data")
                        _, writable, exceptional = select.select([], [sock], [sock], min(0.1, remaining))
                        if exceptional:
                            raise ConnectionError("The receiver closed the connection")
                        if not writable:
                            continue
                        try:
                            count = sock.send(view)
                        except (BlockingIOError, InterruptedError):
                            continue
                        if count == 0:
                            raise ConnectionError("The receiver closed the connection")
                        view = view[count:]
                        sent += count
                        last_activity = time.monotonic()
                        if last_activity - last_update >= 0.05:
                            update(TransferUpdate(phase, sent, info.size, last_activity - started))
                            last_update = last_activity
                _check_cancel(cancel, phase, sent)
                # EOF is how raw loaders learn that the payload is complete.
                sock.shutdown(socket.SHUT_WR)
                elapsed = max(time.monotonic() - started, 0.000001)
                update(TransferUpdate("complete", sent, info.size, elapsed))
                return TransferResult(info, endpoint, sent, elapsed)
    except TransferError:
        raise
    except TimeoutError as exc:
        detail = "Check the IP, loader port, and whether the BIN loader is enabled."
        if phase == "sending":
            detail = "The transfer stalled. Check the console before manually resending."
        raise TransferError(f"{exc}. {detail}", phase, sent) from exc
    except ConnectionRefusedError as exc:
        raise TransferError(
            f"{endpoint.display} refused the connection. Enable the BIN loader and check its port.", phase, sent
        ) from exc
    except (OSError, ValueError) as exc:
        message = f"Transfer failed during {phase}: {exc}"
        if sent:
            message += f". {format_bytes(sent)} were submitted to TCP; check the console before resending."
        raise TransferError(message, phase, sent) from exc
