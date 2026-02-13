# Frequently Asked Questions (FAQ)

## General Questions

### Q: What is RTF?
**A:** RTF (Rich Text Format) is a document file format developed by Microsoft. It allows formatting like bold, italic, fonts, and colors while remaining readable across different platforms.

### Q: Why would I want to convert RTF to PDF?
**A:** PDF files are more universally compatible, maintain formatting better across devices, are harder to accidentally modify, and are better for sharing and archiving documents.

### Q: Is this free to use?
**A:** Yes! This software is open source and free to use under the GNU AGPL v3.0 license.

### Q: Does it work on Mac or Linux?
**A:** The current version is designed for Windows. However, if you have Python installed, you can run the Python scripts on any platform. The GUI requires display support.

## Installation & Setup

### Q: Do I need to install Python?
**A:** Not if you use the standalone .exe file. If you run from source, you'll need Python 3.8 or later.

### Q: What if I get a "Windows protected your PC" warning?
**A:** This is normal for unsigned executables. Click "More info" then "Run anyway". This warning appears because the executable hasn't been digitally signed.

### Q: How much disk space do I need?
**A:** About 50 MB for the executable, or 100 MB if installing Python and dependencies.

## Usage

### Q: Can I convert multiple files at once?
**A:** Yes! Use the `batch_convert.bat` script or create your own batch script using the CLI interface.

### Q: How long does conversion take?
**A:** Most files convert in under 5 seconds. Very large files (100+ pages) may take longer.

### Q: What's the maximum file size I can convert?
**A:** There's no hard limit, but very large files (>10 MB) may take longer and use more memory.

### Q: Can I use this in my business?
**A:** Yes, but note the GNU AGPL v3.0 license requirements. If you modify the software, you must share your changes.

## Formatting & Features

### Q: Will all my formatting be preserved?
**A:** Most basic formatting (bold, italic, font sizes, paragraphs) is preserved. Complex features like tables, embedded images, or advanced layouts may need adjustment.

### Q: My document has images. Will they be converted?
**A:** Basic image support is included, but complex embedded images may not convert perfectly. Test with your specific files.

### Q: Can I adjust PDF settings like page size or margins?
**A:** The current version uses standard settings (Letter size, 1-inch margins). You can modify the source code to change these if needed.

### Q: Does it support right-to-left languages?
**A:** Basic text is supported, but complex RTL formatting may not be preserved perfectly.

## Troubleshooting

### Q: The conversion fails with "No module named 'tkinter'"
**A:** This means tkinter isn't installed. If using the .exe, this shouldn't happen. If running from Python, install tkinter: `sudo apt-get install python3-tk` (Linux) or reinstall Python with tkinter enabled (Windows).

### Q: I get "Permission denied" errors
**A:** Make sure you have write permissions to the output directory. Try saving to your Desktop or Documents folder.

### Q: The PDF looks corrupted or won't open
**A:** This might mean the input RTF file was corrupted or in an unsupported format. Try opening the RTF in WordPad or Word first to verify it's valid.

### Q: Some text is missing in the PDF
**A:** This could be due to unsupported RTF features. Try simplifying the formatting in the original document.

### Q: The application freezes or crashes
**A:** This might happen with very large or complex files. Try converting a smaller portion of the document first. If the issue persists, please report it as a bug.

## Technical Questions

### Q: What Python version is required?
**A:** Python 3.8 or later is recommended. The application may work on Python 3.7 but this is not officially supported.

### Q: Can I modify the source code?
**A:** Yes! The code is open source under GNU AGPL v3.0. You're free to modify it, but must share your changes if you distribute the modified version.

### Q: What libraries does it use?
**A:** Main libraries are: tkinter (GUI), reportlab (PDF generation), striprtf (RTF parsing), and Pillow (image handling).

### Q: Can I integrate this into my own application?
**A:** Yes! You can import and use the RTFToPDFConverter class in your own Python projects. Just respect the license terms.

### Q: How do I build my own executable?
**A:** See the USER_GUIDE.md "Building Your Own Executable" section or run `build_windows.bat`.

## Performance

### Q: Why is the conversion slow?
**A:** Large files with complex formatting take longer. The conversion speed depends on file size, complexity, and your computer's performance.

### Q: Can I speed up batch conversions?
**A:** The CLI version is already optimized. For even faster processing, you could modify the code to use multiprocessing for parallel conversions.

### Q: Does it use a lot of memory?
**A:** Memory usage is proportional to file size. Most documents use less than 100 MB of RAM during conversion.

## Security & Privacy

### Q: Is my data sent anywhere?
**A:** No! All conversion happens locally on your computer. No data is sent to any servers or the internet.

### Q: Can I use this for confidential documents?
**A:** Yes, since everything is processed locally and nothing is uploaded or shared.

### Q: Does it log my files or activities?
**A:** No, the application doesn't create logs or track what files you convert.

## Support

### Q: Where can I get help?
**A:** Check this FAQ, the USER_GUIDE.md, and the README.md. For bugs or feature requests, open an issue on GitHub.

### Q: Can I request new features?
**A:** Yes! Open a feature request issue on GitHub. Popular requests may be implemented in future versions.

### Q: How do I report bugs?
**A:** Open an issue on GitHub with:
- Description of the problem
- Steps to reproduce
- Your Windows version
- Error messages (if any)

### Q: Is there a newer version?
**A:** Check the GitHub repository for the latest release and changelog.

## Contributing

### Q: Can I contribute to the project?
**A:** Yes! Contributions are welcome. Fork the repository, make your changes, and submit a pull request.

### Q: What kind of contributions are needed?
**A:** Code improvements, bug fixes, documentation, translations, testing, and feature development are all valuable.

### Q: How do I set up a development environment?
**A:** Clone the repo, install dependencies with `pip install -r requirements.txt`, and start coding. See README.md for details.

---

**Still have questions?** Open an issue on GitHub or check the documentation.
