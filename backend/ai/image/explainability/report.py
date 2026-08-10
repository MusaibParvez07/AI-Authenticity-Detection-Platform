"""
Professional Report Formatter
"""


class ReportFormatter:

    def build(
        self,
        report,
    ):

        return {

            "prediction":

                report["explanation"]["prediction"],

            "confidence":

                report["explanation"]["confidence"],

            "summary":

                report["explanation"]["summary"],

            "analysis":

                report["explanation"]["analysis"],

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


report_formatter = ReportFormatter()