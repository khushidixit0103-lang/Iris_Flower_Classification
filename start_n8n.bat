@echo off
TITLE n8n Workflow Automation Server
echo ===================================================
echo   Starting n8n Workflow Automation Engine
echo ===================================================
set "PATH=C:\Users\Khushi\AppData\Local\Programs\nodejs;C:\Users\Khushi\AppData\Local\Programs\git\cmd;C:\Users\Khushi\AppData\Roaming\npm;%PATH%"

echo Checking Node.js environment...
node --version
echo Starting n8n on http://localhost:5678 ...
echo (Press Ctrl+C to stop)
npx -y n8n
pause
