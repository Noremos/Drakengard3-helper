#!/bin/bash
# Build script for creating dod3.exe on macOS/Linux

set -e

echo "Installing dependencies..."
pip install pygame pyinstaller

echo "Navigating to main directory..."
cd main

echo "Building EXE with PyInstaller..."
pyinstaller dod3.spec

echo "Build complete!"
echo "EXE located at: $(pwd)/dist/dod3.exe"
