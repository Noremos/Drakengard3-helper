@echo off
REM Build script for creating dod3.exe on Windows

echo Installing dependencies...
pip install pygame pyinstaller

echo Navigating to main directory...
cd main

echo Building EXE with PyInstaller...
pyinstaller dod3.spec

echo Build complete!
echo EXE located at: %cd%\dist\dod3.exe
pause
