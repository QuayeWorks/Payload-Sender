import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import tempfile
import time
import unittest
from pathlib import Path

try:
    from PySide6.QtCore import QMimeData, QPointF, QTimer, QUrl, Qt
    from PySide6.QtGui import QDragEnterEvent, QDropEvent
    from PySide6.QtWidgets import QApplication
    from payload_sender.gui import MainWindow
    from payload_sender.settings import SettingsStore
    QT_AVAILABLE = True
except ImportError:
    QT_AVAILABLE = False

from tests.support import Receiver


@unittest.skipUnless(QT_AVAILABLE, "Install requirements.txt to run GUI tests")
class GuiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        cls.app.setStyle("Fusion")

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.directory = Path(self.temporary.name)
        self.path = self.directory / "test-payload.bin"
        self.data = bytes(range(256)) * 1024
        self.path.write_bytes(self.data)
        self.window = MainWindow(SettingsStore(self.directory / "config"))
        self.window.show()
        self.app.processEvents()

    def tearDown(self):
        self.window.close()
        self.wait_for(lambda: self.window.worker is None)
        self.window.close()
        self.app.processEvents()
        self.temporary.cleanup()

    def wait_for(self, condition, timeout=4):
        deadline = time.monotonic() + timeout
        while not condition() and time.monotonic() < deadline:
            self.app.processEvents()
            time.sleep(0.005)
        self.app.processEvents()
        self.assertTrue(condition(), "UI operation did not complete")

    def select(self):
        self.window.select_file(self.path)
        self.wait_for(lambda: self.window.worker is None)

    def test_real_selection_send_history_and_return_to_ready(self):
        self.assertFalse(self.window.send_button.isEnabled())
        self.select()
        self.assertIsNotNone(self.window.payload)
        self.assertFalse(self.window.send_button.isEnabled())
        with Receiver() as receiver:
            self.window.host_input.setText(receiver.host)
            self.window.port_input.setValue(receiver.port)
            self.assertTrue(self.window.send_button.isEnabled())
            self.window.start_send()
            self.assertFalse(self.window.host_input.isEnabled())
            self.assertFalse(self.window.send_button.isEnabled())
            self.wait_for(lambda: self.window.worker is None)
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)
        self.assertEqual(self.window.progress_bar.value(), 1000)
        self.assertEqual(self.window.settings.history[0]["status"], "Sent")
        self.assertTrue(self.window.send_button.isEnabled())
        self.assertFalse(self.window.cancel_button.isEnabled())

    def test_stalled_transfer_keeps_ui_responsive_and_cancels(self):
        self.path.write_bytes(b"x" * (16 * 1024 * 1024))
        self.select()
        ticks = []
        timer = QTimer(self.window)
        timer.setInterval(10)
        timer.timeout.connect(lambda: ticks.append(1))
        with Receiver(stall=True) as receiver:
            self.window.host_input.setText(receiver.host)
            self.window.port_input.setValue(receiver.port)
            self.window.start_send()
            timer.start()
            self.wait_for(lambda: receiver.accepted.is_set() and len(ticks) >= 5)
            self.assertIsNotNone(self.window.worker)
            self.window.cancel_job()
            self.wait_for(lambda: self.window.worker is None)
            timer.stop()
        self.assertEqual(self.window.settings.history[0]["status"], "Canceled")
        self.assertIn("Canceled", self.window.stage_label.text().title())

    def test_closing_cancels_worker_without_destroying_running_thread(self):
        self.path.write_bytes(b"x" * (16 * 1024 * 1024))
        self.select()
        with Receiver(stall=True) as receiver:
            self.window.host_input.setText(receiver.host)
            self.window.port_input.setValue(receiver.port)
            self.window.start_send()
            self.wait_for(receiver.accepted.is_set)
            self.window.close()
            self.wait_for(lambda: self.window.worker is None and not self.window.isVisible())

    def test_refused_connection_reports_error_and_restores_controls(self):
        import socket
        self.select()
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            self.window.host_input.setText("127.0.0.1")
            self.window.port_input.setValue(listener.getsockname()[1])
            self.window.start_send()
            self.wait_for(lambda: self.window.worker is None)
        self.assertEqual(self.window.settings.history[0]["status"], "Failed")
        self.assertIn("refused", self.window.feedback.text())
        self.assertTrue(self.window.send_button.isEnabled())

    def test_theme_port_profile_and_clipboard_controls(self):
        self.window.toggle_theme()
        self.assertEqual(self.window.settings.theme, "light")
        self.assertEqual(self.window.store.load().theme, "light")
        self.window.loader_combo.setCurrentIndex(1)
        self.assertEqual(self.window.port_input.value(), 9020)
        self.window.port_input.setValue(9500)
        self.assertEqual(self.window.loader_combo.currentIndex(), 2)
        self.window.host_input.setText("127.0.0.1")
        self.window.save_profile()
        self.assertEqual(self.window.store.load().profiles[0].port, 9500)
        self.select()
        self.window.copy_hash()
        self.assertEqual(self.app.clipboard().text(), self.window.payload.sha256)
        self.window.copy_log()
        self.assertIn("SHA-256", self.app.clipboard().text())

    def test_clear_payload_resets_transfer_metrics_and_disables_send(self):
        self.select()
        self.window.host_input.setText("127.0.0.1")
        self.assertTrue(self.window.send_button.isEnabled())
        self.window.clear_file()
        self.assertIsNone(self.window.payload)
        self.assertFalse(self.window.send_button.isEnabled())
        self.assertEqual(self.window.progress_bar.value(), 0)
        self.assertEqual(self.window.bytes_label.text(), "0 B / 0 B")

    def test_drag_and_drop_selects_payload(self):
        mime = QMimeData()
        mime.setUrls([QUrl.fromLocalFile(str(self.path))])
        enter = QDragEnterEvent(QPointF(10, 10), Qt.DropAction.CopyAction, mime,
                               Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
        self.app.sendEvent(self.window.drop_area, enter)
        self.assertTrue(enter.isAccepted())
        drop = QDropEvent(QPointF(10, 10), Qt.DropAction.CopyAction, mime,
                          Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
        self.app.sendEvent(self.window.drop_area, drop)
        self.wait_for(lambda: self.window.worker is None)
        self.assertEqual(self.window.payload.path, self.path)
        self.assertFalse(self.window.drop_area.property("dragging"))

    def test_unsupported_dropped_file_displays_validation_error(self):
        invalid = self.path.with_suffix(".txt")
        invalid.write_bytes(b"not a payload")
        self.window.select_file(invalid)
        self.wait_for(lambda: self.window.worker is None)
        self.assertIsNone(self.window.payload)
        self.assertIn(".bin or .elf", self.window.feedback.text())
        self.assertEqual(self.window.stage_label.text(), "File not ready")

    def test_small_window_scrolls_and_numeric_fields_remain_visible(self):
        self.assertEqual(self.window.centralWidget().verticalScrollBar().maximum(), 0)
        self.assertGreater(self.window.port_input.lineEdit().width(), 50)
        self.assertGreater(self.window.timeout_input.lineEdit().width(), 50)
        self.window.resize(980, 720)
        self.app.processEvents()
        self.assertGreater(self.window.centralWidget().verticalScrollBar().maximum(), 0)


if __name__ == "__main__":
    unittest.main()
