from backend.ai.image.model_loader import (
    image_loader
)

model = image_loader.load()

print(model)

print()

print(
    image_loader.get_metadata()
)
