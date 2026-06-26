import torch
from torchvision import transforms
from PIL import Image


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


def image_to_tensor(image_path: str):

    image = Image.open(image_path)

    image = image.convert("RGB")

    tensor = transform(image)

    tensor = tensor.unsqueeze(0)

    return tensor