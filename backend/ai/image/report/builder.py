"""
Professional Image Report Builder
"""

from backend.ai.image.report.risk import (
    risk_analyzer,
)

from backend.ai.image.report.recommendation import (
    recommendation_engine,
)


class ReportBuilder:

    def build(
        self,
        report,
    ):

        risk = risk_analyzer.calculate(
            report
        )

        recommendation = recommendation_engine.generate(
            report
        )

        return {

            "prediction":

                report["decision"]["prediction"],

            "authenticity_score":

                report["decision"]["authenticity_score"],

            "confidence":

                report["ai_detector"]["confidence_percent"],

            "risk":

                risk,

            "recommendation":

                recommendation,

            "explanation":

                report["explanation"],

            "visuals": {

                "faces":

                    report["visuals"]["files"]["faces"],

                "ela":

                    report["visuals"]["files"]["ela"],

                "noise":

                    report["visuals"]["files"]["noise"],

                "jpeg":

                    report["visuals"]["files"]["jpeg"],

            },

            "forensics": {

                "faces":

                    report["face_analysis"]["faces_detected"],

                "ela":

                    report["ela"]["max_difference"],

                "noise":

                    report["noise"]["mean_noise"],

                "jpeg":

                    report["jpeg"]["jpeg_artifact_score"],

            }

        }


report_builder = ReportBuilder()