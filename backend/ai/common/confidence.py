from typing import Dict

import torch


def softmax_confidence(
    logits: torch.Tensor
) -> Dict[str, float | int]:

    probabilities = torch.softmax(
        logits,
        dim=1
    )

    confidence, prediction = torch.max(
        probabilities,
        dim=1
    )

    return {
        "prediction": int(
            prediction.item()
        ),
        "confidence": float(
            confidence.item()
        )
    }


def confidence_percentage(
    confidence: float
) -> float:

    return round(
        confidence * 100,
        2
    )


def confidence_label(
    confidence: float
) -> str:

    if confidence >= 0.95:
        return "Very High"

    if confidence >= 0.80:
        return "High"

    if confidence >= 0.60:
        return "Medium"

    return "Low"