# -*- coding: utf-8 -*-

import os
import sys

import PySide6
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit


class MainWindow(QWidget):
    def __init__(self, parent=None):
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = \
            os.path.join(os.path.dirname(PySide6.__file__), "plugins", "platforms")

        super().__init__(parent)

        self.button, self.text_edit = None, None

        self.setWindowTitle("FireSB")
        self.resize(600, 500)

        self.set_button()
        self.set_text_edit()

    def set_button(self):
        self.button = QPushButton(self)

        self.button.setText("解析する!")
        self.button.move(320, 50)
        self.button.resize(75, 25)
        self.button.clicked.connect(self.convert)

    def set_text_edit(self):
        self.text_edit = QTextEdit(self)

        self.text_edit.move(150, 50)
        self.text_edit.resize(150, 25)

    def convert(self):
        print(self.text_edit.toPlainText().translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)})))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
