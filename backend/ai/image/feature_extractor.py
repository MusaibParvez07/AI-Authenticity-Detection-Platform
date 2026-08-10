"""
Image Feature Extractor

Converts the forensic pipeline report into
a numerical feature vector suitable for ML.
"""

from pathlib import Path

from backend.ai.image.pipeline import image_pipeline


class ImageFeatureExtractor:

    def extract(
        self,
        image_path: str | Path,
    ):

        report = image_pipeline.analyze(
            image_path
        )

        features = {

            # ------------------------
            # AI
            # ------------------------

            "ai_prediction":

                report["ai_detector"]["prediction"],

            "ai_confidence":

                report["ai_detector"]["confidence"],

            # ------------------------
            # Face
            # ------------------------

            "faces_detected":

                report["face_analysis"]["faces_detected"],

            # ------------------------
            # ELA
            # ------------------------

            "ela_max_difference":

                report["ela"]["max_difference"],

            # ------------------------
            # Noise
            # ------------------------

            "noise_mean":

                report["noise"]["mean_noise"],

            "noise_std":

                report["noise"]["std_noise"],

            "noise_max":

                report["noise"]["max_noise"],

            "noise_ratio":

                report["noise"]["high_noise_ratio"],

            # ------------------------
            # JPEG
            # ------------------------

            "jpeg_score":

                report["jpeg"]["jpeg_artifact_score"],

            "jpeg_vertical":

                report["jpeg"]["vertical_block_score"],

            "jpeg_horizontal":

                report["jpeg"]["horizontal_block_score"],

        }

        return features


feature_extractor = ImageFeatureExtractor()