@echo off
cls
echo $ - Installing Python and necessary modules for the Auto Button Presser Bot...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo $ - Python is not installed. Installing Python...
    echo.
    :: Download and install Python (modify the URL to the latest version)
    powershell -command "& { iwr -outf python-installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe; Start-Process python-installer.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait; Remove-Item python-installer.exe -Force }"
) else (
    echo $ - Python is already installed.
    echo.
)

echo $ - Installing required Python modules...
echo.

:: Install necessary Python modules
python -m pip install --upgrade pip
python -m pip install pywinauto

echo.
echo.
echo.
echo $ - All requirements have been installed successfully!
echo.
pause
