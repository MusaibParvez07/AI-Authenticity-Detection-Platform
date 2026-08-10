"""
Professional Image Analysis Pipeline

Runs every image analysis module and
returns a complete forensic report.
"""

from pathlib import Path

from backend.ai.image.inference import (
    image_inference,
)

from backend.ai.image.face.pipeline import (
    face_pipeline,
)

from backend.ai.image.forensics.ela import (
    ela_analyzer,
)

from backend.ai.image.forensics.noise import (
    noise_analyzer,
)

from backend.ai.image.forensics.jpeg import (
    jpeg_analyzer,
)

from backend.ai.image.visual.pipeline import (
    visual_pipeline,
)

from backend.ai.image.decision.scorer import (
    image_scorer,
)

from backend.ai.image.explainability.engine import (
    explainability_engine,
)

from backend.ai.image.explainability.report import (
    report_formatter,
)

from backend.ai.image.report.builder import (
    report_builder,
)


class ImagePipeline:

    def analyze(
        self,
        image_path: str | Path,
    ):

        image_path = Path(image_path)

        # ==================================================
        # AI DETECTOR
        # ==================================================

        ai_result = image_inference.predict(
            image_path
        )

        # ==================================================
        # FACE ANALYSIS
        # ==================================================

        face_result = face_pipeline.analyze(
            image_path
        )

        # ==================================================
        # ERROR LEVEL ANALYSIS
        # ==================================================

        ela_result = ela_analyzer.analyze(
            image_path
        )

        # ==================================================
        # NOISE ANALYSIS
        # ==================================================

        noise_result = noise_analyzer.analyze(
            image_path
        )

        # ==================================================
        # JPEG ANALYSIS
        # ==================================================

        jpeg_result = jpeg_analyzer.analyze(
            image_path
        )

        # ==================================================
        # BUILD REPORT
        # ==================================================

        report = {

            "image": str(image_path),

            "ai_detector": ai_result,

            "face_analysis": face_result,

            "ela": {

                "max_difference":
                    ela_result["max_difference"],

                "compression_quality":
                    ela_result["compression_quality"],

            },

            "noise": {

                "mean_noise":
                    noise_result["mean_noise"],

                "std_noise":
                    noise_result["std_noise"],

                "median_noise":
                    noise_result["median_noise"],

                "max_noise":
                    noise_result["max_noise"],

                "high_noise_ratio":
                    noise_result["high_noise_ratio"],

            },

            "jpeg": {

                "jpeg_artifact_score":
                    jpeg_result["jpeg_artifact_score"],

                "vertical_block_score":
                    jpeg_result["vertical_block_score"],

                "horizontal_block_score":
                    jpeg_result["horizontal_block_score"],

                "vertical_std":
                    jpeg_result["vertical_std"],

                "horizontal_std":
                    jpeg_result["horizontal_std"],

            },

        }

        # ==================================================
        # VISUAL FORENSICS
        # ==================================================

        visuals = visual_pipeline.generate(
            image_path
        )

        report["visuals"] = visuals

        # ==================================================
        # DECISION ENGINE
        # ==================================================

        decision = image_scorer.score(
            report
        )

        report["decision"] = decision

        # ==================================================
        # EXPLAINABILITY
        # ==================================================

        explanation = explainability_engine.generate(
            report
        )

        report["explanation"] = explanation

        # ==================================================
        # PROFESSIONAL REPORT
        # ==================================================

        report["professional_report"] = report_builder.build(
            report
        )

        # ==================================================
        # LEGACY FORMATTER
        # ==================================================

        report["formatted_report"] = report_formatter.build(
            report
        )

        # ==================================================
        # RETURN
        # ==================================================

        return report


image_pipeline = ImagePipeline()