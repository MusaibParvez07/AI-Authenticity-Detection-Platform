import cv2

from backend.ai.image.face.inference import (
    face_inference,
)

from backend.ai.image.face.quality import (
    face_quality,
)

IMAGE = "datasets/image/sample.jpg"

image = cv2.imread(
    IMAGE
)

result = face_inference.analyze(
    IMAGE
)

print("=" * 70)

for i, face in enumerate(
    result["faces"]
):

    print(f"\nFACE {i+1}")

    quality = face_quality.analyze(
        image,
        face
    )

    for k, v in quality.items():

        print(
            f"{k:15}: {v}"
        )