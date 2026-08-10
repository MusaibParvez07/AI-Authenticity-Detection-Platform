from backend.ai.audio.preprocessing import (
    audio_preprocessor,
)

audio = audio_preprocessor.preprocess(
    "datasets/audio/1ef95c059f834fc8a30f9691ed83eb80.mp3"
)

print(audio.keys())

print(audio["input_values"].shape)