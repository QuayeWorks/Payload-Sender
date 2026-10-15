@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 bootstrap.py --build
) else (
    python bootstrap.py --build
)
if errorlevel 1 (
    echo.
    echo Build failed. Read the message above.
) else (
    echo.
    echo The executable is in dist\QuayeWorks-PS4-Payload-Sender\.
    echo Keep the whole folder together when moving the app.
)
pause
endlocal
