"""Native desktop UI; all file inspection and networking run outside the UI thread."""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import Qt, QTimer, Signal, Slot
from PySide6.QtGui import QCloseEvent, QDragEnterEvent, QDropEvent, QFont, QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QAbstractItemView, QApplication, QComboBox, QDoubleSpinBox, QFileDialog, QFrame,
    QHBoxLayout, QHeaderView, QInputDialog, QLabel, QLineEdit, QMainWindow, QMenu,
    QMessageBox, QPlainTextEdit, QProgressBar, QPushButton, QScrollArea, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QTabWidget, QVBoxLayout, QWidget,
)

from . import __version__
from .core import Endpoint, OperationCancelled, PayloadInfo, TransferError, TransferResult, TransferUpdate, format_bytes
from .settings import Profile, SettingsStore
from .theme import apply_theme, colors, make_icon
from .workers import PayloadWorker


def label(text: str, role: str = "", name: str = "") -> QLabel:
    widget = QLabel(text)
    widget.setTextFormat(Qt.TextFormat.PlainText)
    if role:
        widget.setProperty("role", role)
    if name:
        widget.setObjectName(name)
    return widget


def button(text: str, name: str = "") -> QPushButton:
    widget = QPushButton(text)
    widget.setCursor(Qt.CursorShape.PointingHandCursor)
    if name:
        widget.setObjectName(name)
    return widget


def rule() -> QFrame:
    widget = QFrame()
    widget.setObjectName("Rule")
    widget.setFixedHeight(1)
    return widget


class DropArea(QFrame):
    selected = Signal(object)

    def __init__(self):
        super().__init__()
        self.setObjectName("DropArea")
        self.setAcceptDrops(True)
        self.setProperty("dragging", False)
        self.setMinimumHeight(152)

    def _highlight(self, active: bool):
        self.setProperty("dragging", active)
        self.style().unpolish(self)
        self.style().polish(self)

    def dragEnterEvent(self, event: QDragEnterEvent):
        urls = event.mimeData().urls()
        if self.isEnabled() and len(urls) == 1 and urls[0].isLocalFile():
            self._highlight(True)
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        self._highlight(False)
        event.accept()

    def dropEvent(self, event: QDropEvent):
        self._highlight(False)
        urls = event.mimeData().urls()
        if self.isEnabled() and len(urls) == 1 and urls[0].isLocalFile():
            self.selected.emit(Path(urls[0].toLocalFile()))
            event.acceptProposedAction()


class ContentRoot(QWidget):
    def heightForWidth(self, width: int) -> int:
        # Scroll only when the actual minimum layout no longer fits the window.
        return self.layout().minimumHeightForWidth(width)


class MainWindow(QMainWindow):
    def __init__(self, store: SettingsStore | None = None):
        super().__init__()
        self.store = store or SettingsStore()
        self.settings = self.store.load()
        self.payload: PayloadInfo | None = None
        self.worker: PayloadWorker | None = None
        self.job_kind = ""
        self.pending_path: Path | None = None
        self.last_phase = ""
        self.closing = False
        self.log_lines: list[str] = []
        self.setWindowTitle(f"QuayeWorks · PS4 Payload Sender {__version__}")
        self.resize(1120, 940)
        self.setMinimumSize(980, 720)
        self._build()
        self._load_profiles()
        self._apply_theme()
        self._refresh_history()
        self._refresh()
        self._log("READY", "Choose a payload and enter your console's IP address.")
        if self.store.warning:
            self._log("SETTINGS", self.store.warning)
        for sequence, handler in [("Ctrl+O", self.browse), ("Ctrl+Return", self.start_send),
                                  ("Escape", self.cancel_job), ("Ctrl+L", self.clear_log)]:
            shortcut = QShortcut(QKeySequence(sequence), self)
            shortcut.activated.connect(handler)

    def _build(self):
        root = ContentRoot()
        root.setObjectName("Root")
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setWidget(root)
        self.setCentralWidget(scroll)
        outer = QVBoxLayout(root)
        outer.setContentsMargins(28, 22, 28, 18)
        outer.setSpacing(20)

        top = QHBoxLayout()
        tile = label("QW", name="BrandTile")
        tile.setFixedSize(44, 44)
        tile.setAlignment(Qt.AlignmentFlag.AlignCenter)
        top.addWidget(tile)
        brand = QVBoxLayout()
        brand.setSpacing(2)
        brand.addWidget(label("QuayeWorks", name="Brand"))
        brand.addWidget(label("CONSOLE TOOLS", "eyebrow"))
        top.addLayout(brand)
        top.addStretch()
        self.theme_button = button("Light mode")
        self.theme_button.clicked.connect(self.toggle_theme)
        self.help_button = button("Quick start")
        self.help_button.clicked.connect(self.show_help)
        top.addWidget(self.theme_button)
        top.addWidget(self.help_button)
        outer.addLayout(top)

        heading = QHBoxLayout()
        titles = QVBoxLayout()
        titles.setSpacing(5)
        titles.addWidget(label("PS4 Payload Sender", name="PageTitle"))
        titles.addWidget(label("Your payload. Your console. One clean transfer.", "muted"))
        heading.addLayout(titles)
        heading.addStretch()
        self.status = label("●  IDLE", name="Status")
        self.status.setProperty("state", "idle")
        heading.addWidget(self.status, alignment=Qt.AlignmentFlag.AlignVCenter)
        outer.addLayout(heading)

        body = QHBoxLayout()
        body.setSpacing(20)
        sidebar = QFrame()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(286)
        side = QVBoxLayout(sidebar)
        side.setContentsMargins(20, 20, 20, 18)
        side.setSpacing(8)
        side.addWidget(label("01  /  DESTINATION", "eyebrow"))
        side.addWidget(label("Your console", "heading"))
        side.addSpacing(4)
        side.addWidget(label("SAVED PROFILE", "eyebrow"))
        self.profile_combo = QComboBox()
        self.profile_combo.setAccessibleName("Console profile")
        self.profile_combo.setMinimumContentsLength(12)
        self.profile_combo.currentIndexChanged.connect(self.profile_changed)
        side.addWidget(self.profile_combo)
        profile_actions = QHBoxLayout()
        profile_actions.setSpacing(4)
        self.save_profile_button = button("Save", "Link")
        self.add_profile_button = button("Add", "Link")
        self.delete_profile_button = button("Delete", "Link")
        self.save_profile_button.clicked.connect(self.save_profile)
        self.add_profile_button.clicked.connect(self.add_profile)
        self.delete_profile_button.clicked.connect(self.delete_profile)
        for item in (self.save_profile_button, self.add_profile_button, self.delete_profile_button):
            profile_actions.addWidget(item)
        profile_actions.addStretch()
        side.addLayout(profile_actions)
        side.addWidget(rule())
        side.addWidget(label("CONSOLE IP ADDRESS", "eyebrow"))
        self.host_input = QLineEdit()
        self.host_input.setPlaceholderText("192.168.1.100")
        self.host_input.setAccessibleName("Console IP address")
        self.host_input.setMaxLength(128)
        self.host_input.textChanged.connect(self._refresh)
        side.addWidget(self.host_input)
        side.addWidget(label("LOADER", "eyebrow"))
        self.loader_combo = QComboBox()
        self.loader_combo.addItems(["GoldHEN BIN Loader", "Raw TCP · port 9020", "Custom port"])
        self.loader_combo.setAccessibleName("Loader preset")
        self.loader_combo.currentIndexChanged.connect(self.loader_changed)
        side.addWidget(self.loader_combo)
        limits = QHBoxLayout()
        for title, widget in [("PORT", QSpinBox()), ("TIMEOUT", QDoubleSpinBox())]:
            column = QVBoxLayout()
            column.setSpacing(7)
            column.addWidget(label(title, "eyebrow"))
            column.addWidget(widget)
            limits.addLayout(column)
            if title == "PORT":
                self.port_input = widget
                widget.setRange(1, 65535)
                widget.setValue(9090)
                widget.setAccessibleName("Loader port")
                widget.valueChanged.connect(self.port_changed)
            else:
                self.timeout_input = widget
                widget.setRange(0.5, 120)
                widget.setDecimals(1)
                widget.setSingleStep(0.5)
                widget.setSuffix(" s")
                widget.setValue(10)
                widget.setAccessibleName("Connect and stall timeout")
        side.addLayout(limits)
        side.addStretch(1)
        hint = QFrame()
        hint.setObjectName("Hint")
        hints = QVBoxLayout(hint)
        hints.setContentsMargins(12, 10, 12, 10)
        text = label("Enable your PS4's BIN loader.\nKeep both devices on the same network.", "muted")
        text.setWordWrap(True)
        hints.addWidget(text)
        side.addWidget(hint)
        body.addWidget(sidebar)

        right = QVBoxLayout()
        right.setSpacing(16)
        payload_panel = QFrame()
        payload_panel.setObjectName("Panel")
        payload_layout = QVBoxLayout(payload_panel)
        payload_layout.setContentsMargins(22, 20, 22, 20)
        payload_layout.setSpacing(14)
        payload_heading = QHBoxLayout()
        payload_heading.addWidget(label("02  /  PAYLOAD", "eyebrow"))
        payload_heading.addStretch()
        payload_heading.addWidget(label("BIN  /  ELF", "eyebrow"))
        payload_layout.addLayout(payload_heading)
        self.drop_area = DropArea()
        self.drop_area.selected.connect(self.select_file)
        drop = QVBoxLayout(self.drop_area)
        drop.setContentsMargins(18, 18, 18, 18)
        drop.setSpacing(8)
        file_row = QHBoxLayout()
        file_row.setSpacing(16)
        self.file_symbol = label("", name="FileSymbol")
        self.file_symbol.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_symbol.setFixedSize(56, 60)
        file_row.addWidget(self.file_symbol)
        names = QVBoxLayout()
        names.setSpacing(5)
        self.file_name = label("Drop a payload here", name="FileName")
        self.file_name.setWordWrap(True)
        self.file_name.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        self.file_detail = label("Choose a .bin or .elf file to get started.", "muted")
        self.file_detail.setWordWrap(True)
        names.addWidget(self.file_name)
        names.addWidget(self.file_detail)
        file_row.addLayout(names, 1)
        drop.addLayout(file_row)
        browse_row = QHBoxLayout()
        self.browse_button = button("Browse files")
        self.browse_button.clicked.connect(self.browse)
        self.recent_button = button("Recent files", "Link")
        self.recent_button.clicked.connect(self.show_recent)
        self.clear_file_button = button("Remove", "Link")
        self.clear_file_button.clicked.connect(self.clear_file)
        browse_row.addWidget(self.browse_button)
        browse_row.addWidget(self.recent_button)
        browse_row.addStretch()
        browse_row.addWidget(self.clear_file_button)
        drop.addLayout(browse_row)
        payload_layout.addWidget(self.drop_area)
        hash_row = QHBoxLayout()
        hash_row.addWidget(label("SHA-256", "eyebrow"))
        self.hash_label = label("Calculated locally when you select a file", "muted")
        self.hash_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.hash_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        hash_row.addWidget(self.hash_label, 1)
        self.copy_hash_button = button("Copy", "Link")
        self.copy_hash_button.clicked.connect(self.copy_hash)
        hash_row.addWidget(self.copy_hash_button)
        payload_layout.addLayout(hash_row)
        right.addWidget(payload_panel)

        transfer_panel = QFrame()
        transfer_panel.setObjectName("Panel")
        transfer = QVBoxLayout(transfer_panel)
        transfer.setContentsMargins(22, 20, 22, 20)
        transfer.setSpacing(12)
        transfer.addWidget(label("03  /  TRANSFER", "eyebrow"))
        transfer_row = QHBoxLayout()
        self.stage_label = label("Ready when you are", name="Stage")
        self.percent_label = label("0%", name="Percent")
        transfer_row.addWidget(self.stage_label)
        transfer_row.addStretch()
        transfer_row.addWidget(self.percent_label)
        transfer.addLayout(transfer_row)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 1000)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setAccessibleName("Payload transfer progress")
        transfer.addWidget(self.progress_bar)
        stats = QHBoxLayout()
        self.bytes_label = label("0 B / 0 B", "muted")
        self.speed_label = label("— / s", "muted")
        self.elapsed_label = label("0.0 s", "muted")
        stats.addWidget(self.bytes_label)
        stats.addStretch()
        stats.addWidget(self.speed_label)
        stats.addSpacing(20)
        stats.addWidget(self.elapsed_label)
        transfer.addLayout(stats)
        self.feedback = label("A connection opens when you send.", name="Feedback")
        self.feedback.setWordWrap(True)
        self.feedback.setMinimumHeight(31)
        transfer.addWidget(self.feedback)
        actions = QHBoxLayout()
        self.send_button = button("Send payload", "Primary")
        self.send_button.clicked.connect(self.start_send)
        self.cancel_button = button("Cancel", "Danger")
        self.cancel_button.clicked.connect(self.cancel_job)
        actions.addWidget(self.send_button, 1)
        actions.addWidget(self.cancel_button)
        transfer.addLayout(actions)
        right.addWidget(transfer_panel)
        body.addLayout(right, 1)
        outer.addLayout(body)

        activity_panel = QFrame()
        activity_panel.setObjectName("Panel")
        activity = QVBoxLayout(activity_panel)
        activity.setContentsMargins(16, 10, 16, 14)
        activity.setSpacing(8)
        tabs_row = QHBoxLayout()
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBar().setDrawBase(False)
        self.log_view = QPlainTextEdit()
        self.log_view.setReadOnly(True)
        self.log_view.setMaximumBlockCount(500)
        self.log_view.setAccessibleName("Activity log")
        self.history_table = QTableWidget(0, 5)
        self.history_table.setHorizontalHeaderLabels(["PAYLOAD", "DESTINATION", "SIZE", "RESULT", "TIME"])
        self.history_table.verticalHeader().hide()
        self.history_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.history_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.history_table.setShowGrid(False)
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.tabs.addTab(self.log_view, "Activity")
        self.tabs.addTab(self.history_table, "Transfer history")
        tabs_row.addWidget(label("SESSION", "eyebrow"))
        tabs_row.addStretch()
        self.copy_log_button = button("Copy log", "Link")
        self.export_button = button("Export log", "Link")
        self.clear_log_button = button("Clear", "Link")
        self.copy_log_button.clicked.connect(self.copy_log)
        self.export_button.clicked.connect(self.export_log)
        self.clear_log_button.clicked.connect(self.clear_log)
        for item in (self.copy_log_button, self.export_button, self.clear_log_button):
            tabs_row.addWidget(item)
        activity.addLayout(tabs_row)
        activity.addWidget(self.tabs)
        activity_panel.setMinimumHeight(160)
        outer.addWidget(activity_panel, 1)
        footer = QHBoxLayout()
        footer.addWidget(label("LOCAL TCP  ·  NO ACCOUNT REQUIRED", "eyebrow"))
        footer.addStretch()
        footer.addWidget(label(f"PYTHON + QT  /  v{__version__}", "eyebrow"))
        outer.addLayout(footer)

    def _apply_theme(self):
        apply_theme(QApplication.instance(), self.settings.theme)
        c = colors(self.settings.theme)
        self.setWindowIcon(make_icon("brand", c["accent"], 64))
        self.file_symbol.setPixmap(make_icon("file", c["accent"], 32).pixmap(32, 32))
        self.send_button.setIcon(make_icon("send", c["accent_text"]))
        self.browse_button.setIcon(make_icon("folder", c["text"]))
        self.theme_button.setIcon(make_icon("theme", c["muted"]))
        self.theme_button.setText("Dark mode" if self.settings.theme == "light" else "Light mode")
        self.cancel_button.setIcon(make_icon("close", c["danger"], 16))

    def toggle_theme(self):
        self.settings.theme = "light" if self.settings.theme == "dark" else "dark"
        self._apply_theme()
        self._persist()

    def _persist(self):
        try:
            self.store.save(self.settings)
        except (OSError, ValueError) as exc:
            self._log("SETTINGS", f"Preferences could not be saved: {exc}")

    def _load_profiles(self):
        self.profile_combo.blockSignals(True)
        self.profile_combo.clear()
        self.profile_combo.addItems([p.name for p in self.settings.profiles])
        self.profile_combo.setCurrentIndex(self.settings.active_profile)
        self.profile_combo.blockSignals(False)
        self.profile_changed(self.settings.active_profile)

    def profile_changed(self, index: int):
        if not 0 <= index < len(self.settings.profiles):
            return
        self.settings.active_profile = index
        profile = self.settings.profiles[index]
        self.host_input.setText(profile.host)
        self.port_input.setValue(profile.port)
        self.port_changed(profile.port)
        self.timeout_input.setValue(profile.timeout)
        self._refresh()

    def loader_changed(self, index: int):
        if index in (0, 1):
            self.port_input.setValue(9090 if index == 0 else 9020)

    def port_changed(self, value: int):
        self.loader_combo.blockSignals(True)
        self.loader_combo.setCurrentIndex(0 if value == 9090 else 1 if value == 9020 else 2)
        self.loader_combo.blockSignals(False)

    def _endpoint(self) -> Endpoint:
        return Endpoint(self.host_input.text(), self.port_input.value(), self.timeout_input.value()).validate()

    def save_profile(self):
        if self.worker:
            return
        try:
            endpoint = self._endpoint()
        except TransferError as exc:
            self._feedback(str(exc), "error")
            return
        self._save_endpoint(endpoint)
        self._log("PROFILE", f"Saved {self.profile_combo.currentText()} · {endpoint.display}")
        self._feedback("Console profile saved.")

    def _save_endpoint(self, endpoint: Endpoint):
        profile = self.settings.profiles[self.settings.active_profile]
        profile.host, profile.port, profile.timeout = endpoint.host, endpoint.port, endpoint.timeout
        self._persist()

    def add_profile(self):
        if self.worker or len(self.settings.profiles) >= 50:
            return
        name, accepted = QInputDialog.getText(self, "Add console", "Profile name:", text="Another PS4")
        if accepted and name.strip():
            self.settings.profiles.append(Profile(name.strip()[:80]))
            self.settings.active_profile = len(self.settings.profiles) - 1
            self._load_profiles()
            self._persist()

    def delete_profile(self):
        if self.worker or len(self.settings.profiles) <= 1:
            return
        self.settings.profiles.pop(self.settings.active_profile)
        self.settings.active_profile = 0
        self._load_profiles()
        self._persist()

    def _refresh(self, *_):
        busy = self.worker is not None
        for widget in (self.host_input, self.port_input, self.timeout_input, self.profile_combo,
                       self.loader_combo, self.save_profile_button, self.add_profile_button):
            widget.setEnabled(not busy)
        self.delete_profile_button.setEnabled(not busy and len(self.settings.profiles) > 1)
        self.drop_area.setEnabled(not busy)
        self.clear_file_button.setEnabled(not busy and self.payload is not None)
        self.copy_hash_button.setEnabled(self.payload is not None)
        self.recent_button.setEnabled(not busy and bool(self.settings.recent_files))
        self.cancel_button.setEnabled(busy and not self.worker.cancel_event.is_set())
        try:
            self._endpoint()
            valid = True
        except TransferError:
            valid = False
        self.send_button.setEnabled(not busy and valid and self.payload is not None)
        self.send_button.setToolTip("Send the selected file (Ctrl+Enter)" if valid else "Enter a valid console IP address first")
        if not busy:
            self.send_button.setText("Send payload")

    def _badge(self, state: str, text: str):
        self.status.setText("●  " + text.upper())
        self.status.setProperty("state", state)
        self.status.style().unpolish(self.status)
        self.status.style().polish(self.status)

    def _feedback(self, text: str, state: str = ""):
        self.feedback.setText(text)
        self.feedback.setProperty("state", state)
        self.feedback.style().unpolish(self.feedback)
        self.feedback.style().polish(self.feedback)

    def _log(self, level: str, text: str):
        line = f"{datetime.now():%H:%M:%S}  {level:<8} {text}"
        self.log_lines.append(line)
        self.log_lines = self.log_lines[-500:]
        self.log_view.appendPlainText(line)

    def browse(self):
        if self.worker:
            return
        directory = str(self.payload.path.parent) if self.payload else ""
        path, _ = QFileDialog.getOpenFileName(self, "Choose a PS4 payload", directory,
                                            "Payloads (*.bin *.BIN *.elf *.ELF)")
        if path:
            self.select_file(Path(path))

    @Slot(object)
    def select_file(self, path: Path):
        if self.worker:
            return
        self.payload = None
        self.pending_path = Path(path)
        self.file_name.setText(self.pending_path.name)
        self.file_detail.setText("Inspecting file and calculating SHA-256…")
        self.hash_label.setText("Calculating…")
        self._feedback("Reading your file locally.")
        self._start_worker(PayloadWorker(self.pending_path, parent=self), "inspect")

    def _start_worker(self, worker: PayloadWorker, kind: str):
        self.worker = worker
        self.job_kind = kind
        self.last_phase = ""
        self.progress_bar.setValue(0)
        self.percent_label.setText("0%")
        self.elapsed_label.setText("0.0 s")
        self.speed_label.setText("— / s")
        worker.progress.connect(self.progress_changed)
        worker.inspected.connect(self.inspection_finished)
        worker.transferred.connect(self.transfer_finished)
        worker.failed.connect(self.job_failed)
        worker.finished.connect(self.worker_stopped)
        self._refresh()
        worker.start()

    @Slot(object)
    def inspection_finished(self, info: PayloadInfo):
        self.payload = info
        self.file_name.setText(info.path.name)
        self.file_name.setToolTip(str(info.path))
        self.file_detail.setText(f"{format_bytes(info.size)}  ·  {info.path.suffix[1:].upper()} payload")
        self.hash_label.setText(info.sha256[:24] + "…")
        self.hash_label.setToolTip(info.sha256)
        self.progress_bar.setValue(0)
        self.percent_label.setText("0%")
        self.bytes_label.setText(f"0 B / {format_bytes(info.size)}")
        self.stage_label.setText("Ready to send")
        self._badge("ready", "Payload ready")
        self._feedback("Payload inspected. Enable your loader, then send.")
        path = str(info.path)
        self.settings.recent_files = [path] + [p for p in self.settings.recent_files if p != path][:7]
        self._persist()
        self._log("FILE", f"{info.path.name} · {format_bytes(info.size)} · SHA-256 {info.sha256}")

    def start_send(self):
        if self.worker or self.payload is None:
            return
        try:
            endpoint = self._endpoint()
        except TransferError as exc:
            self._feedback(str(exc), "error")
            return
        self._save_endpoint(endpoint)
        self._feedback(f"Sending to {endpoint.display}.")
        self._log("SEND", f"{self.payload.path.name} → {endpoint.display}")
        self._start_worker(PayloadWorker(self.payload.path, endpoint, self.payload, self), "send")
        self.send_button.setText("Sending…")

    @Slot(object)
    def progress_changed(self, event: TransferUpdate):
        if event.phase != self.last_phase:
            self.last_phase = event.phase
            titles = {"preparing": "Inspecting payload" if self.job_kind == "inspect" else "Preparing verified payload",
                      "connecting": "Connecting to your console", "sending": "Sending payload", "complete": "Transfer complete"}
            self.stage_label.setText(titles.get(event.phase, event.phase))
            self._badge("complete" if event.phase == "complete" else "busy", event.phase)
            if event.phase == "connecting":
                self._log("CONNECT", "Opening the payload connection.")
            elif event.phase == "sending":
                self._log("CONNECTED", "Console accepted the TCP connection. Streaming payload bytes.")
        fraction = min(1.0, event.completed / max(event.total, 1))
        self.progress_bar.setValue(round(fraction * 1000))
        self.percent_label.setText(f"{fraction:.0%}")
        self.bytes_label.setText(f"{format_bytes(event.completed)} / {format_bytes(event.total)}")
        if event.phase in ("sending", "complete"):
            self.elapsed_label.setText(f"{event.elapsed:.1f} s")
            if event.elapsed > 0:
                self.speed_label.setText(f"{format_bytes(event.completed / event.elapsed)} / s")

    @Slot(object)
    def transfer_finished(self, result: TransferResult):
        self._badge("complete", "Transfer complete")
        self.stage_label.setText("Transfer complete")
        self._feedback("All payload bytes sent. Verify execution on your PS4.", "complete")
        self._log("SENT", f"{format_bytes(result.bytes_sent)} → {result.endpoint.display} · {result.elapsed:.3f} s")
        self._log("NOTE", "The loader does not provide an execution acknowledgement.")
        self._record_history("Sent", result.endpoint, result.bytes_sent)

    @Slot(object)
    def job_failed(self, error: TransferError):
        canceled = isinstance(error, OperationCancelled)
        self._badge("idle" if canceled else "error", "Canceled" if canceled else "Needs attention")
        if self.job_kind == "inspect":
            self.stage_label.setText("Inspection canceled" if canceled else "File not ready")
        else:
            self.stage_label.setText("Transfer canceled" if canceled else "Transfer interrupted")
        self._feedback(str(error), "" if canceled else "error")
        self._log("CANCELED" if canceled else "ERROR", str(error))
        if self.job_kind == "inspect":
            self.file_detail.setText("File not ready. Choose a valid payload.")
            self.hash_label.setText("Not available")
        elif self.worker and self.worker.endpoint:
            self._record_history("Canceled" if canceled else "Failed", self.worker.endpoint, error.bytes_sent)

    @Slot()
    def worker_stopped(self):
        worker = self.worker
        self.worker = None
        self.job_kind = ""
        if worker:
            worker.deleteLater()
        self._refresh()
        if self.closing:
            self.close()

    def cancel_job(self):
        if self.worker and not self.worker.cancel_event.is_set():
            self.worker.cancel()
            self._feedback("Canceling the current operation…")
            self._refresh()

    def clear_file(self):
        if self.worker:
            return
        self.payload = None
        self.file_name.setText("Drop a payload here")
        self.file_detail.setText("Choose a .bin or .elf file to get started.")
        self.hash_label.setText("Calculated locally when you select a file")
        self.hash_label.setToolTip("")
        self.progress_bar.setValue(0)
        self.percent_label.setText("0%")
        self.bytes_label.setText("0 B / 0 B")
        self.speed_label.setText("— / s")
        self.elapsed_label.setText("0.0 s")
        self.stage_label.setText("Ready when you are")
        self._badge("idle", "Idle")
        self._feedback("A connection opens when you send.")
        self._refresh()

    def show_recent(self):
        if self.worker:
            return
        menu = QMenu(self)
        for path in self.settings.recent_files:
            action = menu.addAction(Path(path).name)
            action.setToolTip(path)
            action.setEnabled(Path(path).is_file())
            action.triggered.connect(lambda checked=False, p=path: self.select_file(Path(p)))
        menu.exec(self.recent_button.mapToGlobal(self.recent_button.rect().bottomLeft()))

    def copy_hash(self):
        if self.payload:
            QApplication.clipboard().setText(self.payload.sha256)
            self._feedback("Full SHA-256 copied to the clipboard.")

    def copy_log(self):
        QApplication.clipboard().setText("\n".join(self.log_lines))
        self._feedback("Session log copied to the clipboard.")

    def clear_log(self):
        self.log_lines.clear()
        self.log_view.clear()

    def export_log(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export session log",
                                            f"payload-sender-{datetime.now():%Y%m%d-%H%M%S}.log", "Log files (*.log)")
        if path:
            try:
                Path(path).write_text("\n".join(self.log_lines) + "\n", encoding="utf-8")
                self._feedback("Session log exported.")
            except OSError as exc:
                self._feedback(f"Could not export the log: {exc}", "error")

    def _record_history(self, status: str, endpoint: Endpoint, submitted: int):
        self.settings.history.insert(0, {"file": self.payload.path.name if self.payload else "Unknown",
                                       "destination": endpoint.display, "bytes": submitted, "status": status,
                                       "time": datetime.now().astimezone().isoformat(timespec="seconds"),
                                       "sha256": self.payload.sha256 if self.payload else ""})
        self.settings.history = self.settings.history[:30]
        self._refresh_history()
        self._persist()

    def _refresh_history(self):
        self.history_table.setRowCount(len(self.settings.history))
        for row, item in enumerate(self.settings.history):
            try:
                size = format_bytes(max(0, int(item.get("bytes", 0))))
            except (ValueError, TypeError, OverflowError):
                size = "—"
            values = [item.get("file", ""), item.get("destination", ""), size,
                      item.get("status", ""), str(item.get("time", "")).replace("T", " ")]
            for column, value in enumerate(values):
                cell = QTableWidgetItem(str(value))
                cell.setToolTip(str(value))
                self.history_table.setItem(row, column, cell)

    def show_help(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Quick start")
        dialog.setTextFormat(Qt.TextFormat.PlainText)
        dialog.setText("1. Enable your PS4's BIN loader.\n\n"
                       "2. Enter the console's IP address and the loader's port. GoldHEN uses 9090.\n\n"
                       "3. Browse or drop a .bin/.elf payload supported by that loader.\n\n"
                       "4. Click Send payload and verify execution on the console.\n\n"
                       "A fresh TCP connection is opened for each send. There is no execution acknowledgement. "
                       "After a partial transfer, check/restart your loader before manually resending.\n\n"
                       "Shortcuts: Ctrl+O browse · Ctrl+Enter send · Esc cancel · Ctrl+L clear log")
        dialog.exec()

    def closeEvent(self, event: QCloseEvent):
        if self.worker:
            self.closing = True
            self.cancel_job()
            event.ignore()
        else:
            self._persist()
            event.accept()


def run_gui(config_dir: Path | None = None, payload: Path | None = None,
            host: str | None = None, port: int = 9090, timeout: float = 10) -> int:
    app = QApplication([sys.argv[0]])
    app.setApplicationName("QuayeWorks PS4 Payload Sender")
    app.setOrganizationName("QuayeWorks")
    app.setStyle("Fusion")
    app.setFont(QFont("Segoe UI", 10))
    window = MainWindow(SettingsStore(config_dir))
    if host:
        window.host_input.setText(host)
        window.port_input.setValue(max(1, min(65535, port)))
        window.timeout_input.setValue(timeout)
    window.show()
    if payload:
        QTimer.singleShot(0, lambda: window.select_file(payload))
    return app.exec()
