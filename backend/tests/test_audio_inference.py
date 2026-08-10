from pathlib import Path

from backend.ai.audio.inference import (
    audio_inference,
    
)

audio_dir = Path(
    "datasets/audio"
)

audio_file = next(
    audio_dir.glob("*.mp3")
)

result = audio_inference.predict(
    str(audio_file)
)

print(result)