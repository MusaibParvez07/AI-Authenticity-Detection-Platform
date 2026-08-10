"""
Global AI Configuration

Shared configuration for the AI Digital Forensics Platform.
"""

from pathlib import Path


# =====================================================
# Project Directories
# =====================================================

AI_DIR = Path(__file__).resolve().parent

BACKEND_DIR = AI_DIR.parent

PROJECT_DIR = BACKEND_DIR.parent


# =====================================================
# Weights
# =====================================================

WEIGHTS_DIR = BACKEND_DIR / "weights"

IMAGE_WEIGHTS_DIR = WEIGHTS_DIR / "image"
VIDEO_WEIGHTS_DIR = WEIGHTS_DIR / "video"
AUDIO_WEIGHTS_DIR = WEIGHTS_DIR / "audio"
TEXT_WEIGHTS_DIR = WEIGHTS_DIR / "text"


# =====================================================
# Upload / Dataset Directories
# =====================================================

DATASET_DIR = BACKEND_DIR / "datasets"

IMAGE_DATASET_DIR = DATASET_DIR / "image"
VIDEO_DATASET_DIR = DATASET_DIR / "video"
AUDIO_DATASET_DIR = DATASET_DIR / "audio"
TEXT_DATASET_DIR = DATASET_DIR / "text"


# =====================================================
# Reports
# =====================================================

REPORT_DIR = BACKEND_DIR / "reports"

IMAGE_REPORT_DIR = REPORT_DIR / "image"
VIDEO_REPORT_DIR = REPORT_DIR / "video"
AUDIO_REPORT_DIR = REPORT_DIR / "audio"
TEXT_REPORT_DIR = REPORT_DIR / "text"


# =====================================================
# Cache
# =====================================================

CACHE_DIR = BACKEND_DIR / "cache"

HF_CACHE_DIR = CACHE_DIR / "huggingface"

FACE_MODEL_CACHE = CACHE_DIR / "insightface"


# =====================================================
# Image AI
# =====================================================

IMAGE_MODEL_NAME = "prithivMLmods/deepfake-detector-model-v1"

IMAGE_SIZE = 224

IMAGE_CONFIDENCE_THRESHOLD = 0.50


# =====================================================
# Face Analysis
# =====================================================

FACE_DETECTION_THRESHOLD = 0.60

FACE_DETECTION_SIZE = (640, 640)


# =====================================================
# Text AI
# =====================================================

TEXT_MODEL_NAME = "Hello-SimpleAI/chatgpt-detector-roberta"

TEXT_MAX_LENGTH = 512

TEXT_CLASSES = [
    "real",
    "fake",
]

TEXT_NUM_CLASSES = len(TEXT_CLASSES)

TEXT_CONFIDENCE_THRESHOLD = 0.50


# =====================================================
# Audio AI
# =====================================================

AUDIO_MODEL_NAME = "facebook/wav2vec2-base"

AUDIO_SAMPLE_RATE = 16000

AUDIO_MAX_DURATION = 10

AUDIO_CLASSES = [
    "real",
    "fake",
]

AUDIO_NUM_CLASSES = len(AUDIO_CLASSES)

AUDIO_CONFIDENCE_THRESHOLD = 0.50


# =====================================================
# Video AI
# =====================================================

VIDEO_MODEL_NAME = IMAGE_MODEL_NAME

VIDEO_FRAME_SIZE = IMAGE_SIZE

VIDEO_SAMPLE_FRAMES = 16

VIDEO_CLASSES = [
    "real",
    "fake",
]

VIDEO_NUM_CLASSES = len(VIDEO_CLASSES)

VIDEO_CONFIDENCE_THRESHOLD = 0.50


# =====================================================
# General
# =====================================================

DEFAULT_BATCH_SIZE = 1

DEFAULT_NUM_WORKERS = 2

DEFAULT_RANDOM_SEED = 42


# =====================================================
# Create Required Directories
# =====================================================

DIRECTORIES = [

    IMAGE_WEIGHTS_DIR,
    VIDEO_WEIGHTS_DIR,
    AUDIO_WEIGHTS_DIR,
    TEXT_WEIGHTS_DIR,

    IMAGE_DATASET_DIR,
    VIDEO_DATASET_DIR,
    AUDIO_DATASET_DIR,
    TEXT_DATASET_DIR,

    IMAGE_REPORT_DIR,
    VIDEO_REPORT_DIR,
    AUDIO_REPORT_DIR,
    TEXT_REPORT_DIR,

    CACHE_DIR,
    HF_CACHE_DIR,

]


for directory in DIRECTORIES:

    directory.mkdir(

        parents=True,

        exist_ok=True,

    )