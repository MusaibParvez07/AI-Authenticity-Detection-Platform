from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "datasets"

IMAGE_DIR = DATASET_DIR / "image"
VIDEO_DIR = DATASET_DIR / "video"
AUDIO_DIR = DATASET_DIR / "audio"
TEXT_DIR = DATASET_DIR / "text"

IMAGE_DIR.mkdir(exist_ok=True)
VIDEO_DIR.mkdir(exist_ok=True)
AUDIO_DIR.mkdir(exist_ok=True)
TEXT_DIR.mkdir(exist_ok=True)