# -*- coding: utf-8 -*-

import gc
import os
import sys

import psutil
import PySide6
from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QLabel, QApplication

from python.internal import _requester
from python.internal.static.assets import _style_sheets


class MainProcess(QWidget):
    def __init__(self, parent: None | QWidget = None) -> None:
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = \
            os.path.join(os.path.dirname(PySide6.__file__), "plugins", "platforms")

        self.system = System()
        self.require = _requester.Require()

        super().__init__(parent)

        self.button_1, self.text_edit, self.label = None, None, None

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
        self.button_1 = QPushButton(self)

        self.button_1.setStyleSheet(_style_sheets.BUTTON_STYLE)
        self.button_1.setText("解析する!")
        self.button_1.move(x_pos, y_pos)
        self.button_1.resize(75, 25)
        self.button_1.clicked.connect(lambda: self.analyze(None))

    def set_text_edit(self, x_pos: int, y_pos: int) -> None:
        self.text_edit = QTextEdit(self)

        self.text_edit.setStyleSheet(_style_sheets.TEXT_EDIT_STYLE)
        self.text_edit.move(x_pos, y_pos)
        self.text_edit.resize(150, 25)

    def analyze(self, status) -> None:
        self.button_1.setEnabled(False)

        _status = status

        try:  # TODO: この try-except 部分の処理の考案
            project_url = \
                self.text_edit.toPlainText().translate(str.maketrans(
                    {chr(0xFF01 + x): chr(0x21 + x) for x in range(94)}))
            project_data = self.require.get_project_data(project_url)

        except Exception:
            self.system.restart_process("Restarting...")

        self.label.setText("データの取得が完了しました!")


class System:
    def restart_process(self, message: str) -> None:
        sys.stderr.write(message)

        self._cleanup()

        os.execv(sys.executable, ["python"] + sys.argv)

    @staticmethod
    def exit_process(force: bool, code: int = 0) -> None:
        if force:
            os._exit(code)

        else:
            sys.exit(code)

    @staticmethod
    def _cleanup() -> None:
        process = psutil.Process(os.getpid())

        try:
            if len(process.connections()) == len(process.open_files()):
                for (c_handler, f_handler) in zip(process.connections(), process.open_files()):
                    os.close(c_handler.fd)
                    os.close(f_handler.fd)

            else:
                for c_handler in process.connections():
                    os.close(c_handler.fd)

                for f_handler in process.open_files():
                    os.close(f_handler.fd)

        except OSError:
            pass

        gc.collect()

        sys.stdout.flush()


app = QApplication(sys.argv).instance()
window = MainProcess()
window.show()
sys.exit(app.exec())
