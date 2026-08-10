"""
Professional Face Landmark Analyzer

Supports both:
- 106 landmarks (InsightFace)
- 5 landmarks (fallback)
"""

from __future__ import annotations


class LandmarkAnalyzer:

    # -----------------------------------------
    # Extract Landmarks
    # -----------------------------------------

    def extract(
        self,
        face,
    ):

        result = {}

        # -----------------------------------------
        # 106 Landmarks
        # -----------------------------------------

        if hasattr(face, "landmark_2d_106"):

            landmarks = face.landmark_2d_106

            result["type"] = "106"

            result["num_landmarks"] = len(
                landmarks
            )

            result["landmarks"] = landmarks.tolist()

            return result

        # -----------------------------------------
        # 5 Landmarks
        # -----------------------------------------

        if hasattr(face, "kps"):

            landmarks = face.kps

            result["type"] = "5"

            result["num_landmarks"] = len(
                landmarks
            )

            result["landmarks"] = landmarks.tolist()

            return result

        # -----------------------------------------

        return {

            "type": "none",

            "num_landmarks": 0,

            "landmarks": [],

        }


landmark_analyzer = LandmarkAnalyzer()