from pathlib import Path

from backend.ai.image.visual.noise_visualizer import (
    noise_visualizer,
)

image = Path(
    "datasets/image/c3ec910e5e284706a104f06f00263be7.JPG"
)

result = noise_visualizer.visualize(

    image,

    "datasets/output/noise/result.png",

)

print(result)