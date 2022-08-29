# -*- coding: utf-8 -*-

import os
import sys

import PySide6
from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QLabel, QApplication

from internal import _requester
from internal.static.assets import style_sheets


class MainWindow(QWidget):
    def __init__(self, parent=None) -> None:
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = \
            os.path.join(os.path.dirname(PySide6.__file__), "plugins", "platforms")

        super().__init__(parent)

        self.button, self.text_edit, self.label = None, None, None

        self.setWindowTitle("FireSB")
        self.resize(600, 500)

        self.set_label(150, 85)
        self.set_button(320, 50)
        self.set_text_edit(150, 50)

    def set_label(self, x_pos: int, y_pos: int) -> None:
        self.label = QLabel(self)

        self.label.setStyleSheet(style_sheets.label_style)
        self.label.setText("入力待ちです...")
        self.label.move(x_pos, y_pos)
        self.label.resize(250, 25)

    def set_button(self, x_pos: int, y_pos: int) -> None:
        self.button = QPushButton(self)

        self.button.setStyleSheet(style_sheets.button_style)
        self.button.setText("解析する!")
        self.button.move(x_pos, y_pos)
        self.button.resize(75, 25)
        self.button.clicked.connect(self.analyze)

    def set_text_edit(self, x_pos: int, y_pos: int) -> None:
        self.text_edit = QTextEdit(self)

        self.text_edit.setStyleSheet(style_sheets.text_edit_style)
        self.text_edit.move(x_pos, y_pos)
        self.text_edit.resize(150, 25)

    def analyze(self) -> None:
        self.button.setEnabled(False)

        p_id = \
            self.text_edit.toPlainText().translate(str.maketrans({chr(0xFF01 + x): chr(0x21 + x) for x in range(94)}))
        data = _requester.Require.get_project_data(p_id)

        if data is None:
            self.label.setText("データの取得に失敗しました - 再試行してみてください")

        else:
            self.label.setText("データの取得が完了しました!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
