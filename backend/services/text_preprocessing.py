from backend.models.text_models.roberta_detector import (
    TextDetector
)

_detector = TextDetector()


def preprocess_text(
    text: str
):

    encoded = _detector.tokenizer(
        text,
        padding="max_length",
        truncation=True,
        max_length=256,
        return_tensors="pt"
    )

    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"]
    }