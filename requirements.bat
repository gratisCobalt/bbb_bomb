@echo off
python logo.py
python get-pip.py
python -m pip install --upgrade pip
python -m pip install selenium
python -m pip install pygame
powershell -executionpolicy remotesigned -file get-VBCABLE.ps1
start "./VBCABLE_Driver_Pack43/VBCABLE_Setup.exe"
powershell -executionpolicy remotesigned -file addPATH.ps1
powershell -executionpolicy remotesigned -file get-Chromdriver.ps1
