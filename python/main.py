# -*- coding: utf-8 -*-

import os
import sys

from python.internal.static import _exceptions

CD_PATH = os.getcwd()

print("プログラムを実行します...")

if sys.platform == "win32":
    os.system(rf"python -O {CD_PATH}\python\runtime.py")

else:
    raise _exceptions.PlatformError("Windows 以外のプラットフォームはサポートしていません")
