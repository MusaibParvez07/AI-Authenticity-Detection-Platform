"""
Image Preprocessing

Supports:
1. Image file path
2. PIL Image
3. NumPy frame
4. HuggingFace Image Processor
"""

from pathlib import Path

import numpy as np

from PIL import Image


# =====================================================
# Load Image
# =====================================================

def _load_image(
    image,
) -> Image.Image:

    # ----------------------------------------
    # File Path
    # ----------------------------------------

    if isinstance(
        image,
        (str, Path),
    ):

        return Image.open(
            image
        ).convert("RGB")

    # ----------------------------------------
    # NumPy Array
    # ----------------------------------------

    if isinstance(
        image,
        np.ndarray,
    ):

        return Image.fromarray(
            image
        ).convert("RGB")

    # ----------------------------------------
    # PIL Image
    # ----------------------------------------

    if isinstance(
        image,
        Image.Image,
    ):

        return image.convert(
            "RGB"
        )

    raise TypeError(
        f"Unsupported image type: {type(image)}"
    )


# =====================================================
# Preprocess
# =====================================================

def preprocess_image(
    image_path,
    processor,
):

    image = _load_image(
        image_path
    )

    inputs = processor(

        images=image,

        return_tensors="pt",

    )

    # =====================================================
    # DEBUG INFORMATION
    # =====================================================

    print("\n" + "=" * 70)
    print("IMAGE PREPROCESS DEBUG")
    print("=" * 70)

    print(f"Image Size  : {image.size}")
    print(f"Image Mode  : {image.mode}")

    print("\nPROCESSOR OUTPUT")

    for key, value in inputs.items():

        if hasattr(value, "shape"):

            print(f"{key:<15}: {value.shape}")

            print(
                f"Min: {value.min().item():.6f} | "
                f"Max: {value.max().item():.6f}"
            )

    if hasattr(processor, "size"):

        print("\nProcessor Size")

        print(processor.size)

    if hasattr(processor, "image_mean"):

        print("\nImage Mean")

        print(processor.image_mean)

    if hasattr(processor, "image_std"):

        print("\nImage Std")

        print(processor.image_std)

    print("=" * 70 + "\n")

    return inputs