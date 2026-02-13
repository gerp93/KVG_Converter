#!/bin/bash
# Build script for creating Windows executable (can be run on Linux/Mac with Wine)

echo "Installing dependencies..."
pip install -r requirements.txt
pip install -r requirements-dev.txt

echo ""
echo "Building Windows executable..."
pyinstaller --name="RTF_to_PDF_Converter" \
    --onefile \
    --windowed \
    --icon=NONE \
    --add-data="LICENSE:." \
    rtf_to_pdf_converter.py

echo ""
echo "Build complete! Executable can be found in the 'dist' folder."
