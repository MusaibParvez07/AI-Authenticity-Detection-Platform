"""
Primary Image Detector Loader

Loads the primary AI image detection model.
Supports any Hugging Face image classification model.
"""

import logging
import os

import torch
from transformers import (
    AutoImageProcessor,
    AutoModelForImageClassification,
)

logger = logging.getLogger(__name__)

# =====================================================
# Configuration
# =====================================================

MODEL_NAME = os.getenv(
    "IMAGE_MODEL",
    "prithivMLmods/deepfake-detector-model-v1",
)

MODEL_DIR = "backend/weights/image/deepfake_detector_v1"


# =====================================================
# Device
# =====================================================

def get_device():

    if torch.backends.mps.is_available():

        return torch.device("mps")

    if torch.cuda.is_available():

        return torch.device("cuda")

    return torch.device("cpu")


# =====================================================
# Load Primary Detector
# =====================================================

def load_image_detector():

    logger.info("=" * 60)
    logger.info("Loading Primary Image Detector...")
    logger.info("=" * 60)

    if os.path.exists(MODEL_DIR):

        logger.info("Loading model from local cache...")

        processor = AutoImageProcessor.from_pretrained(
            MODEL_DIR
        )

        model = AutoModelForImageClassification.from_pretrained(
            MODEL_DIR
        )

    else:

        logger.info("Downloading model from Hugging Face...")

        processor = AutoImageProcessor.from_pretrained(
            MODEL_NAME
        )

        model = AutoModelForImageClassification.from_pretrained(
            MODEL_NAME
        )

        os.makedirs(
            MODEL_DIR,
            exist_ok=True,
        )

        processor.save_pretrained(
            MODEL_DIR
        )

        model.save_pretrained(
            MODEL_DIR
        )

    device = get_device()

    model.to(device)

    model.eval()

    print("=" * 60)
    print("PRIMARY IMAGE DETECTOR")
    print("=" * 60)

    print(f"Model      : {MODEL_NAME}")
    print(f"Cache      : {MODEL_DIR}")
    print(f"Device     : {device}")

    if hasattr(model.config, "_name_or_path"):

        print(
            f"Checkpoint : {model.config._name_or_path}"
        )

    if hasattr(model.config, "id2label"):

        print(
            f"Labels     : {model.config.id2label}"
        )

    print("=" * 60)

    return {

        "name": MODEL_NAME,

        "model": model,

        "processor": processor,

        "device": device,

    }


# ----------------------------------------------------
# Backward Compatibility
# ----------------------------------------------------

def load_siglip_model():
    """
    Temporary wrapper so the rest of the project
    doesn't need to change immediately.
    """
    return load_image_detector()