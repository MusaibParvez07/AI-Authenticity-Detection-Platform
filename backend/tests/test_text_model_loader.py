from backend.ai.text.model_loader import (
    text_loader,
)

model = text_loader.load()

print(type(model))

print(text_loader.get_metadata())