from backend.config import IMAGE_DIR

from backend.ai.image.forensics.noise import (
    noise_analyzer,
)

image = next(
    IMAGE_DIR.glob("*")
)

print(image)

result = noise_analyzer.analyze(
    image
)

print()

print("Mean Noise :", result["mean_noise"])

print("Std Noise :", result["std_noise"])

print("Median :", result["median_noise"])

print("Max :", result["max_noise"])

print("High Noise Ratio :", result["high_noise_ratio"])