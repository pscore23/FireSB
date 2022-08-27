@echo off
cd /d %~dp0

python.exe -m pip install --upgrade pip
python.exe -m pip install -r requirements.txt
