@echo off
REM Local Preview (Windows)
REM Usage: double-click or run: start_server.bat [port]
SETLOCAL
WHERE python >NUL 2>&1
IF ERRORLEVEL 1 (
  ECHO Python not found. Please install Python 3 and try again.
  PAUSE
  EXIT /B 1
)
python start_server.py %*
ECHO.
ECHO Press Ctrl+C in this window to stop the server.
PAUSE