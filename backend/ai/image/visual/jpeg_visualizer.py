"""
Professional JPEG Artifact Visualizer

Highlights JPEG 8x8 compression block artifacts.
"""

from pathlib import Path

import cv2
import numpy as np


class JPEGVisualizer:

    def visualize(
        self,
        image_path: str | Path,
        output_path: str | Path,
    ):

        image_path = Path(image_path)
        output_path = Path(output_path)

        image = cv2.imread(str(image_path))

        if image is None:
            raise FileNotFoundError(image_path)

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY,
        )

        h, w = gray.shape

        artifact = np.zeros_like(gray)

        # -------------------------------------
        # Vertical JPEG Blocks
        # -------------------------------------

        for x in range(8, w, 8):

            diff = np.abs(

                gray[:, x].astype(np.int16)

                -

                gray[:, x - 1].astype(np.int16)

            )

            artifact[:, x] = np.clip(diff, 0, 255)

        # -------------------------------------
        # Horizontal JPEG Blocks
        # -------------------------------------

        for y in range(8, h, 8):

            diff = np.abs(

                gray[y, :].astype(np.int16)

                -

                gray[y - 1, :].astype(np.int16)

            )

            artifact[y, :] = np.maximum(

                artifact[y, :],

                np.clip(diff, 0, 255),

            )

        # -------------------------------------
        # Normalize
        # -------------------------------------

        artifact = cv2.normalize(

            artifact,

            None,

            0,

            255,

            cv2.NORM_MINMAX,

        )

        artifact = artifact.astype(np.uint8)

        heatmap = cv2.applyColorMap(

            artifact,

            cv2.COLORMAP_JET,

        )

        output_path.parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        cv2.imwrite(

            str(output_path),

            heatmap,

        )

        return {

            "saved_to":

                str(output_path),

            "artifact_score":

                float(np.mean(artifact)),

            "max_artifact":

                int(np.max(artifact)),

        }


jpeg_visualizer = JPEGVisualizer()