"""
MP4 to GIF Converter
Converts MP4 video files to animated GIF format with configurable options.
"""

import os
from pathlib import Path
import imageio.v3 as iio
import imageio
from PIL import Image
import numpy as np


class MP4ToGIFConverter:
    """Handles conversion of MP4 video files to animated GIF format."""

    DEFAULT_FPS = 10
    DEFAULT_SCALE = 1.0
    DEFAULT_MAX_WIDTH = 640

    def convert(self, mp4_path, gif_path, fps=None, scale=None, max_width=None,
                start_time=None, end_time=None):
        """
        Convert an MP4 file to an animated GIF.

        Args:
            mp4_path (str): Path to the input MP4 file.
            gif_path (str): Path to the output GIF file.
            fps (int|float|None): Frames per second for the output GIF.
                                  Defaults to DEFAULT_FPS.
            scale (float|None): Scale factor (0.0–1.0) to resize frames.
                                 Ignored when max_width is set.
            max_width (int|None): Maximum width in pixels; maintains aspect ratio.
                                  Overrides scale when provided.
            start_time (float|None): Start time in seconds to begin reading.
            end_time (float|None): End time in seconds to stop reading.

        Raises:
            FileNotFoundError: If the input file does not exist.
            ValueError: If the input file is not an MP4 or parameters are invalid.
            Exception: If conversion fails.
        """
        if not os.path.exists(mp4_path):
            raise FileNotFoundError(f"Input file not found: {mp4_path}")

        ext = Path(mp4_path).suffix.lower()
        if ext not in ('.mp4', '.m4v', '.mov', '.avi', '.mkv'):
            raise ValueError(
                f"Unsupported input format '{ext}'. Expected a video file (.mp4, .mov, .avi, .mkv)."
            )

        fps = fps if fps is not None else self.DEFAULT_FPS
        if fps <= 0:
            raise ValueError("fps must be a positive number.")

        frames = self._read_frames(mp4_path, fps, start_time, end_time)
        frames = self._resize_frames(frames, scale, max_width)
        self._write_gif(frames, gif_path, fps)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _read_frames(self, mp4_path, target_fps, start_time, end_time):
        """Read frames from the video, sampling at *target_fps*."""
        reader = imageio.get_reader(mp4_path, format='ffmpeg')
        meta = reader.get_meta_data()
        source_fps = meta.get('fps', 25)
        # How many source frames to skip between each captured frame
        frame_step = max(1, round(source_fps / target_fps))

        frames = []
        for idx, frame in enumerate(reader):
            t = idx / source_fps
            if start_time is not None and t < start_time:
                continue
            if end_time is not None and t > end_time:
                break
            adjusted_idx = idx if start_time is None else idx - round(start_time * source_fps)
            if adjusted_idx % frame_step == 0:
                frames.append(np.array(frame))

        reader.close()
        return frames

    def _resize_frames(self, frames, scale, max_width):
        """Resize a list of numpy frames according to *scale* or *max_width*."""
        if not frames:
            return frames

        h, w = frames[0].shape[:2]

        if max_width is not None and max_width > 0:
            if w > max_width:
                scale_factor = max_width / w
                new_w = max_width
                new_h = max(1, int(h * scale_factor))
            else:
                return frames
        elif scale is not None and scale != 1.0:
            if scale <= 0:
                raise ValueError("scale must be a positive number.")
            new_w = max(1, int(w * scale))
            new_h = max(1, int(h * scale))
        else:
            return frames

        resized = []
        for frame in frames:
            img = Image.fromarray(frame)
            img = img.resize((new_w, new_h), Image.LANCZOS)
            resized.append(np.array(img))
        return resized

    def _write_gif(self, frames, gif_path, fps):
        """Write *frames* to *gif_path* as an animated GIF."""
        if not frames:
            raise ValueError("No frames were extracted from the video.")
        duration = 1.0 / fps  # seconds per frame (imageio uses seconds)
        pil_frames = [Image.fromarray(frame) for frame in frames]
        # Quantize each frame to reduce GIF palette to 256 colours
        pil_frames = [f.convert('P', palette=Image.ADAPTIVE, colors=256) for f in pil_frames]
        pil_frames[0].save(
            gif_path,
            save_all=True,
            append_images=pil_frames[1:],
            optimize=False,
            duration=int(duration * 1000),  # Pillow uses milliseconds
            loop=0,
        )
