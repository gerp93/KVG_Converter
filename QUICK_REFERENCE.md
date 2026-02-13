# Quick Reference Card

## RTF to PDF Converter

### GUI Mode (Recommended)
```
1. Double-click RTF_to_PDF_Converter.exe
2. Click "Browse..." to select RTF file
3. Click "Convert to PDF"
4. Done!
```

### CLI Mode (For Scripts)
```bash
# Basic usage
python rtf_to_pdf_cli.py input.rtf

# Specify output
python rtf_to_pdf_cli.py input.rtf output.pdf

# Full paths
python rtf_to_pdf_cli.py "C:\Docs\file.rtf" "C:\PDFs\file.pdf"
```

### Batch Convert (Multiple Files)
```bash
# Place batch_convert.bat in folder with RTF files
# Double-click batch_convert.bat
# All RTF files will be converted to PDF
```

### Installation
**Executable**: Just download and run - no installation needed!

**From Source**:
```bash
pip install -r requirements.txt
python rtf_to_pdf_converter.py
```

### Build Your Own Executable
```bash
# Windows
build_windows.bat

# Linux/Mac
bash build_windows.sh
```

### Key Features
- ✅ Simple user interface
- ✅ Preserves text formatting
- ✅ Progress indication
- ✅ Error handling
- ✅ No internet required
- ✅ Fast conversion

### Supported Formatting
- Bold, italic, underline
- Font sizes
- Headings
- Paragraphs
- Line breaks
- Text alignment

### System Requirements
- Windows 7+ (for .exe)
- Python 3.8+ (for source)
- 50-100 MB disk space

### Quick Troubleshooting
**Won't start?** → Run as Administrator  
**Permission error?** → Save to Desktop  
**Conversion fails?** → Verify RTF is valid  
**Missing output?** → Check suggested path  

### Get Help
- Check FAQ.md
- Read USER_GUIDE.md
- Open GitHub issue

### Files Overview
```
rtf_to_pdf_converter.py  - Main GUI app
rtf_to_pdf_cli.py        - CLI version
batch_convert.bat        - Batch script
test_converter.py        - Test script
build_windows.bat        - Build .exe
README.md               - Overview
USER_GUIDE.md           - Detailed guide
FAQ.md                  - Q&A
```

### Development
```bash
# Install deps
pip install -r requirements.txt

# Run tests
python test_converter.py

# Build
build_windows.bat
```

---

**Version:** 1.0.0  
**License:** GNU AGPL v3.0  
**Repository:** github.com/gerp93/KVG_Converter
