# -*- coding: utf-8 -*-

import os
import time

CD_PATH = os.getcwd()

print("プログラムを実行します...")
os.system(rf"python -O {CD_PATH}\runtime.py")

time.sleep(0.3)
