@echo off
TITLE Iris Classification Project Launcher
echo =============================================================
echo   Starting Complete Iris Flower Classification System
echo   1. Python Flask Prediction API (Port 5000)
echo   2. n8n Workflow Automation Platform (Port 5678)
echo =============================================================
cd /d "%~dp0"

echo Launching Python Prediction API in separate window...
start "Python Iris API" start_api.bat

timeout /t 3 /nobreak >nul

echo Launching n8n Workflow Platform in separate window...
start "n8n Server" start_n8n.bat

echo.
echo =============================================================
echo   Services are starting up:
echo   - Python API: http://127.0.0.1:5000
echo   - n8n Platform: http://localhost:5678
echo =============================================================
timeout /t 5 /nobreak >nul
