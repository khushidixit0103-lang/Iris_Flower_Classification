@echo off
echo ============================================================
echo   Pushing Iris Flower Classification to GitHub
echo ============================================================
set "PATH=C:\Users\Khushi\AppData\Local\Programs\git\cmd;C:\Users\Khushi\AppData\Local\Programs\gh\bin;%PATH%"
cd /d "%~dp0"
echo Target Remote: https://github.com/khushidixit0103-lang/Iris_Flower_Classification.git
echo.
git push -u origin main
echo.
if %ERRORLEVEL% EQU 0 (
    echo ============================================================
    echo   SUCCESSFULLY PUSHED TO GITHUB!
    echo ============================================================
) else (
    echo ============================================================
    echo   PUSH FAILED OR NEEDS AUTHENTICATION.
    echo   If prompted, sign in via your browser or run:
    echo   C:\Users\Khushi\AppData\Local\Programs\gh\bin\gh.exe auth login
    echo ============================================================
)
pause
