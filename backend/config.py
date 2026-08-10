"""
Global Project Configuration

Contains all project directories used by the backend.
"""

from pathlib import Path

# =====================================================
# Project Root
# =====================================================

PROJECT_DIR = Path(__file__).resolve().parent.parent

# =====================================================
# Dataset Directories
# =====================================================

DATASET_DIR = PROJECT_DIR / "datasets"

IMAGE_DIR = DATASET_DIR / "image"
VIDEO_DIR = DATASET_DIR / "video"
AUDIO_DIR = DATASET_DIR / "audio"
TEXT_DIR = DATASET_DIR / "text"

# =====================================================
# Weights Directories
# =====================================================

WEIGHTS_DIR = PROJECT_DIR / "backend" / "weights"

IMAGE_WEIGHTS_DIR = WEIGHTS_DIR / "image"
VIDEO_WEIGHTS_DIR = WEIGHTS_DIR / "video"
AUDIO_WEIGHTS_DIR = WEIGHTS_DIR / "audio"
TEXT_WEIGHTS_DIR = WEIGHTS_DIR / "text"

# =====================================================
# Reports
# =====================================================

REPORT_DIR = PROJECT_DIR / "reports"

IMAGE_REPORT_DIR = REPORT_DIR / "image"
VIDEO_REPORT_DIR = REPORT_DIR / "video"
AUDIO_REPORT_DIR = REPORT_DIR / "audio"
TEXT_REPORT_DIR = REPORT_DIR / "text"

# =====================================================
# Logs
# =====================================================

LOG_DIR = PROJECT_DIR / "backend" / "logs"

# =====================================================
# Cache
# =====================================================

CACHE_DIR = PROJECT_DIR / "cache"

HF_CACHE_DIR = CACHE_DIR / "huggingface"

# =====================================================
# Create Required Directories
# =====================================================

DIRECTORIES = [

    DATASET_DIR,

    IMAGE_DIR,
    VIDEO_DIR,
    AUDIO_DIR,
    TEXT_DIR,

    WEIGHTS_DIR,

    IMAGE_WEIGHTS_DIR,
    VIDEO_WEIGHTS_DIR,
    AUDIO_WEIGHTS_DIR,
    TEXT_WEIGHTS_DIR,

    REPORT_DIR,

    IMAGE_REPORT_DIR,
    VIDEO_REPORT_DIR,
    AUDIO_REPORT_DIR,
    TEXT_REPORT_DIR,

    LOG_DIR,

    CACHE_DIR,
    HF_CACHE_DIR,

]

for directory in DIRECTORIES:

    directory.mkdir(

        parents=True,

        exist_ok=True,

    )