"""
Professional Face Detector

Uses InsightFace to detect faces and returns
raw InsightFace Face objects.

Every downstream analyzer (landmarks, quality,
geometry, etc.) works directly on these objects.
"""

from pathlib import Path

import cv2

from insightface.app import FaceAnalysis

from backend.ai.config import (
    FACE_DETECTION_SIZE,
)


class FaceDetector:

    def __init__(self):

        self.app = FaceAnalysis(

            name="buffalo_l",

            providers=[
                "CPUExecutionProvider",
            ],

        )

        self.app.prepare(

            ctx_id=0,

            det_size=FACE_DETECTION_SIZE,

        )

    # -------------------------------------------------
    # Detect Faces
    # -------------------------------------------------

    def detect(

        self,

        image_path: str | Path,

    ):

        image_path = Path(image_path)

        image = cv2.imread(

            str(image_path)

        )

        if image is None:

            raise FileNotFoundError(

                f"Cannot read image: {image_path}"

            )

        faces = self.app.get(

            image

        )

        # =====================================================
        # DEBUG OUTPUT
        # =====================================================

        print("\n" + "=" * 70)
        print("FACE DETECTOR")
        print("=" * 70)

        print(f"Image : {image_path}")

        print(f"Resolution : {image.shape[1]} x {image.shape[0]}")

        print(f"Faces Detected : {len(faces)}")

        if len(faces) == 0:

            print("No faces found.")

        else:

            for i, face in enumerate(faces):

                print("\n" + "-" * 40)

                print(f"Face {i + 1}")

                print("-" * 40)

                print("Bounding Box :")

                print(face.bbox)

                print()

                print("Confidence :")

                print(face.det_score)

                if hasattr(face, "kps"):

                    print()

                    print("5 Landmarks :")

                    print(face.kps)

                if hasattr(face, "landmark_2d_106"):

                    print()

                    print("106 Landmarks Loaded")

                if hasattr(face, "gender"):

                    print()

                    print(f"Gender : {face.gender}")

                if hasattr(face, "age"):

                    print(f"Age : {face.age}")

        print("=" * 70 + "\n")

        # =====================================================

        return faces


face_detector = FaceDetector()