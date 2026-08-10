from backend.ai.text.inference import (
    text_inference,
)

sample = """
Artificial Intelligence
is changing education.
"""

result = text_inference.predict(
    sample
)

print(result)