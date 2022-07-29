import zipfile


class JSONNotFoundError(FileNotFoundError):
    pass


class NotSB3Error(zipfile.BadZipfile):
    pass
