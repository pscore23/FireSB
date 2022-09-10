# -*- coding: utf-8 -*-

import os
import time

CD_PATH = os.getcwd()

print("アップデートの確認をしています...")

os.system(rf"{CD_PATH}\launch\starter.bat")
os.system(rf"python -O {CD_PATH}\python\runtime.py")

time.sleep(0.3)
