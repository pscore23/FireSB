import pathlib
import shutil
import sys

from PyQt6 import QtWidgets


class FileManager(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("SB3 Analyzer")
		self.resize(500, 500)

		self.show()

	def open_file(self):
		open_name = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "", "Custom Files (*.sb3)")[0]

		if not open_name:
			return None

		return open_name

	def change_suffix(self, file_name, from_suffix, to_suffix):
		suffix = pathlib.PurePath(file_name).suffix

		if suffix == from_suffix:
			stem = pathlib.PurePath(file_name).stem
			to_name = stem + to_suffix

			shutil.move(file_name, to_name)


app = QtWidgets.QApplication(sys.argv)
main = FileManager()
print(main.open_file())
sys.exit(app.exec())
