#!/usr/bin/env python3
"""
Command-line interface for RTF to PDF converter
Usage: python rtf_to_pdf_cli.py input.rtf output.pdf
"""

import sys
import os
from pathlib import Path
from rtf_to_pdf_converter import RTFToPDFConverter


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("RTF to PDF Converter - Command Line Interface")
        print("")
        print("Usage:")
        print(f"  python {os.path.basename(__file__)} <input.rtf> [output.pdf]")
        print("")
        print("Arguments:")
        print("  input.rtf   - Path to input RTF file (required)")
        print("  output.pdf  - Path to output PDF file (optional, defaults to input filename with .pdf extension)")
        print("")
        print("Examples:")
        print(f"  python {os.path.basename(__file__)} document.rtf")
        print(f"  python {os.path.basename(__file__)} document.rtf output.pdf")
        print(f"  python {os.path.basename(__file__)} C:\\Users\\Documents\\file.rtf")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)
    
    # Determine output file
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        output_file = str(Path(input_file).with_suffix('.pdf'))
    
    print(f"Converting RTF to PDF...")
    print(f"  Input:  {input_file}")
    print(f"  Output: {output_file}")
    print("")
    
    try:
        converter = RTFToPDFConverter()
        converter.convert(input_file, output_file)
        print("✓ Conversion successful!")
        print(f"✓ PDF saved to: {output_file}")
        
        # Show file size
        file_size = os.path.getsize(output_file)
        print(f"✓ File size: {file_size} bytes ({file_size / 1024:.2f} KB)")
        
    except Exception as e:
        print(f"✗ Conversion failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
