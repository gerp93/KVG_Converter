# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2026-02-13

### Security
- **CRITICAL**: Updated Pillow from 10.3.0 to 12.1.1 to fix out-of-bounds write vulnerability when loading PSD images
  - Affected versions: >= 10.3.0, < 12.1.1
  - Fixed in: 12.1.1
  - All users should update immediately

### Changed
- Updated Pillow dependency to 12.1.1 (security patch)

## [1.0.1] - 2026-02-13

### Security
- **CRITICAL**: Updated Pillow from 10.2.0 to 10.3.0 to fix buffer overflow vulnerability (CVE)
  - Affected versions: < 10.3.0
  - Fixed in: 10.3.0
  - All users should update immediately

### Changed
- Updated Pillow dependency to 10.3.0 (security patch)

## [1.0.0] - 2026-02-13

### Added
- Initial release of RTF to PDF Converter
- Windows desktop GUI application with tkinter
- Command-line interface for batch processing
- RTF file parsing with striprtf library
- PDF generation with reportlab library
- Custom paragraph styles for better formatting
- Threading support for responsive GUI
- Progress bar and status updates
- Automatic output path suggestion
- Comprehensive error handling
- Build scripts for Windows executable (PyInstaller)
- Setup.py for Python package distribution
- Test script for conversion verification
- Comprehensive documentation:
  - README.md with quick start guide
  - USER_GUIDE.md with detailed instructions
  - FAQ.md with common questions and troubleshooting
- Batch conversion script (batch_convert.bat)
- Cross-platform temp directory support
- Security scanning with CodeQL

### Features
- Convert RTF files to PDF format
- Preserve text formatting (bold, italic, font sizes)
- Maintain paragraph structure and spacing
- Support for headings and titles
- User-friendly GUI interface
- Command-line interface for automation
- Progress indication during conversion
- Error messages with helpful feedback

### Supported Platforms
- Windows 7 or later (GUI and CLI)
- Any platform with Python 3.8+ (CLI only)

### Dependencies
- reportlab 4.1.0 - PDF generation
- striprtf 0.0.26 - RTF parsing
- Pillow 10.2.0 - Image handling
- tkinter (built-in) - GUI framework

### Development Dependencies
- pyinstaller 6.3.0 - Executable creation

### Security
- All dependencies scanned for vulnerabilities
- No security issues found
- CodeQL security scanning passed
- Local processing only (no data sent to servers)

## [Unreleased]

### Planned Features
- Enhanced formatting support (tables, images)
- Multiple page size options
- Custom margin settings
- Drag and drop file support
- Recent files list
- Settings/preferences dialog
- MacOS and Linux GUI support
- Multi-language support
- Dark mode theme

---

For more details, see the [README](README.md) and [USER_GUIDE](USER_GUIDE.md).
