"""
Image Authenticity Scoring Engine
"""

from backend.ai.image.decision.weights import *


class ImageScorer:

    def score(
        self,
        report,
    ):

        # -----------------------------
        # AI Score
        # -----------------------------

        ai = report["ai_detector"]

        if ai["prediction"] == "real":

            ai_score = ai["confidence"]

        else:

            ai_score = 1 - ai["confidence"]

        # -----------------------------
        # Face Score
        # -----------------------------

        faces = report["face_analysis"]["faces_detected"]

        face_score = 1.0 if faces > 0 else 0.60

        # -----------------------------
        # ELA
        # -----------------------------

        ela = report["ela"]["max_difference"]

        ela_score = max(

            0,

            1 - (ela / 50)

        )

        # -----------------------------
        # Noise
        # -----------------------------

        noise = report["noise"]["mean_noise"]

        noise_score = min(

            noise / 10,

            1.0

        )

        # -----------------------------
        # JPEG
        # -----------------------------

        jpeg = report["jpeg"]["jpeg_artifact_score"]

        jpeg_score = max(

            0,

            1 - (jpeg / 20)

        )

        # -----------------------------
        # Final Weighted Score
        # -----------------------------

        final_score = (

            ai_score * AI_WEIGHT +

            face_score * FACE_WEIGHT +

            ela_score * ELA_WEIGHT +

            noise_score * NOISE_WEIGHT +

            jpeg_score * JPEG_WEIGHT

        )

        final_score *= 100

        prediction = (

            "Real"

            if final_score >= 50

            else

            "Fake"

        )

        return {

            "prediction": prediction,

            "authenticity_score":

                round(final_score, 2),

            "components": {

                "ai_score":

                    round(ai_score, 3),

                "face_score":

                    round(face_score, 3),

                "ela_score":

                    round(ela_score, 3),

                "noise_score":

                    round(noise_score, 3),

                "jpeg_score":

                    round(jpeg_score, 3),

            }

        }


image_scorer = ImageScorer()