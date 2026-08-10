"""
Professional Face Inference

Runs face detection and returns raw Face objects
plus a lightweight summary for downstream modules.
"""

from pathlib import Path

from backend.ai.image.face.detector import (
    face_detector,
)


class FaceInference:

    def analyze(
        self,
        image_path: str | Path,
    ):

        image_path = Path(image_path)

        if not image_path.exists():

            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        faces = face_detector.detect(
            image_path
        )

        summary = []

        for i, face in enumerate(faces):

            summary.append(

                {

                    "face_id": i + 1,

                    "bbox": face.bbox.tolist(),

                    "confidence": float(
                        face.det_score
                    ),

                }

            )

        return {

            "status": "success",

            "image": str(
                image_path
            ),

            "faces_detected": len(
                faces
            ),

            # JSON-safe summary
            "summary": summary,

            # Raw InsightFace objects
            "faces": faces,

        }


face_inference = FaceInference()