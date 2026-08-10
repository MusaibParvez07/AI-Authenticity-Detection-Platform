"""
Error Level Analysis (ELA)

Measures JPEG recompression differences.
"""

from pathlib import Path
from io import BytesIO

from PIL import Image
from PIL import ImageChops
from PIL import ImageEnhance


class ErrorLevelAnalyzer:

    def analyze(
        self,
        image_path,
        quality: int = 90,
    ):

        image = Image.open(image_path).convert("RGB")

        buffer = BytesIO()

        image.save(
            buffer,
            "JPEG",
            quality=quality,
        )

        buffer.seek(0)

        compressed = Image.open(buffer)

        diff = ImageChops.difference(
            image,
            compressed,
        )

        extrema = diff.getextrema()

        max_diff = max(

            channel[1]

            for channel in extrema

        )

        if max_diff == 0:

            max_diff = 1

        scale = 255.0 / max_diff

        ela_image = ImageEnhance.Brightness(
            diff
        ).enhance(scale)

        return {

            "ela_image": ela_image,

            "max_difference": max_diff,

            "compression_quality": quality,

        }


ela_analyzer = ErrorLevelAnalyzer()