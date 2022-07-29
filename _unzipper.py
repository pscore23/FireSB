import json
import zipfile

import _exceptions as _except


class SB3:
	@classmethod
	def open(cls, file_name):
		need = "project.json"

		with zipfile.ZipFile(file_name) as zf:
			names = zf.namelist()

			if need not in names:
				raise _except.JSONNotFoundError("'.sb3' file must contain 'project.json' file")

			json_file = json.dumps(json.loads(
				zf.read(need).decode("utf-8")), ensure_ascii=False, indent=4, sort_keys=False, separators=(',', ': '))

		return json_file


def main():
	print(SB3.open(r"C:\Users\soneh\Downloads\【CPU Benchmark】 QuaBench Z30 ver. 2.2.7.sb3"))
