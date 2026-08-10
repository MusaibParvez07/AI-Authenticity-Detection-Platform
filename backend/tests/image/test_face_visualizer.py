from backend.config import IMAGE_DIR

from backend.ai.image.visual.face_visualizer import (
    face_visualizer,
)

image = next(
    IMAGE_DIR.glob("*")
)

result = face_visualizer.visualize(

    image,

    "datasets/output/faces/result.png",

)

print(result)