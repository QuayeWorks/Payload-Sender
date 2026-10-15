from __future__ import annotations

import hashlib
import json
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from threading import Event
from unittest.mock import patch

from payload_sender import core
from payload_sender.core import Endpoint, OperationCancelled, TransferError, inspect_payload, transfer_payload
from tests.support import Receiver


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.path = Path(self.temporary.name) / "payload.bin"
        self.data = bytes(range(256)) * 4097
        self.path.write_bytes(self.data)

    def tearDown(self):
        self.temporary.cleanup()

    def test_delivers_exact_binary_bytes_and_eof_without_headers(self):
        events = []
        with Receiver() as receiver:
            result = transfer_payload(self.path, Endpoint(receiver.host, receiver.port), update=events.append)
            self.assertTrue(receiver.done.wait(3))
            self.assertIsNone(receiver.error)
            self.assertEqual(bytes(receiver.data), self.data)
            self.assertEqual(result.bytes_sent, len(self.data))
            self.assertEqual(result.payload.sha256, hashlib.sha256(self.data).hexdigest())
            self.assertGreater(result.elapsed, 0)
            self.assertEqual(events[-1].phase, "complete")

    def test_handles_partial_socket_writes(self):
        original_connect = core._connect

        class LimitedSocket:
            def __init__(self, sock):
                self.sock = sock

            def __getattr__(self, name):
                return getattr(self.sock, name)

            def __enter__(self):
                return self

            def __exit__(self, *_):
                self.sock.close()

            def send(self, data):
                return self.sock.send(data[:997])

        with Receiver() as receiver, patch.object(core, "_connect", side_effect=lambda *a: LimitedSocket(original_connect(*a))):
            transfer_payload(self.path, Endpoint(receiver.host, receiver.port))
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)

    def test_snapshot_still_sends_verified_content_when_source_is_edited(self):
        info = inspect_payload(self.path)

        def change_source(event):
            if event.phase == "connecting":
                self.path.write_bytes(b"Edited after preparation")

        with Receiver() as receiver:
            result = transfer_payload(self.path, Endpoint(receiver.host, receiver.port),
                                      update=change_source, expected=info)
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)
            self.assertEqual(result.payload.sha256, info.sha256)

    def test_changed_selected_payload_is_rejected_before_connecting(self):
        info = inspect_payload(self.path)
        self.path.write_bytes(b"changed")
        with patch.object(core, "_connect") as connect:
            with self.assertRaisesRegex(TransferError, "changed"):
                transfer_payload(self.path, Endpoint("127.0.0.1", 9090), expected=info)
            connect.assert_not_called()

    def test_empty_missing_and_wrong_extension_never_connect(self):
        empty = self.path.with_name("empty.bin")
        empty.write_bytes(b"")
        text = self.path.with_suffix(".txt")
        text.write_bytes(b"data")
        missing = self.path.with_name("missing.bin")
        for path in (empty, text, missing):
            with self.subTest(path=path), patch.object(core, "_connect") as connect:
                with self.assertRaises(TransferError):
                    transfer_payload(path, Endpoint("127.0.0.1"))
                connect.assert_not_called()

    def test_elf_and_uppercase_bin_are_accepted(self):
        for suffix in (".elf", ".BIN"):
            path = self.path.with_suffix(suffix)
            path.write_bytes(b"\x00\x01\x02")
            self.assertEqual(inspect_payload(path).size, 3)

    def test_invalid_endpoints_fail_before_connecting(self):
        for endpoint in (Endpoint("not-an-ip"), Endpoint(""), Endpoint("127.0.0.1", 0),
                         Endpoint("127.0.0.1", 65536), Endpoint("127.0.0.1", True),
                         Endpoint("127.0.0.1", timeout=0), Endpoint("127.0.0.1", timeout=float("nan"))):
            with self.subTest(endpoint=endpoint), patch.object(core, "_connect") as connect:
                with self.assertRaises(TransferError):
                    transfer_payload(self.path, endpoint)
                connect.assert_not_called()

    def test_pre_cancellation_never_connects(self):
        cancel = Event()
        cancel.set()
        with patch.object(core, "_connect") as connect:
            with self.assertRaises(OperationCancelled) as caught:
                transfer_payload(self.path, Endpoint("127.0.0.1"), cancel)
            self.assertEqual(caught.exception.bytes_sent, 0)
            connect.assert_not_called()

    def test_cancel_during_send_reports_exact_submitted_bytes(self):
        cancel = Event()

        def progress(event):
            if event.phase == "sending" and event.completed > 0:
                cancel.set()

        with Receiver() as receiver:
            with self.assertRaises(OperationCancelled) as caught:
                transfer_payload(self.path, Endpoint(receiver.host, receiver.port), cancel, progress)
            self.assertTrue(receiver.done.wait(3))
            self.assertGreater(caught.exception.bytes_sent, 0)
            self.assertLess(caught.exception.bytes_sent, len(self.data))
            self.assertEqual(len(receiver.data), caught.exception.bytes_sent)

    def test_stalled_receiver_times_out_and_records_partial_transfer(self):
        self.path.write_bytes(b"x" * (16 * 1024 * 1024))
        with Receiver(stall=True) as receiver:
            started = time.monotonic()
            with self.assertRaises(TransferError) as caught:
                transfer_payload(self.path, Endpoint(receiver.host, receiver.port, 0.5))
            self.assertEqual(caught.exception.phase, "sending")
            self.assertGreater(caught.exception.bytes_sent, 0)
            self.assertLess(caught.exception.bytes_sent, self.path.stat().st_size)
            self.assertLess(time.monotonic() - started, 3)
            self.assertIn("stalled", str(caught.exception))

    def test_connection_refusal_has_actionable_error(self):
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            port = listener.getsockname()[1]
            with self.assertRaisesRegex(TransferError, "Enable the BIN loader") as caught:
                transfer_payload(self.path, Endpoint("127.0.0.1", port, 0.5))
            self.assertEqual(caught.exception.phase, "connecting")
            self.assertEqual(caught.exception.bytes_sent, 0)

    def test_cancellation_during_pending_connection_closes_socket(self):
        cancel = Event()
        from unittest.mock import Mock
        pending = Mock()
        pending.connect_ex.return_value = core.errno.EINPROGRESS

        def pending_select(*_):
            cancel.set()
            return [], [], []

        with patch.object(core.socket, "socket", return_value=pending), patch.object(core.select, "select", side_effect=pending_select):
            with self.assertRaises(OperationCancelled) as caught:
                core._connect(Endpoint("127.0.0.1", 9090, 0.5), cancel)
        self.assertEqual(caught.exception.phase, "connecting")
        pending.close.assert_called_once()

    def test_pending_connection_timeout_closes_socket(self):
        from unittest.mock import Mock
        pending = Mock()
        pending.connect_ex.return_value = core.errno.EINPROGRESS
        with patch.object(core.socket, "socket", return_value=pending), patch.object(core.time, "monotonic", side_effect=[0, 1]):
            with self.assertRaises(TimeoutError):
                core._connect(Endpoint("127.0.0.1", 9090, 0.5), Event())
        pending.close.assert_called_once()

    def test_ipv6_loopback_when_supported(self):
        try:
            receiver = Receiver(ipv6=True)
        except OSError:
            self.skipTest("IPv6 loopback is unavailable")
        with receiver:
            transfer_payload(self.path, Endpoint(receiver.host, receiver.port))
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)

    def test_large_snapshot_spills_to_disk_and_remains_exact(self):
        original_limit = core.SPOOL_MEMORY_LIMIT
        with Receiver() as receiver, patch.object(core, "SPOOL_MEMORY_LIMIT", 64):
            transfer_payload(self.path, Endpoint(receiver.host, receiver.port))
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)
        self.assertEqual(core.SPOOL_MEMORY_LIMIT, original_limit)

    def test_cli_json_success(self):
        with Receiver() as receiver:
            result = subprocess.run([sys.executable, "-m", "payload_sender", "--cli", "--json",
                                     "--host", receiver.host, "--port", str(receiver.port), str(self.path)],
                                    capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 0, result.stderr)
            output = json.loads(result.stdout)
            self.assertEqual(output["status"], "sent")
            self.assertFalse(output["execution_confirmed"])
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)

    def test_cli_json_failure_has_nonzero_exit_and_no_bytes(self):
        result = subprocess.run([sys.executable, "-m", "payload_sender", "--cli", "--json",
                                 "--host", "invalid", str(self.path)], capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["bytes_sent"], 0)


if __name__ == "__main__":
    unittest.main()
