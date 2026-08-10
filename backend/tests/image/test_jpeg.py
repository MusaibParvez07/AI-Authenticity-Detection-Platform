from backend.config import IMAGE_DIR

from backend.ai.image.forensics.jpeg import (
    jpeg_analyzer,
)

image = next(
    IMAGE_DIR.glob("*")
)

print(image)

result = jpeg_analyzer.analyze(
    image
)

print()

for key, value in result.items():

    print(f"{key:30}: {value}")