"""
Professional Noise Visualizer

Creates a grayscale noise map
using Gaussian Blur subtraction.
"""

from pathlib import Path

import cv2
import numpy as np


class NoiseVisualizer:

    def visualize(
        self,
        image_path: str | Path,
        output_path: str | Path,
    ):

        image_path = Path(image_path)
        output_path = Path(output_path)

        image = cv2.imread(
            str(image_path),
            cv2.IMREAD_GRAYSCALE,
        )

        if image is None:

            raise FileNotFoundError(image_path)

        # ---------------------------------------
        # Blur Image
        # ---------------------------------------

        blurred = cv2.GaussianBlur(

            image,

            (5, 5),

            0,

        )

        # ---------------------------------------
        # Noise Map
        # ---------------------------------------

        noise = cv2.absdiff(

            image,

            blurred,

        )

        # ---------------------------------------
        # Normalize
        # ---------------------------------------

        noise = cv2.normalize(

            noise,

            None,

            0,

            255,

            cv2.NORM_MINMAX,

        )

        output_path.parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        cv2.imwrite(

            str(output_path),

            noise,

        )

        return {

            "saved_to":

                str(output_path),

            "mean_noise":

                float(np.mean(noise)),

            "max_noise":

                int(np.max(noise)),

            "std_noise":

                float(np.std(noise)),

        }


noise_visualizer = NoiseVisualizer()