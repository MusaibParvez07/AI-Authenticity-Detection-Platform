"""Metric calculation independent from application inference code."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_recall_fscore_support,
    roc_auc_score,
)


@dataclass(frozen=True)
class BinaryEvaluation:
    accuracy: float
    precision: float
    recall: float
    f1: float
    roc_auc: float | None
    confusion_matrix: tuple[tuple[int, int], tuple[int, int]]
    false_positive_rate: float | None
    false_negative_rate: float | None
    positive_label: str
    negative_label: str


def evaluate_binary_classification(
    y_true: Iterable[str],
    y_pred: Iterable[str],
    *,
    scores: Sequence[float] | None = None,
    positive_label: str = "fake",
    negative_label: str = "real",
) -> BinaryEvaluation:
    """Evaluate supplied labels/predictions without running a model.

    ``scores`` must be the probability or score for ``positive_label``. ROC-AUC
    is returned only when scores and both ground-truth classes are available.
    """

    truth = list(y_true)
    predicted = list(y_pred)
    if not truth or len(truth) != len(predicted):
        raise ValueError("y_true and y_pred must be non-empty and equally sized")
    allowed = {positive_label, negative_label}
    if not set(truth).union(predicted).issubset(allowed):
        raise ValueError("binary evaluation received labels outside the declared classes")
    if scores is not None and len(scores) != len(truth):
        raise ValueError("scores must have one value per ground-truth label")

    precision, recall, f1, _ = precision_recall_fscore_support(
        truth,
        predicted,
        average="binary",
        pos_label=positive_label,
        zero_division=0,
    )
    matrix = confusion_matrix(truth, predicted, labels=[negative_label, positive_label])
    tn, fp, fn, tp = (int(value) for value in matrix.ravel())

    roc_auc = None
    if scores is not None and len(set(truth)) == 2:
        roc_auc = float(roc_auc_score([item == positive_label for item in truth], scores))

    return BinaryEvaluation(
        accuracy=float(accuracy_score(truth, predicted)),
        precision=float(precision),
        recall=float(recall),
        f1=float(f1),
        roc_auc=roc_auc,
        confusion_matrix=((tn, fp), (fn, tp)),
        false_positive_rate=fp / (fp + tn) if fp + tn else None,
        false_negative_rate=fn / (fn + tp) if fn + tp else None,
        positive_label=positive_label,
        negative_label=negative_label,
    )
