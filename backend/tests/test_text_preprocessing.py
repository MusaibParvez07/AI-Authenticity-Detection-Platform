from backend.ai.text.preprocessing import (
    text_preprocessor,
)

sample = """
Artificial Intelligence is changing
the future of education.
"""

tokens = text_preprocessor.preprocess(
    sample
)

print(tokens.keys())

print(tokens["input_ids"].shape)

print(tokens["attention_mask"].shape)