from backend.ai.audio.model_loader import (
    audio_loader,
)

model = audio_loader.load()

print(type(model))

print(audio_loader.get_metadata())