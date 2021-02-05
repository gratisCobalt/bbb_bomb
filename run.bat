@echo off
copy /b/v/y config.json temp_config.json
start cmd /k python input_listener.py
start /min python bomb.py

REM use this for loop to start multiple bots
REM for /l %x in (1, 1, 5) do start /min python bomb.py