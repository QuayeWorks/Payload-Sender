"""Desktop and command-line entry points. CLI use needs only standard Python."""

from __future__ import annotations

import argparse
import json
import signal
import sys
import time
from pathlib import Path
from threading import Event

from . import __version__
from .core import Endpoint, OperationCancelled, TransferError, format_bytes, transfer_payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="QuayeWorks PS4 Payload Sender")
    parser.add_argument("payload", nargs="?", type=Path, help="A .bin or .elf payload")
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("--cli", action="store_true", help="Send without the desktop interface")
    parser.add_argument("--host", help="Console IPv4 or IPv6 address (required for CLI)")
    parser.add_argument("--port", type=int, default=9090, help="Loader port (default: 9090)")
    parser.add_argument("--timeout", type=float, default=10, help="Connect/stall timeout in seconds")
    parser.add_argument("--json", action="store_true", help="CLI: print a machine-readable result")
    parser.add_argument("--config-dir", type=Path, help="Override the desktop settings directory")
    args = parser.parse_args(argv)
    if args.cli:
        if args.payload is None or not args.host:
            parser.error("--cli requires --host and a payload path")
        cancel = Event()
        previous = signal.signal(signal.SIGINT, lambda *_: cancel.set())
        last = 0.0

        def progress(event):
            nonlocal last
            now = time.monotonic()
            if not args.json and (now - last > 0.1 or event.phase == "complete"):
                print(f"\r{event.phase.title():12} {format_bytes(event.completed)} / "
                      f"{format_bytes(event.total)}          ", end="", file=sys.stderr, flush=True)
                last = now

        try:
            result = transfer_payload(args.payload, Endpoint(args.host, args.port, args.timeout), cancel, progress)
            data = {"status": "sent", "destination": result.endpoint.display, "bytes_sent": result.bytes_sent,
                    "sha256": result.payload.sha256, "seconds": round(result.elapsed, 6),
                    "execution_confirmed": False}
            print(json.dumps(data) if args.json else
                  f"\nSent {format_bytes(result.bytes_sent)} to {result.endpoint.display}. "
                  "Verify payload execution on the console.")
            return 0
        except TransferError as exc:
            data = {"status": "canceled" if isinstance(exc, OperationCancelled) else "error",
                    "message": str(exc), "phase": exc.phase, "bytes_sent": exc.bytes_sent}
            print(json.dumps(data) if args.json else f"\n{exc}",
                  file=sys.stdout if args.json else sys.stderr)
            return 130 if isinstance(exc, OperationCancelled) else 1
        finally:
            signal.signal(signal.SIGINT, previous)
    if args.json:
        parser.error("--json is available only with --cli")
    try:
        from .gui import run_gui
    except ImportError as exc:
        print(f"The desktop interface needs PySide6-Essentials. Run Start_Windows.bat or "
              f"python bootstrap.py to set it up.\nDetails: {exc}", file=sys.stderr)
        return 1
    return run_gui(args.config_dir, args.payload, args.host, args.port, args.timeout)
