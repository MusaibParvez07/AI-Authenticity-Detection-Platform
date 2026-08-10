from pprint import pprint

from backend.config import IMAGE_DIR

from backend.ai.image.feature_extractor import (
    feature_extractor,
)

image = next(
    IMAGE_DIR.glob("*")
)

features = feature_extractor.extract(
    image
)

pprint(features)