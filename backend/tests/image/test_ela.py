from pathlib import Path

from backend.ai.image.forensics.ela import (
    ela_analyzer,
)

from backend.config import IMAGE_DIR


image = next(
    IMAGE_DIR.glob("*")
)

print(image)

result = ela_analyzer.analyze(
    image
)

print(result)