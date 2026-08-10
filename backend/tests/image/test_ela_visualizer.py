from pathlib import Path

from backend.ai.image.visual.ela_visualizer import (
    ela_visualizer,
)

image = Path(
    "datasets/image/c3ec910e5e284706a104f06f00263be7.JPG"
)

result = ela_visualizer.visualize(

    image,

    "datasets/output/ela/result.png",

)

print(result)