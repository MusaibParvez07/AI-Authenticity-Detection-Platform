from pathlib import Path

from backend.config import IMAGE_DIR

from backend.ai.image.face.pipeline import face_pipeline

images = list(IMAGE_DIR.glob("*"))

print("=" * 60)

for image in images[:10]:

    print(f"\nTesting: {image.name}")

    result = face_pipeline.analyze(image)

    print(result["faces_detected"])