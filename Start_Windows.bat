@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 bootstrap.py %*
) else (
    python bootstrap.py %*
)
if errorlevel 1 (
    echo.
    echo The application could not start. Read the message above.
    pause
)
endlocal
