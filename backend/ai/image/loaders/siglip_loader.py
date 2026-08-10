"""
Primary Image Detector Loader

Loads the primary AI image detection model.
Works with any Hugging Face image classification model.
"""

import os
import logging

import torch

from transformers import (
    AutoImageProcessor,
    AutoModelForImageClassification,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------
# Configuration
# ---------------------------------------------------

MODEL_NAME = os.getenv(
    "IMAGE_MODEL",
    "Smogy/SMOGY-Ai-images-detector"
)

MODEL_DIR = "backend/weights/image/primary_detector"

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------


def load_siglip_model():

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
            exist_ok=True
        )

        processor.save_pretrained(
            MODEL_DIR
        )

        model.save_pretrained(
            MODEL_DIR
        )

    # ---------------------------------------------------
    # Device
    # ---------------------------------------------------

    if torch.backends.mps.is_available():

        device = torch.device("mps")

    elif torch.cuda.is_available():

        device = torch.device("cuda")

    else:

        device = torch.device("cpu")

    model.to(device)

    model.eval()

    logger.info(f"Device : {device}")
    logger.info(f"Model  : {MODEL_NAME}")

    if hasattr(model.config, "id2label"):

        logger.info(f"Labels : {model.config.id2label}")

    return {

        "name": MODEL_NAME,

        "model": model,

        "processor": processor,

        "device": device,


    }