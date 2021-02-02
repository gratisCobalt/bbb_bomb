@echo off
python get-pip.py
python -m pip install --upgrade pip
python -m pip install selenium
:loop
python bomb.py
GOTO loop