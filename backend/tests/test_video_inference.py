from pathlib import Path

from backend.ai.video.inference import (
    video_inference,
)

video_dir = Path(
    "datasets/video"
)

video = next(
    video_dir.glob("*.mp4")
)

result = video_inference.predict(
    str(video)
)

print(result)