"""
JPEG Compression Artifact Analyzer

Analyzes JPEG compression quality and block artifacts.
"""

from pathlib import Path

import cv2
import numpy as np


class JPEGArtifactAnalyzer:

    def analyze(
        self,
        image_path: str | Path,
    ):

        image = cv2.imread(str(image_path))

        if image is None:
            raise FileNotFoundError(image_path)

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY,
        )

        height, width = gray.shape

        vertical = []
        horizontal = []

        # ------------------------------------------
        # Vertical JPEG Block Boundaries
        # ------------------------------------------

        for x in range(8, width, 8):

            diff = np.abs(

                gray[:, x].astype(np.int32)

                -

                gray[:, x - 1].astype(np.int32)

            )

            vertical.append(
                np.mean(diff)
            )

        # ------------------------------------------
        # Horizontal JPEG Block Boundaries
        # ------------------------------------------

        for y in range(8, height, 8):

            diff = np.abs(

                gray[y, :].astype(np.int32)

                -

                gray[y - 1, :].astype(np.int32)

            )

            horizontal.append(
                np.mean(diff)
            )

        vertical = np.array(vertical)

        horizontal = np.array(horizontal)

        return {

            "vertical_block_score":
                float(vertical.mean()),

            "horizontal_block_score":
                float(horizontal.mean()),

            "jpeg_artifact_score":
                float(
                    (vertical.mean() + horizontal.mean()) / 2
                ),

            "vertical_std":
                float(vertical.std()),

            "horizontal_std":
                float(horizontal.std()),

        }


jpeg_analyzer = JPEGArtifactAnalyzer()