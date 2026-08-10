"""
Face Quality Analyzer
"""

from __future__ import annotations

import cv2
import numpy as np


class FaceQualityAnalyzer:

    def analyze(
        self,
        image,
        face,
    ):

        bbox = face.bbox.astype(int)

        x1, y1, x2, y2 = bbox

        h, w = image.shape[:2]

        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(w, x2)
        y2 = min(h, y2)

        crop = image[
            y1:y2,
            x1:x2
        ]

        if crop.size == 0:

            return {

                "blur": 0.0,

                "brightness": 0.0,

                "contrast": 0.0,

                "sharpness": 0.0,

                "resolution": 0,

                "face_width": 0,

                "face_height": 0,

            }

        gray = cv2.cvtColor(
            crop,
            cv2.COLOR_BGR2GRAY
        )

        blur = cv2.Laplacian(
            gray,
            cv2.CV_64F
        ).var()

        brightness = float(
            gray.mean()
        )

        contrast = float(
            gray.std()
        )

        sharpness = float(
            np.mean(
                cv2.Sobel(
                    gray,
                    cv2.CV_64F,
                    1,
                    1,
                )
            )
        )

        face_width = x2 - x1
        face_height = y2 - y1

        resolution = (
            face_width *
            face_height
        )

        return {

            "blur": float(
                blur
            ),

            "brightness": brightness,

            "contrast": contrast,

            "sharpness": sharpness,

            "resolution": int(
                resolution
            ),

            "face_width": int(
                face_width
            ),

            "face_height": int(
                face_height
            ),

        }


face_quality = FaceQualityAnalyzer()