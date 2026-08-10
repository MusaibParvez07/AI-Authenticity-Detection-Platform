import os
import torch

from transformers import (
    AutoImageProcessor,
    SiglipForImageClassification,
)

MODEL_NAME = "Ateeqq/ai-vs-human-image-detector"

MODEL_DIR = "backend/weights/image/active_model"


def load_vit_model():

    print("=" * 60)
    print("Loading Image Detection Model...")
    print("=" * 60)

    if os.path.exists(MODEL_DIR):

        print("Loading model from local cache...")

        processor = AutoImageProcessor.from_pretrained(
            MODEL_DIR
        )

        model = SiglipForImageClassification.from_pretrained(
            MODEL_DIR
        )

    else:

        print("Downloading model from Hugging Face...")

        processor = AutoImageProcessor.from_pretrained(
            MODEL_NAME
        )

        model = SiglipForImageClassification.from_pretrained(
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

    if torch.backends.mps.is_available():

        device = torch.device("mps")

    elif torch.cuda.is_available():

        device = torch.device("cuda")

    else:

        device = torch.device("cpu")

    model.to(device)

    model.eval()

    print(f"Device : {device}")
    print(f"Model  : {MODEL_NAME}")

    return model, processor