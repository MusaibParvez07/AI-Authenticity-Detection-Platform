"""
Professional Explainability Rules
"""


class ExplainabilityRules:

    def analyze(
        self,
        report,
    ):

        reasons = []

        ai = report["ai_detector"]

        # ------------------------------------------------
        # AI Detector
        # ------------------------------------------------

        if ai["prediction"] == "fake":

            if ai["confidence"] >= 0.90:

                reasons.append(
                    "AI detector has very high confidence that the image is AI-generated."
                )

            elif ai["confidence"] >= 0.75:

                reasons.append(
                    "AI detector indicates strong evidence of AI generation."
                )

            else:

                reasons.append(
                    "AI detector indicates moderate evidence of AI generation."
                )

        else:

            if ai["confidence"] >= 0.90:

                reasons.append(
                    "AI detector has very high confidence that the image is authentic."
                )

            else:

                reasons.append(
                    "AI detector predicts the image is authentic."
                )

        # ------------------------------------------------
        # Face Analysis
        # ------------------------------------------------

        faces = report["face_analysis"]["faces_detected"]

        if faces == 0:

            reasons.append(
                "No human face was detected."
            )

        elif faces == 1:

            reasons.append(
                "One face detected with stable facial landmarks."
            )

        else:

            reasons.append(
                f"{faces} human faces detected."
            )

        # ------------------------------------------------
        # ELA
        # ------------------------------------------------

        ela = report["ela"]["max_difference"]

        if ela >= 40:

            reasons.append(
                "High Error Level Analysis difference detected."
            )

        elif ela >= 20:

            reasons.append(
                "Moderate Error Level Analysis difference detected."
            )

        else:

            reasons.append(
                "Low Error Level Analysis difference detected."
            )

        # ------------------------------------------------
        # Noise
        # ------------------------------------------------

        noise = report["noise"]["mean_noise"]

        if noise < 2:

            reasons.append(
                "Very smooth image noise pattern."
            )

        elif noise < 5:

            reasons.append(
                "Natural sensor noise detected."
            )

        else:

            reasons.append(
                "High image noise detected."
            )

        # ------------------------------------------------
        # JPEG
        # ------------------------------------------------

        jpeg = report["jpeg"]["jpeg_artifact_score"]

        if jpeg > 10:

            reasons.append(
                "Strong JPEG compression artifacts."
            )

        elif jpeg > 5:

            reasons.append(
                "Moderate JPEG compression artifacts."
            )

        else:

            reasons.append(
                "JPEG compression artifacts are minimal."
            )

        return reasons


rules_engine = ExplainabilityRules()