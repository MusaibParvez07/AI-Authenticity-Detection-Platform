"""
Face Geometry & Consistency Analyzer

Computes geometric measurements from
InsightFace facial landmarks.

These measurements will later be used
by the Digital Forensics Engine.
"""

from __future__ import annotations

import math


class FaceGeometryAnalyzer:

    # ----------------------------------------
    # Euclidean Distance
    # ----------------------------------------

    @staticmethod
    def distance(p1, p2):

        return math.sqrt(

            (p1[0] - p2[0]) ** 2 +

            (p1[1] - p2[1]) ** 2

        )

    # ----------------------------------------
    # Analyze
    # ----------------------------------------

    def analyze(

        self,

        face,

    ):

        if not hasattr(

            face,

            "kps",

        ):

            return {}

        landmarks = face.kps

        left_eye = landmarks[0]

        right_eye = landmarks[1]

        nose = landmarks[2]

        left_mouth = landmarks[3]

        right_mouth = landmarks[4]

        eye_distance = self.distance(

            left_eye,

            right_eye,

        )

        mouth_width = self.distance(

            left_mouth,

            right_mouth,

        )

        eye_to_nose = (

            self.distance(

                left_eye,

                nose,

            )

            +

            self.distance(

                right_eye,

                nose,

            )

        ) / 2

        nose_to_mouth = (

            self.distance(

                nose,

                left_mouth,

            )

            +

            self.distance(

                nose,

                right_mouth,

            )

        ) / 2

        face_width = (

            face.bbox[2]

            -

            face.bbox[0]

        )

        face_height = (

            face.bbox[3]

            -

            face.bbox[1]

        )

        aspect_ratio = (

            face_width /

            face_height

        )

        return {

            "eye_distance":

                float(

                    eye_distance

                ),

            "mouth_width":

                float(

                    mouth_width

                ),

            "eye_to_nose":

                float(

                    eye_to_nose

                ),

            "nose_to_mouth":

                float(

                    nose_to_mouth

                ),

            "face_width":

                float(

                    face_width

                ),

            "face_height":

                float(

                    face_height

                ),

            "aspect_ratio":

                float(

                    aspect_ratio

                ),

        }


face_geometry = FaceGeometryAnalyzer()