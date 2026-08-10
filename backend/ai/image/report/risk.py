"""
Professional Risk Assessment
"""


class RiskAnalyzer:

    def calculate(
        self,
        report,
    ):

        score = report["decision"]["authenticity_score"]

        if score >= 85:

            return {

                "level": "VERY LOW",

                "color": "green",

                "message": "Image appears highly authentic.",

            }

        if score >= 70:

            return {

                "level": "LOW",

                "color": "green",

                "message": "Image appears authentic.",

            }

        if score >= 50:

            return {

                "level": "MEDIUM",

                "color": "orange",

                "message": "Further verification is recommended.",

            }

        if score >= 30:

            return {

                "level": "HIGH",

                "color": "red",

                "message": "Image contains suspicious characteristics.",

            }

        return {

            "level": "VERY HIGH",

            "color": "darkred",

            "message": "Image is highly likely to be AI generated.",

        }


risk_analyzer = RiskAnalyzer()