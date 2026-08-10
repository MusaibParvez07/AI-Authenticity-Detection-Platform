from pprint import pprint

from backend.config import IMAGE_DIR

from backend.ai.image.pipeline import (
    image_pipeline,
)

image = next(
    IMAGE_DIR.glob("*")
)

print()

print("=" * 70)

print(image)

print("=" * 70)

report = image_pipeline.analyze(
    image
)

pprint(report)