"""
Professional Explainability Engine
"""

from backend.ai.image.explainability.rules import (
    rules_engine,
)


class ExplainabilityEngine:

    def generate(
        self,
        report,
    ):

        reasons = rules_engine.analyze(
            report
        )

        ai = report["ai_detector"]

        return {

            "prediction":

                ai["prediction"].upper(),

            "confidence":

                ai["confidence_percent"],

            "analysis":

                reasons,

            "summary":

                self.summary(
                    report
                ),

        }

    # ------------------------------------------------

    def summary(
        self,
        report,
    ):

        ai = report["ai_detector"]

        if ai["prediction"] == "fake":

            if ai["confidence"] > 0.90:

                return (
                    "The uploaded image shows strong evidence of AI generation."
                )

            elif ai["confidence"] > 0.75:

                return (
                    "The uploaded image is likely AI-generated."
                )

            return (
                "The uploaded image contains suspicious characteristics."
            )

        else:

            if ai["confidence"] > 0.90:

                return (
                    "The uploaded image appears authentic."
                )

            return (
                "The uploaded image appears mostly authentic."
            )


explainability_engine = ExplainabilityEngine()