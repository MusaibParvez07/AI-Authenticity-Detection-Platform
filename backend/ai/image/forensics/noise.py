"""
Noise Analysis

Estimate sensor noise consistency.
"""

from pathlib import Path

import cv2
import numpy as np


class NoiseAnalyzer:

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

        # ----------------------------------------
        # Estimate Noise
        # ----------------------------------------

        blur = cv2.GaussianBlur(
            gray,
            (5, 5),
            0,
        )

        noise = cv2.absdiff(
            gray,
            blur,
        )

        noise = noise.astype(np.float32)

        mean_noise = float(
            np.mean(noise)
        )

        std_noise = float(
            np.std(noise)
        )

        max_noise = float(
            np.max(noise)
        )

        median_noise = float(
            np.median(noise)
        )

        high_noise_ratio = float(

            np.sum(noise > 25)

            /

            noise.size

        )

        return {

            "mean_noise": mean_noise,

            "std_noise": std_noise,

            "median_noise": median_noise,

            "max_noise": max_noise,

            "high_noise_ratio": high_noise_ratio,

            "noise_map": noise,

        }


noise_analyzer = NoiseAnalyzer()