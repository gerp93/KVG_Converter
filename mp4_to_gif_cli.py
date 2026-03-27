#!/usr/bin/env python3
"""
Command-line interface for MP4 to GIF converter.

Usage:
    python mp4_to_gif_cli.py input.mp4 [output.gif] [options]

Options:
    --fps FPS           Frames per second for output GIF (default: 10)
    --scale SCALE       Scale factor, e.g. 0.5 for half size (default: 1.0)
    --max-width WIDTH   Maximum output width in pixels (overrides --scale)
    --start START       Start time in seconds
    --end END           End time in seconds
"""

import sys
import os
import argparse
from pathlib import Path
from mp4_to_gif_converter import MP4ToGIFConverter


def build_parser():
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__),
        description="Convert an MP4 video file to an animated GIF.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            f"  python {os.path.basename(__file__)} video.mp4\n"
            f"  python {os.path.basename(__file__)} video.mp4 output.gif --fps 15\n"
            f"  python {os.path.basename(__file__)} video.mp4 --max-width 480 --start 2 --end 8\n"
            f"  python {os.path.basename(__file__)} video.mp4 --scale 0.5 --fps 12\n"
        ),
    )
    parser.add_argument("input", metavar="input.mp4", help="Path to input MP4 file (required)")
    parser.add_argument(
        "output",
        metavar="output.gif",
        nargs="?",
        help="Path to output GIF file (optional, defaults to input filename with .gif extension)",
    )
    parser.add_argument(
        "--fps",
        type=float,
        default=10,
        metavar="FPS",
        help="Frames per second for the output GIF (default: 10)",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=None,
        metavar="SCALE",
        help="Scale factor for resizing frames, e.g. 0.5 (default: no scaling)",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=None,
        metavar="WIDTH",
        dest="max_width",
        help="Maximum width in pixels; maintains aspect ratio (overrides --scale)",
    )
    parser.add_argument(
        "--start",
        type=float,
        default=None,
        metavar="SECONDS",
        help="Start time in seconds (default: beginning of video)",
    )
    parser.add_argument(
        "--end",
        type=float,
        default=None,
        metavar="SECONDS",
        help="End time in seconds (default: end of video)",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    input_file = args.input

    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}", file=sys.stderr)
        sys.exit(1)

    output_file = args.output or str(Path(input_file).with_suffix('.gif'))

    print("Converting MP4 to GIF...")
    print(f"  Input:     {input_file}")
    print(f"  Output:    {output_file}")
    print(f"  FPS:       {args.fps}")
    if args.max_width:
        print(f"  Max width: {args.max_width}px")
    elif args.scale:
        print(f"  Scale:     {args.scale}")
    if args.start is not None:
        print(f"  Start:     {args.start}s")
    if args.end is not None:
        print(f"  End:       {args.end}s")
    print()

    try:
        converter = MP4ToGIFConverter()
        converter.convert(
            input_file,
            output_file,
            fps=args.fps,
            scale=args.scale,
            max_width=args.max_width,
            start_time=args.start,
            end_time=args.end,
        )

        print("✓ Conversion successful!")
        print(f"✓ GIF saved to: {output_file}")

        file_size = os.path.getsize(output_file)
        print(f"✓ File size: {file_size} bytes ({file_size / 1024:.2f} KB)")

    except Exception as e:
        print(f"✗ Conversion failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
