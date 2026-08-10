"""
Professional Error Level Analysis Visualizer

Creates an Error Level Analysis (ELA) visualization
and saves it as an image.
"""

from pathlib import Path
from PIL import Image, ImageChops, ImageEnhance


class ELAVisualizer:

    def visualize(
        self,
        image_path: str | Path,
        output_path: str | Path,
        quality: int = 90,
    ):

        image_path = Path(image_path)
        output_path = Path(output_path)

        original = Image.open(
            image_path
        ).convert("RGB")

        temp_path = output_path.parent / "_ela_temp.jpg"

        original.save(
            temp_path,
            "JPEG",
            quality=quality,
        )

        compressed = Image.open(
            temp_path
        )

        ela_image = ImageChops.difference(
            original,
            compressed,
        )

        extrema = ela_image.getextrema()

        max_difference = max(

            ex[1]

            for ex in extrema

        )

        if max_difference == 0:

            max_difference = 1

        scale = 255.0 / max_difference

        ela_image = ImageEnhance.Brightness(
            ela_image
        ).enhance(scale)

        output_path.parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        ela_image.save(output_path)

        if temp_path.exists():

            temp_path.unlink()

        return {

            "saved_to":

                str(output_path),

            "max_difference":

                max_difference,

            "quality":

                quality,

        }


ela_visualizer = ELAVisualizer()