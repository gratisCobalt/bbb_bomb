@echo off
copy /b/v/y config.json temp_config.json
start cmd /k python input_listener.py
start /min python bomb.py