# -*- coding: utf-8 -*-

import os
import sys

import PySide6
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QApplication


class MainWindow(QWidget):
    def __init__(self, parent=None):
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.path.join(os.path.dirname(PySide6.__file__), "plugins", "platforms")

        super().__init__(parent)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
