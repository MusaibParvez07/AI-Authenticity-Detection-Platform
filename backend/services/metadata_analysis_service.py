from PIL import Image
from PIL.ExifTags import TAGS


def analyze_metadata(file_path: str) -> dict:
    """
    Analyze image metadata (EXIF) and
    produce a simple authenticity score.
    """

    metadata = {}

    try:

        image = Image.open(file_path)

        exif = image.getexif()

        if exif:

            for tag_id, value in exif.items():

                tag = TAGS.get(tag_id, tag_id)

                metadata[tag] = str(value)

    except Exception:

        pass

    score = 0
    reasons = []

    # -------------------------
    # Camera information
    # -------------------------

    if "Make" in metadata:

        score += 15
        reasons.append(
            f"Camera Make: {metadata['Make']}"
        )

    if "Model" in metadata:

        score += 15
        reasons.append(
            f"Camera Model: {metadata['Model']}"
        )

    # -------------------------
    # Editing software
    # -------------------------

    if "Software" in metadata:

        software = metadata["Software"].lower()

        if any(
            x in software
            for x in [
                "photoshop",
                "midjourney",
                "stable",
                "sdxl",
                "gimp",
                "canva",
            ]
        ):

            score -= 25

            reasons.append(
                f"Edited using {metadata['Software']}"
            )

    # -------------------------
    # Metadata availability
    # -------------------------

    if len(metadata) == 0:

        reasons.append(
            "No EXIF metadata found."
        )

    return {

        "metadata_score": score,

        "metadata": metadata,

        "reasons": reasons,

    }