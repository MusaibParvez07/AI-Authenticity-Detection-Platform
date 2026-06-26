import torch

from backend.services.model_loader import get_image_model
from backend.services.image_preprocessing import preprocess_image
from backend.services.tensor_preprocessing import image_to_tensor


def predict_image(file_path: str) -> dict:

    metadata = get_image_model()

    image = preprocess_image(
        image_path=file_path
    )

    print(
        f"Using model: {metadata.name}"
    )

    print(
        f"Processed Image Size: {image.size}"
    )

    model = metadata.model

    tensor = image_to_tensor(
        image_path=file_path
    )

    print(
        f"Tensor Shape: {tensor.shape}"
    )

    model.eval()

    with torch.no_grad():

        output = model(
            tensor
        )

        probabilities = torch.softmax(
            output,
            dim=1
        )

        confidence, prediction_idx = torch.max(
            probabilities,
            dim=1
        )

    prediction = (
        "real"
        if prediction_idx.item() == 0
        else "fake"
    )

    return {
        "prediction": prediction,
        "confidence": round(
            confidence.item(),
            4
        )
    }