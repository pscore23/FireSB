import json
import zipfile

import _exceptions as _except


class SB3:
    @staticmethod
    def open(file_name):
        need = "project.json"

        try:
            with zipfile.ZipFile(file_name) as zf:
                names = zf.namelist()

                if need not in names:
                    raise _except.JSONNotFoundError("'.sb3' file must contain 'project.json' file")

                json_file = json.dumps(json.loads(
                    zf.read(need).decode("utf-8")
                ), ensure_ascii=False, indent=4, sort_keys=False, separators=(',', ': '))
                actual_names = (item for item in names if (
                    item.count(".") == 1 and
                    len(item.split(".")[0]) == 32 and
                    item.split(".")[0].isalnum()
                ))
                files = tuple(zf.open(name) for name in actual_names)

            return json_file, files

        except zipfile.BadZipFile:
            raise _except.NotSB3Error("File with extension '.sb3' is not specified.")
