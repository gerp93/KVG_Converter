#!/usr/bin/env python3
"""
Simple test script to verify RTF to PDF conversion works
"""

import sys
import os
import tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rtf_to_pdf_converter import RTFToPDFConverter

def test_conversion():
    """Test the RTF to PDF conversion."""
    converter = RTFToPDFConverter()
    
    # Use platform-independent temp directory
    temp_dir = tempfile.gettempdir()
    input_file = os.path.join(temp_dir, "sample_test.rtf")
    output_file = os.path.join(temp_dir, "sample_test_output.pdf")
    
    print(f"Testing conversion of {input_file} to {output_file}")
    
    try:
        converter.convert(input_file, output_file)
        print("✓ Conversion successful!")
        
        # Check if output file was created
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"✓ Output PDF created: {output_file}")
            print(f"✓ File size: {file_size} bytes")
            return True
        else:
            print("✗ Output PDF file was not created")
            return False
            
    except Exception as e:
        print(f"✗ Conversion failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_conversion()
    sys.exit(0 if success else 1)
