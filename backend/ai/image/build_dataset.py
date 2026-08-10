"""
Build Training Dataset

Extracts forensic features from every image
and creates a CSV for ML training.
"""

from pathlib import Path
import csv

from backend.ai.image.feature_extractor import (
    feature_extractor,
)


class DatasetBuilder:

    def build(
        self,
        image_dir,
        label,
        output_csv,
    ):

        image_dir = Path(image_dir)

        output_csv = Path(output_csv)

        output_csv.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        rows = []

        images = []

        for ext in [

            "*.jpg",
            "*.jpeg",
            "*.png",
            "*.JPG",
            "*.JPEG",
            "*.PNG",

        ]:

            images.extend(

                image_dir.glob(ext)

            )

        print(f"\nFound {len(images)} images")

        for i, image in enumerate(images):

            try:

                features = feature_extractor.extract(
                    image
                )

                features["label"] = label

                features["filename"] = image.name

                rows.append(features)

                print(
                    f"[{i+1}/{len(images)}] {image.name}"
                )

            except Exception as e:

                print(
                    f"Skipped {image.name}"
                )

                print(e)

        if not rows:

            print("No data extracted.")

            return

        fieldnames = rows[0].keys()

        with open(

            output_csv,

            "w",

            newline="",

        ) as file:

            writer = csv.DictWriter(

                file,

                fieldnames=fieldnames,

            )

            writer.writeheader()

            writer.writerows(rows)

        print("\nDataset Saved")

        print(output_csv)


dataset_builder = DatasetBuilder()