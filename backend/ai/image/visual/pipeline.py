"""
Professional Visual Forensics Pipeline

Generates every forensic visualization
for a single image.

Outputs:

- Face Detection
- ELA
- Noise
- JPEG Artifacts
"""

from pathlib import Path

from backend.ai.image.visual.face_visualizer import (
    face_visualizer,
)

from backend.ai.image.visual.ela_visualizer import (
    ela_visualizer,
)

from backend.ai.image.visual.noise_visualizer import (
    noise_visualizer,
)

from backend.ai.image.visual.jpeg_visualizer import (
    jpeg_visualizer,
)


class VisualPipeline:

    def generate(
        self,
        image_path: str | Path,
        output_root: str | Path = "datasets/output",
    ):

        image_path = Path(image_path)

        output_root = Path(output_root)

        image_name = image_path.stem

        # ------------------------------------------
        # Output Paths
        # ------------------------------------------

        face_output = (
            output_root
            / "faces"
            / f"{image_name}_faces.png"
        )

        ela_output = (
            output_root
            / "ela"
            / f"{image_name}_ela.png"
        )

        noise_output = (
            output_root
            / "noise"
            / f"{image_name}_noise.png"
        )

        jpeg_output = (
            output_root
            / "jpeg"
            / f"{image_name}_jpeg.png"
        )

        # ------------------------------------------
        # Generate Visualizations
        # ------------------------------------------

        print("\n" + "=" * 70)
        print("VISUAL FORENSICS PIPELINE")
        print("=" * 70)

        print("\nGenerating Face Visualization...")
        face_result = face_visualizer.visualize(
            image_path,
            face_output,
        )

        print("Done")

        print("\nGenerating ELA Visualization...")
        ela_result = ela_visualizer.visualize(
            image_path,
            ela_output,
        )

        print("Done")

        print("\nGenerating Noise Visualization...")
        noise_result = noise_visualizer.visualize(
            image_path,
            noise_output,
        )

        print("Done")

        print("\nGenerating JPEG Visualization...")
        jpeg_result = jpeg_visualizer.visualize(
            image_path,
            jpeg_output,
        )

        print("Done")

        print("\nVisual pipeline completed.")
        print("=" * 70)

        return {

            "faces": face_result,

            "ela": ela_result,

            "noise": noise_result,

            "jpeg": jpeg_result,

            "files": {

                "faces": str(face_output),

                "ela": str(ela_output),

                "noise": str(noise_output),

                "jpeg": str(jpeg_output),

            }

        }


visual_pipeline = VisualPipeline()