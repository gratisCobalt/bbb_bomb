@echo off
copy /b/v/y config.json temp_config.json
start cmd /k python input_listener.py
python bomb.py