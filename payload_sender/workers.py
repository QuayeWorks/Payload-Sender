"""Qt workers communicate only through queued signals."""

from pathlib import Path
from threading import Event

from PySide6.QtCore import QThread, Signal

from .core import Endpoint, PayloadInfo, TransferError, inspect_payload, transfer_payload


class PayloadWorker(QThread):
    progress = Signal(object)
    inspected = Signal(object)
    transferred = Signal(object)
    failed = Signal(object)

    def __init__(self, path: Path, endpoint: Endpoint | None = None,
                 expected: PayloadInfo | None = None, parent=None):
        super().__init__(parent)
        self.path = path
        self.endpoint = endpoint
        self.expected = expected
        self.cancel_event = Event()

    def cancel(self) -> None:
        self.cancel_event.set()

    def run(self) -> None:
        try:
            if self.endpoint is None:
                self.inspected.emit(inspect_payload(self.path, self.cancel_event, self.progress.emit))
            else:
                self.transferred.emit(transfer_payload(self.path, self.endpoint, self.cancel_event,
                                                       self.progress.emit, self.expected))
        except TransferError as exc:
            self.failed.emit(exc)
        except Exception as exc:
            self.failed.emit(TransferError(f"Unexpected error: {exc}"))
