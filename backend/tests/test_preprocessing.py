from pathlib import Path

from backend.ai.image.preprocessing import preprocess_image

image_path = Path(
    "/Users/mukundkumar/Downloads/IMG_1975.JPG"
)

tensor = preprocess_image(image_path)

print(tensor.shape)