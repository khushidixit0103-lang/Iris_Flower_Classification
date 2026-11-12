@echo off
TITLE Iris Prediction API Server
echo ===================================================
echo   Starting Iris Flower Classification Python API
echo ===================================================
cd /d "%~dp0"
if exist "venv\Scripts\python.exe" (
    "venv\Scripts\python.exe" api\app.py
) else (
    python api\app.py
)
pause
