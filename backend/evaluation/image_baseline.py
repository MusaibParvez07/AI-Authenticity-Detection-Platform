"""Offline baseline evaluation for the existing image classifier.

This module accepts a predictor callable, never creates labels, and does not
alter production inference, data, model weights, or image-pipeline behavior.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, median
from time import perf_counter
from typing import Callable, Iterable, Mapping

from .manifest import DatasetRecord
from .metrics import BinaryEvaluation, evaluate_binary_classification
from .timing import LatencySummary


ImagePredictor = Callable[[str], Mapping[str, object]]


@dataclass(frozen=True)
class ImageBaselineResult:
    """Metrics produced from a reviewed labelled image manifest."""

    metrics: BinaryEvaluation
    latency: LatencySummary
    records_evaluated: int
    predictions: tuple[str, ...]
    fake_scores: tuple[float, ...]


def evaluate_image_baseline(
    records: Iterable[DatasetRecord],
    predictor: ImagePredictor,
) -> ImageBaselineResult:
    """Evaluate an image predictor using reviewed ``real``/``fake`` records.

    The existing image inference result carries the winning-class confidence.
    As the baseline classifier is binary, this derives a fake score as the
    confidence for fake predictions and ``1 - confidence`` for real ones.
    That conversion is evaluation-only; it never calibrates or changes the
    production confidence returned by the application.
    """

    samples = tuple(records)
    _validate_image_records(samples)

    truths: list[str] = []
    predictions: list[str] = []
    fake_scores: list[float] = []
    latency_samples: list[float] = []

    for record in samples:
        started = perf_counter()
        result = predictor(record.path)
        latency_samples.append((perf_counter() - started) * 1000)

        prediction = str(result.get("prediction", "")).lower()
        if prediction not in {"real", "fake"}:
            raise ValueError("image predictor must return a normalized real/fake prediction")
        try:
            confidence = float(result["confidence"])
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError("image predictor must return a numeric confidence") from error
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("image predictor confidence must be within [0, 1]")

        truths.append(record.label or "")
        predictions.append(prediction)
        fake_scores.append(confidence if prediction == "fake" else 1.0 - confidence)

    values = tuple(latency_samples)
    return ImageBaselineResult(
        metrics=evaluate_binary_classification(truths, predictions, scores=fake_scores),
        latency=LatencySummary(
            samples_ms=values,
            mean_ms=mean(values),
            median_ms=median(values),
            min_ms=min(values),
            max_ms=max(values),
        ),
        records_evaluated=len(samples),
        predictions=tuple(predictions),
        fake_scores=tuple(fake_scores),
    )


def _validate_image_records(records: tuple[DatasetRecord, ...]) -> None:
    if not records:
        raise ValueError("an image baseline needs at least one reviewed record")
    for record in records:
        if record.modality != "image":
            raise ValueError("image baseline accepts only image records")
        if record.label not in {"real", "fake"}:
            raise ValueError("image baseline requires reviewed real/fake labels")
