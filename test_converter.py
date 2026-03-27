#!/usr/bin/env python3
"""
Simple test script to verify RTF to PDF and MP4 to GIF conversion works
"""

import sys
import os
import tempfile
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rtf_to_pdf_converter import RTFToPDFConverter
from mp4_to_gif_converter import MP4ToGIFConverter

def test_rtf_conversion():
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


def _create_test_mp4(path, num_frames=30, width=64, height=64, fps=10):
    """Create a minimal synthetic MP4 file using imageio for testing."""
    import imageio
    writer = imageio.get_writer(path, format='ffmpeg', fps=fps)
    rng = np.random.default_rng(0)
    for _ in range(num_frames):
        frame = rng.integers(0, 256, (height, width, 3), dtype=np.uint8)
        writer.append_data(frame)
    writer.close()


def test_mp4_to_gif_basic():
    """Test basic MP4 to GIF conversion."""
    converter = MP4ToGIFConverter()
    temp_dir = tempfile.gettempdir()
    input_file = os.path.join(temp_dir, "test_input.mp4")
    output_file = os.path.join(temp_dir, "test_output.gif")

    # Clean up any leftover files
    for f in (input_file, output_file):
        if os.path.exists(f):
            os.remove(f)

    print(f"Creating synthetic MP4: {input_file}")
    _create_test_mp4(input_file)

    print(f"Testing MP4 → GIF conversion to {output_file}")
    try:
        converter.convert(input_file, output_file, fps=5)
        if os.path.exists(output_file):
            size = os.path.getsize(output_file)
            print(f"✓ Output GIF created: {output_file} ({size} bytes)")
            return True
        else:
            print("✗ Output GIF was not created")
            return False
    except Exception as e:
        print(f"✗ Conversion failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_mp4_to_gif_max_width():
    """Test MP4 to GIF conversion with max_width resizing."""
    converter = MP4ToGIFConverter()
    temp_dir = tempfile.gettempdir()
    input_file = os.path.join(temp_dir, "test_input_wide.mp4")
    output_file = os.path.join(temp_dir, "test_output_wide.gif")

    for f in (input_file, output_file):
        if os.path.exists(f):
            os.remove(f)

    _create_test_mp4(input_file, width=128, height=64)

    print(f"Testing MP4 → GIF with max_width=64")
    try:
        converter.convert(input_file, output_file, fps=5, max_width=64)
        if os.path.exists(output_file):
            from PIL import Image
            gif = Image.open(output_file)
            w, h = gif.size
            print(f"✓ GIF dimensions: {w}x{h}")
            assert w <= 64, f"Expected width ≤ 64, got {w}"
            return True
        else:
            print("✗ Output GIF was not created")
            return False
    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_mp4_to_gif_missing_file():
    """Test that a missing input file raises FileNotFoundError."""
    converter = MP4ToGIFConverter()
    try:
        converter.convert("/nonexistent/path/video.mp4", "/tmp/out.gif")
        print("✗ Expected FileNotFoundError but none was raised")
        return False
    except FileNotFoundError:
        print("✓ FileNotFoundError raised as expected for missing file")
        return True
    except Exception as e:
        print(f"✗ Unexpected exception: {e}")
        return False


def test_mp4_to_gif_invalid_extension():
    """Test that an unsupported file extension raises ValueError."""
    import tempfile
    converter = MP4ToGIFConverter()
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
        tmp = f.name
    try:
        converter.convert(tmp, "/tmp/out.gif")
        print("✗ Expected ValueError but none was raised")
        return False
    except ValueError:
        print("✓ ValueError raised as expected for unsupported format")
        return True
    except Exception as e:
        print(f"✗ Unexpected exception: {e}")
        return False
    finally:
        os.unlink(tmp)


if __name__ == "__main__":
    results = []

    print("=" * 60)
    print("RTF → PDF conversion test")
    print("=" * 60)
    results.append(test_rtf_conversion())

    print()
    print("=" * 60)
    print("MP4 → GIF conversion tests")
    print("=" * 60)
    results.append(test_mp4_to_gif_basic())
    results.append(test_mp4_to_gif_max_width())
    results.append(test_mp4_to_gif_missing_file())
    results.append(test_mp4_to_gif_invalid_extension())

    print()
    passed = sum(results)
    total = len(results)
    print(f"Tests passed: {passed}/{total}")
    sys.exit(0 if all(results) else 1)

