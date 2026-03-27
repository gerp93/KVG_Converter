# KVG_Converter
RTF to PDF Converter - Windows Desktop Application

A simple and user-friendly Windows desktop application that converts RTF (Rich Text Format) files to PDF format while preserving formatting.

## Features

- ✅ Easy-to-use graphical user interface
- ✅ Convert RTF files to PDF with formatting preservation
- ✅ Support for text formatting (bold, italic, headings, etc.)
- ✅ Batch processing ready
- ✅ Progress indication during conversion
- ✅ Error handling and user feedback

## Installation

### Option 1: Run from Source (Requires Python)

1. Make sure you have Python 3.8 or later installed
2. Clone this repository or download the source code
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python rtf_to_pdf_converter.py
   ```

### Option 2: Build Windows Executable

To create a standalone Windows executable that doesn't require Python:

1. Install Python 3.8 or later
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
3. Run the build script:
   - On Windows: Double-click `build_windows.bat` or run it from command prompt
   - On Linux/Mac: `bash build_windows.sh`
4. The executable will be created in the `dist` folder
5. You can distribute `RTF_to_PDF_Converter.exe` to other Windows computers

## Usage

1. Launch the application (either by running the Python script or the .exe file)
2. Click "Browse..." to select your RTF file
3. The output PDF location will be automatically suggested (you can change it using "Save As...")
4. Click "Convert to PDF" to start the conversion
5. Wait for the conversion to complete
6. Your PDF file will be saved to the specified location

## Requirements

### For Running from Source:
- Python 3.8 or later
- tkinter (usually included with Python)
- Required Python packages (see requirements.txt):
  - pypandoc==1.13
  - reportlab==4.1.0
  - striprtf==0.0.26
  - Pillow==10.2.0

### For Building Executable:
- All of the above, plus:
  - pyinstaller==6.3.0 (see requirements-dev.txt)

### For Running the Executable:
- Windows 7 or later
- No additional software required!

## Supported Formats

- **Input**: RTF (Rich Text Format) files (.rtf)
- **Output**: PDF (Portable Document Format) files (.pdf)

## Technical Details

The application uses:
- **tkinter**: For the graphical user interface
- **striprtf**: For parsing RTF files and extracting formatted content
- **reportlab**: For generating PDF files with proper formatting
- **PyInstaller**: For creating standalone Windows executables

## Troubleshooting

### "The application won't start"
- Make sure you have Python 3.8+ installed if running from source
- Check that all dependencies are installed: `pip install -r requirements.txt`

### "Conversion failed"
- Ensure the input file is a valid RTF file
- Check that you have write permissions to the output directory
- Try using a different output location

### "Text formatting is not preserved"
- The converter preserves basic formatting like paragraphs and headings
- Some advanced RTF features may not be fully supported
- Complex tables and images may require manual adjustment

## Development

To contribute or modify the code:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Author

KVG Converter Team

## Acknowledgments

- Built with Python and open-source libraries
- Uses reportlab for PDF generation
- Uses striprtf for RTF parsing
