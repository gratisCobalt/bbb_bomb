@echo off
python get-pip.py
python -m pip install --upgrade pip
python -m pip install selenium
python -m pip install pygame
move chromedriver.exe %USERPROFILE%\AppData\Local\Microsoft\WindowsApps
"VBCABLE_Driver_Pack43/VBCABLE_Setup.exe"