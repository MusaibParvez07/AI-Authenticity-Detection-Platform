from backend.ai.image.inference import (
    image_inference
)

result = image_inference.predict(
    "/Users/mukundkumar/Downloads/IMG_1975.JPG"
)

print()

print(result)