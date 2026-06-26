from PIL import Image


def preprocess_image(
    image_path: str
):

    image = Image.open(image_path)

    image = image.convert("RGB")

    image = image.resize(
        (224, 224)
    )

    return image