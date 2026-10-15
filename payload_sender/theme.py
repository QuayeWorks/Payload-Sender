"""Two complete desktop themes and small, locally drawn interface icons."""

from pathlib import Path

from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QFont, QIcon, QPainter, QPainterPath, QPalette, QPen, QPixmap

DARK = dict(bg="#0B111B", panel="#121C2A", sidebar="#0F1825", inset="#0C1420",
            line="#29374A", text="#EBF1F8", muted="#94A6BD", accent="#80E7C1",
            accent_hover="#A5F0D6", accent_text="#10291F", danger="#FF9DAB", hover="#1D2C40")
LIGHT = dict(bg="#F0F4F8", panel="#FFFFFF", sidebar="#E6EDF4", inset="#F4F7FA",
             line="#CAD5E1", text="#15263A", muted="#566A80", accent="#137D5A",
             accent_hover="#0F694C", accent_text="#FFFFFF", danger="#B32947", hover="#E6EEF5")


def colors(theme: str) -> dict:
    return LIGHT if theme == "light" else DARK


def apply_theme(app, theme: str) -> None:
    c = colors(theme)
    assets = Path(__file__).resolve().parents[1] / "assets"
    c = {**c, "arrow": (assets / f"chevron-{theme}.png").as_posix(),
         "up_arrow": (assets / f"up-{theme}.png").as_posix()}
    palette = QPalette()
    for role, value in [(QPalette.ColorRole.Window, c["bg"]),
                        (QPalette.ColorRole.WindowText, c["text"]),
                        (QPalette.ColorRole.Base, c["inset"]),
                        (QPalette.ColorRole.AlternateBase, c["panel"]),
                        (QPalette.ColorRole.Text, c["text"]),
                        (QPalette.ColorRole.Button, c["panel"]),
                        (QPalette.ColorRole.ButtonText, c["text"]),
                        (QPalette.ColorRole.Highlight, c["accent"]),
                        (QPalette.ColorRole.HighlightedText, c["accent_text"]),
                        (QPalette.ColorRole.PlaceholderText, c["muted"]),
                        (QPalette.ColorRole.ToolTipBase, c["panel"]),
                        (QPalette.ColorRole.ToolTipText, c["text"])]:
        palette.setColor(role, QColor(value))
    app.setPalette(palette)
    app.setStyleSheet("""
        QWidget { color: %(text)s; font-family: "Segoe UI", "DejaVu Sans", sans-serif; font-size: 13px; }
        QMainWindow, QWidget#Root { background: %(bg)s; }
        QLabel { background: transparent; border: none; }
        QLabel[role="muted"] { color: %(muted)s; }
        QLabel[role="eyebrow"] { color: %(muted)s; font-size: 10px; font-weight: 700; letter-spacing: 1px; }
        QLabel[role="heading"] { font-size: 18px; font-weight: 600; }
        QLabel#PageTitle { font-size: 30px; font-weight: 700; }
        QLabel#Brand { font-size: 17px; font-weight: 700; }
        QLabel#BrandTile { background: %(accent)s; color: %(accent_text)s; font-size: 18px;
                           font-weight: 800; border-radius: 11px; }
        QLabel#Status { background: %(panel)s; border: 1px solid %(line)s; border-radius: 13px; padding: 5px 12px;
                        font-size: 11px; font-weight: 600; color: %(muted)s; }
        QLabel#Status[state="ready"], QLabel#Status[state="complete"] { color: %(accent)s; border-color: %(accent)s; }
        QLabel#Status[state="error"] { color: %(danger)s; border-color: %(danger)s; }
        QLabel#FileName { font-size: 20px; font-weight: 600; }
        QLabel#FileSymbol { background: %(hover)s; border-radius: 16px; }
        QLabel#Stage { font-size: 16px; font-weight: 600; }
        QLabel#Percent { font-size: 24px; font-weight: 700; color: %(accent)s; }
        QLabel#Feedback { font-size: 12px; color: %(muted)s; }
        QLabel#Feedback[state="error"] { color: %(danger)s; }
        QLabel#Feedback[state="complete"] { color: %(accent)s; }
        QFrame#Panel { background: %(panel)s; border: 1px solid %(line)s; border-radius: 16px; }
        QFrame#Sidebar { background: %(sidebar)s; border: 1px solid %(line)s; border-radius: 16px; }
        QFrame#DropArea { background: %(inset)s; border: 1px dashed %(line)s; border-radius: 12px; }
        QFrame#DropArea[dragging="true"] { border: 2px dashed %(accent)s; background: %(hover)s; }
        QFrame#Rule { background: %(line)s; border: none; max-height: 1px; }
        QFrame#Hint { background: %(inset)s; border-radius: 10px; }
        QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {
            background: %(inset)s; border: 1px solid %(line)s; border-radius: 8px;
            padding: 10px; selection-background-color: %(accent)s; selection-color: %(accent_text)s;
            min-height: 18px;
        }
        QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus { border-color: %(accent)s; }
        QLineEdit:disabled, QComboBox:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled { color: %(muted)s; }
        QComboBox::drop-down { border: none; width: 23px; }
        QComboBox::down-arrow { image: url("%(arrow)s"); width: 12px; height: 8px; }
        QComboBox QAbstractItemView { background: %(panel)s; border: 1px solid %(line)s;
                                    selection-background-color: %(hover)s; padding: 6px; }
        QSpinBox::up-button, QDoubleSpinBox::up-button, QSpinBox::down-button, QDoubleSpinBox::down-button {
            width: 16px; border: none; background: %(hover)s;
        }
        QSpinBox QLineEdit, QDoubleSpinBox QLineEdit {
            background: transparent; border: none; padding: 0px; padding-left: 10px; padding-right: 4px;
            min-height: 0px;
        }
        QSpinBox::up-arrow, QDoubleSpinBox::up-arrow { image: url("%(up_arrow)s"); width: 8px; height: 5px; }
        QSpinBox::down-arrow, QDoubleSpinBox::down-arrow { image: url("%(arrow)s"); width: 8px; height: 5px; }
        QPushButton, QToolButton {
            background: %(panel)s; border: 1px solid %(line)s; border-radius: 8px;
            padding: 9px 13px; font-weight: 600; min-height: 18px;
        }
        QPushButton:hover, QToolButton:hover { background: %(hover)s; border-color: %(muted)s; }
        QPushButton:focus, QToolButton:focus { border: 1px solid %(accent)s; }
        QPushButton:disabled, QToolButton:disabled { color: %(muted)s; background: %(inset)s; }
        QPushButton#Primary { background: %(accent)s; color: %(accent_text)s; border: none;
                              padding: 13px 20px; font-size: 14px; }
        QPushButton#Primary:hover { background: %(accent_hover)s; }
        QPushButton#Primary:disabled { background: %(hover)s; color: %(muted)s; }
        QPushButton#Link { background: transparent; border: none; padding: 4px 6px; font-size: 12px; }
        QPushButton#Link:hover { color: %(accent)s; }
        QPushButton#Danger { color: %(danger)s; }
        QPushButton#Danger:disabled { color: %(muted)s; }
        QProgressBar { background: %(inset)s; border: none; border-radius: 4px; height: 7px; max-height: 7px; }
        QProgressBar::chunk { background: %(accent)s; border-radius: 4px; }
        QTabWidget::pane { border: none; }
        QTabBar::tab { background: transparent; color: %(muted)s; padding: 8px 13px;
                      border-bottom: 2px solid transparent; font-weight: 600; }
        QTabBar::tab:selected { color: %(text)s; border-bottom: 2px solid %(accent)s; }
        QPlainTextEdit { background: %(inset)s; border: 1px solid %(line)s; border-radius: 8px;
                         padding: 9px; font-family: "Cascadia Code", "DejaVu Sans Mono", monospace; font-size: 11px; }
        QTableWidget { background: %(inset)s; border: 1px solid %(line)s; border-radius: 8px;
                       gridline-color: %(line)s; font-size: 11px; selection-background-color: %(hover)s; }
        QHeaderView::section { background: %(panel)s; color: %(muted)s; border: none;
                              padding: 7px 8px; font-size: 10px; font-weight: 600; }
        QScrollBar:vertical { background: transparent; width: 7px; margin: 2px; }
        QScrollBar::handle:vertical { background: %(line)s; border-radius: 3px; min-height: 18px; }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }
        QMenu { background: %(panel)s; border: 1px solid %(line)s; padding: 5px; }
        QMenu::item { padding: 8px 18px; }
        QMenu::item:selected { background: %(hover)s; }
        QToolTip { background: %(panel)s; color: %(text)s; border: 1px solid %(line)s; padding: 6px; }
        QMessageBox, QInputDialog, QFileDialog { background: %(bg)s; }
    """ % c)


def make_icon(name: str, color: str, size: int = 20) -> QIcon:
    pixmap = QPixmap(size * 2, size * 2)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.scale(size / 12, size / 12)  # Draw on a 24-unit canvas at 2x resolution.
    painter.setPen(QPen(QColor(color), 1.7, Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
    if name == "send":
        path = QPainterPath(QPointF(3, 3))
        for point in [(21, 12), (3, 21), (7, 12), (3, 3)]:
            path.lineTo(*point)
        painter.drawPath(path)
        painter.drawLine(QPointF(7, 12), QPointF(21, 12))
    elif name == "file":
        path = QPainterPath(QPointF(6, 2))
        for point in [(14, 2), (19, 7), (19, 22), (5, 22), (5, 2), (6, 2)]:
            path.lineTo(*point)
        painter.drawPath(path)
        painter.drawLine(QPointF(14, 2), QPointF(14, 7))
        painter.drawLine(QPointF(14, 7), QPointF(19, 7))
        painter.drawLine(QPointF(9, 12), QPointF(15, 12))
        painter.drawLine(QPointF(9, 16), QPointF(15, 16))
    elif name == "folder":
        path = QPainterPath(QPointF(3, 6))
        for point in [(10, 6), (12, 9), (21, 9), (21, 20), (3, 20), (3, 6)]:
            path.lineTo(*point)
        painter.drawPath(path)
    elif name == "theme":
        painter.drawEllipse(QRectF(6, 6, 12, 12))
        for a, b in [((12, 1), (12, 3)), ((12, 21), (12, 23)), ((1, 12), (3, 12)),
                     ((21, 12), (23, 12)), ((4, 4), (5.5, 5.5)), ((18.5, 18.5), (20, 20)),
                     ((4, 20), (5.5, 18.5)), ((18.5, 5.5), (20, 4))]:
            painter.drawLine(QPointF(*a), QPointF(*b))
    elif name == "close":
        painter.drawLine(QPointF(6, 6), QPointF(18, 18))
        painter.drawLine(QPointF(18, 6), QPointF(6, 18))
    elif name == "check":
        painter.drawLine(QPointF(4, 12), QPointF(9, 17))
        painter.drawLine(QPointF(9, 17), QPointF(20, 6))
    else:
        painter.drawRoundedRect(QRectF(2, 2, 20, 20), 5, 5)
        painter.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        painter.drawText(QRectF(2, 2, 20, 20), Qt.AlignmentFlag.AlignCenter, "Q")
    painter.end()
    pixmap.setDevicePixelRatio(2)
    return QIcon(pixmap)
