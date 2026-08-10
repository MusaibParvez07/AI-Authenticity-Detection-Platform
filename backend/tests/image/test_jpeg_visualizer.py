from pathlib import Path

from backend.ai.image.visual.jpeg_visualizer import (
    jpeg_visualizer,
)

image = Path(
    "datasets/image/c3ec910e5e284706a104f06f00263be7.JPG"
)

result = jpeg_visualizer.visualize(

    image,

    "datasets/output/jpeg/result.png",

)

print(result)