"""
Professional Recommendations
"""


class RecommendationEngine:

    def generate(
        self,
        report,
    ):

        prediction = report["decision"]["prediction"]

        score = report["decision"]["authenticity_score"]

        if prediction.lower() == "fake":

            if score < 30:

                return [
                    "Do not rely on this image without independent verification.",
                    "Compare the image with trusted sources.",
                    "Inspect metadata before making decisions.",
                    "Use additional forensic tools if required.",
                ]

            return [
                "Image contains suspicious forensic indicators.",
                "Further verification is recommended.",
            ]

        return [

            "Image appears authentic.",

            "No major forensic inconsistencies detected.",

        ]


recommendation_engine = RecommendationEngine()