from transformers import (
    AutoModelForImageClassification,
    AutoImageProcessor,
)

import torch


MODEL_NAME = "Ateeqq/ai-vs-human-image-detector"


def load_siglip_model():

    print(f"Loading {MODEL_NAME}...")

    processor = AutoImageProcessor.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForImageClassification.from_pretrained(
        MODEL_NAME
    )

    device = (
        "mps"
        if torch.backends.mps.is_available()
        else "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    model.to(device)

    model.eval()

    print(f"Loaded on {device}")

    return model, processor