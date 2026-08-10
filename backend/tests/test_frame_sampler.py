"""
Test Video Frame Sampler
"""

from pathlib import Path

from backend.ai.video.frame_sampler import (
    frame_sampler,
)


# ============================================
# Dataset Directory
# ============================================

VIDEO_DIR = Path(
    "datasets/video"
)


# ============================================
# Supported Video Extensions
# ============================================

VIDEO_EXTENSIONS = (

    "*.mp4",

    "*.mov",

    "*.MOV",

    "*.avi",

    "*.mkv",

    "*.webm",

)


# ============================================
# Find First Video
# ============================================

video_file = None

for extension in VIDEO_EXTENSIONS:

    videos = sorted(
        VIDEO_DIR.glob(extension)
    )

    if videos:

        video_file = videos[0]

        break


if video_file is None:

    raise FileNotFoundError(

        f"No video file found inside {VIDEO_DIR}"

    )


print(f"Video : {video_file.name}")


# ============================================
# Sample Frames
# ============================================

frames = frame_sampler.sample_frames(

    str(video_file)

)


# ============================================
# Results
# ============================================

print()

print(f"Frames Extracted : {len(frames)}")

print(f"Frame Type       : {type(frames[0])}")

print(f"Frame Shape      : {frames[0].shape}")