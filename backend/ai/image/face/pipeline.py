"""
Face Analysis Pipeline

Runs every face analysis module and
returns a single structured report.
"""

from pathlib import Path

import cv2

from backend.ai.image.face.inference import (
    face_inference,
)

from backend.ai.image.face.landmarks import (
    landmark_analyzer,
)

from backend.ai.image.face.quality import (
    face_quality,
)

from backend.ai.image.face.consistency import (
    face_geometry,
)


class FacePipeline:

    def analyze(
        self,
        image_path: str | Path,
    ):

        image = cv2.imread(
            str(image_path)
        )

        result = face_inference.analyze(
            image_path
        )

        report = []

        for face in result["faces"]:

            report.append(

                {

                    "quality":

                        face_quality.analyze(
                            image,
                            face,
                        ),

                    "geometry":

                        face_geometry.analyze(
                            face,
                        ),

                    "landmarks":

                        landmark_analyzer.extract(
                            face,
                        ),

                }

            )

        return {

            "faces_detected":

                result["faces_detected"],

            "faces":

                report,

        }


face_pipeline = FacePipeline()