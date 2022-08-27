import os
import time

CD_PATH = os.getcwd()

print("セットアップしています...")
os.system(rf"{CD_PATH}\setup.bat")
print("セットアップが完了しました!")

time.sleep(0.3)

print("プログラムを実行します...")
os.system(rf"python -O {CD_PATH}\runtime.py")
