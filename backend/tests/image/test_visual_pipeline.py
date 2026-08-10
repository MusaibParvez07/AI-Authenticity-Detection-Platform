from pathlib import Path
from pprint import pprint

from backend.ai.image.visual.pipeline import (
    visual_pipeline,
)

image = Path(
    "datasets/image/c3ec910e5e284706a104f06f00263be7.JPG"
)

result = visual_pipeline.generate(
    image
)

pprint(result)