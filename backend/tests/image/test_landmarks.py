from backend.ai.image.face.inference import (
    face_inference,
)

from backend.ai.image.face.landmarks import (
    landmark_analyzer,
)

result = face_inference.analyze(
    "datasets/image/sample.jpg"
)

for index, face in enumerate(result["faces"]):

    print("=" * 60)

    print("FACE", index)

    print("=" * 60)

    data = landmark_analyzer.extract(
        face
    )

    print(data)