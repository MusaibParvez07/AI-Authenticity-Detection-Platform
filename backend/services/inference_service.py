import torch
from PIL import Image

from backend.services.model_loader import get_image_model


def predict_image(file_path: str) -> dict:

    metadata = get_image_model()

    model = metadata.model
    processor = metadata.processor

    image = Image.open(file_path).convert("RGB")

    print(f"Using model: {metadata.name}")

    device = next(model.parameters()).device

    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    model.eval()

    with torch.no_grad():

        outputs = model(**inputs)

        probabilities = torch.softmax(
            outputs.logits,
            dim=1
        )

        confidence, prediction_idx = torch.max(
            probabilities,
            dim=1
        )

    label = model.config.id2label[
        prediction_idx.item()
    ].lower()

    if label in [
        "ai",
        "fake",
        "generated"
    ]:

        prediction = "fake"

    else:

        prediction = "real"

    return {

        "prediction": prediction,

        "confidence": round(
            confidence.item(),
            4
        )

    }