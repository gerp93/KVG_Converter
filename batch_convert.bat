@echo off
REM Batch convert all RTF files in a directory to PDF
REM Usage: Place this file in the folder with your RTF files and double-click it

echo ================================================
echo RTF to PDF Batch Converter
echo ================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or later from python.org
    echo.
    pause
    exit /b 1
)

echo Found Python. Checking for converter script...
echo.

REM Check if converter script exists
if not exist rtf_to_pdf_cli.py (
    echo ERROR: rtf_to_pdf_cli.py not found in current directory
    echo Please copy rtf_to_pdf_cli.py and rtf_to_pdf_converter.py to this folder
    echo.
    pause
    exit /b 1
)

REM Count RTF files
set count=0
for %%f in (*.rtf) do set /a count+=1

if %count%==0 (
    echo No RTF files found in current directory.
    echo.
    pause
    exit /b 0
)

echo Found %count% RTF file(s). Starting conversion...
echo.

REM Convert each RTF file
set converted=0
set failed=0

for %%f in (*.rtf) do (
    echo Converting: %%f
    python rtf_to_pdf_cli.py "%%f" "%%~nf.pdf" >nul 2>&1
    if errorlevel 1 (
        echo   [FAILED] %%f
        set /a failed+=1
    ) else (
        echo   [SUCCESS] %%~nf.pdf
        set /a converted+=1
    )
)

echo.
echo ================================================
echo Conversion Complete
echo ================================================
echo Successfully converted: %converted% file(s)
if %failed% gtr 0 (
    echo Failed: %failed% file(s)
)
echo.
pause
