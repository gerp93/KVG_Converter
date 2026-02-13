# RTF to PDF Converter - User Guide

## Overview

The RTF to PDF Converter is a Windows desktop application that allows you to convert Rich Text Format (RTF) files to Portable Document Format (PDF) files while preserving the formatting of your documents.

## Installation Options

### Option 1: Standalone Executable (Recommended for most users)

1. Download `RTF_to_PDF_Converter.exe` from the releases page
2. Place it anywhere on your computer (e.g., Desktop, Documents folder)
3. Double-click the executable to launch the application
4. No installation or Python required!

### Option 2: Run from Python Source

1. Install Python 3.8 or later from [python.org](https://www.python.org/downloads/)
2. Download or clone this repository
3. Open Command Prompt or PowerShell
4. Navigate to the project directory
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the application:
   ```bash
   python rtf_to_pdf_converter.py
   ```

## Using the GUI Application

### Step 1: Launch the Application
- Double-click `RTF_to_PDF_Converter.exe` (if using the executable)
- OR run `python rtf_to_pdf_converter.py` (if running from source)

### Step 2: Select Input File
- Click the "Browse..." button next to "Input RTF File"
- Navigate to your RTF file in the file browser
- Select the file and click "Open"
- The file path will appear in the text box

### Step 3: Choose Output Location
- The application automatically suggests an output location (same folder as input, with .pdf extension)
- To change the location, click "Save As..." next to "Output PDF File"
- Choose your desired location and filename
- Click "Save"

### Step 4: Convert
- Click the green "Convert to PDF" button
- A progress bar will appear while converting
- Wait for the conversion to complete (usually just a few seconds)
- A success message will appear when done

### Step 5: View Your PDF
- Navigate to the output location
- Open the PDF file with your preferred PDF viewer (Adobe Reader, Edge, Chrome, etc.)
- Verify that the formatting looks correct

## Using the Command-Line Interface (CLI)

For advanced users or batch processing, use the CLI version:

### Basic Usage
```bash
python rtf_to_pdf_cli.py input.rtf
```
This converts `input.rtf` to `input.pdf` in the same directory.

### Specify Output File
```bash
python rtf_to_pdf_cli.py input.rtf output.pdf
```

### Full Path Example
```bash
python rtf_to_pdf_cli.py "C:\Documents\myfile.rtf" "C:\PDFs\myfile.pdf"
```

### Batch Processing with Windows Batch Script
Create a `.bat` file to process multiple files:
```batch
@echo off
for %%f in (*.rtf) do (
    echo Converting %%f...
    python rtf_to_pdf_cli.py "%%f"
)
echo All files converted!
pause
```

## Formatting Support

The converter preserves the following formatting:

✅ **Supported:**
- Plain text and paragraphs
- Bold, italic, and underlined text
- Different font sizes
- Basic paragraph spacing
- Headings and titles
- Line breaks and paragraph breaks
- Basic text alignment (left, center, right)

⚠️ **Limited Support:**
- Complex tables (may need manual adjustment)
- Images and graphics (converted as-is or may be skipped)
- Advanced formatting (may be simplified)
- Embedded objects

## Troubleshooting

### Problem: Application won't start
**Solutions:**
- If using .exe: Try running as Administrator
- If running from Python: Make sure Python 3.8+ is installed
- Check that all dependencies are installed: `pip install -r requirements.txt`

### Problem: Conversion fails with error
**Solutions:**
- Verify the input file is a valid RTF file (try opening it in WordPad)
- Check that you have write permissions to the output directory
- Try a different output location (e.g., your Desktop)
- Make sure the output filename doesn't contain invalid characters

### Problem: Formatting looks different in PDF
**Solutions:**
- Some advanced RTF features may not be fully supported
- Try simplifying the formatting in the original RTF file
- The converter works best with standard text formatting (bold, italic, headings)

### Problem: File is very large after conversion
**Solutions:**
- This is normal for complex documents
- PDFs are typically similar in size or slightly larger than RTF files
- You can use a PDF optimizer tool to reduce file size if needed

### Problem: Cannot find the output PDF
**Solutions:**
- Check the path shown in the success message
- Look in the same folder as your input RTF file
- Search Windows for the filename

## Building Your Own Executable

If you want to build the executable yourself:

### Windows
1. Install Python and dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
2. Run the build script:
   ```bash
   build_windows.bat
   ```
3. Find the executable in the `dist` folder

### Linux/Mac (Cross-compile for Windows)
1. Install Wine if needed
2. Install Python and dependencies
3. Run:
   ```bash
   bash build_windows.sh
   ```

## Tips and Best Practices

1. **Keep a backup**: Always keep your original RTF files
2. **Test first**: Try converting a test document before doing important files
3. **Check the output**: Always verify the PDF looks correct after conversion
4. **Use simple formatting**: The converter works best with standard RTF features
5. **Batch process**: Use the CLI for converting multiple files at once

## System Requirements

### For Running the Executable:
- Windows 7 or later
- 50 MB free disk space
- No additional software required

### For Running from Source:
- Python 3.8 or later
- pip (Python package manager)
- 100 MB free disk space (for Python and dependencies)

## Support and Feedback

If you encounter issues or have suggestions:
1. Check this user guide for solutions
2. Review the README.md for technical details
3. Check existing GitHub issues
4. Create a new issue with details about your problem

## License

This software is provided under the GNU Affero General Public License v3.0. See LICENSE file for details.

## Credits

Built with:
- Python - Programming language
- Tkinter - GUI framework
- ReportLab - PDF generation
- striprtf - RTF parsing
- PyInstaller - Executable creation

---

**Version:** 1.0.0  
**Last Updated:** February 2026  
**Author:** KVG Converter Team
