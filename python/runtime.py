# -*- coding: utf-8 -*-

import os
import sys
from typing import Any

import PySide6
from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QLabel, QApplication

from python.internal import _requester
from python.internal.static.assets import _style_sheets


class MainWindow(QWidget):
    def __init__(self, parent: Any = None) -> None:
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = \
            os.path.join(os.path.dirname(PySide6.__file__), "plugins", "platforms")

        super().__init__(parent)

        self.button, self.text_edit, self.label = None, None, None

        self.setWindowTitle("FireSB")
        self.resize(800, 700)

        self.set_label(70, 85)
        self.set_button(240, 50)
        self.set_text_edit(70, 50)

    def set_label(self, x_pos: int, y_pos: int) -> None:
        self.label = QLabel(self)

        self.label.setStyleSheet(_style_sheets.LABEL_STYLE)
        self.label.setText("\"projects.scratch.mit.edu\" などの\r\nproject.json が取得できる URL を入力してください...")
        self.label.move(x_pos, y_pos)
        self.label.resize(250, 30)

    def set_button(self, x_pos: int, y_pos: int) -> None:
        self.button = QPushButton(self)

        self.button.setStyleSheet(_style_sheets.BUTTON_STYLE)
        self.button.setText("解析する!")
        self.button.move(x_pos, y_pos)
        self.button.resize(75, 25)
        self.button.clicked.connect(lambda: self.analyze(None))

    def set_text_edit(self, x_pos: int, y_pos: int) -> None:
        self.text_edit = QTextEdit(self)

        self.text_edit.setStyleSheet(_style_sheets.TEXT_EDIT_STYLE)
        self.text_edit.move(x_pos, y_pos)
        self.text_edit.resize(150, 25)

    def analyze(self, status) -> None:
        self.button.setEnabled(False)

        _status = status

        project_url = \
            self.text_edit.toPlainText().translate(str.maketrans({chr(0xFF01 + x): chr(0x21 + x) for x in range(94)}))
        project_data = _requester.Require().get_project_data(project_url)

        if project_data is None:
            self.label.setText("データの取得に失敗しました - 再試行してみてください")

        else:
            self.label.setText("データの取得が完了しました!")


app = QApplication(sys.argv).instance()
window = MainWindow()
window.show()
sys.exit(app.exec())
