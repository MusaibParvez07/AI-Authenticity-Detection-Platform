"""Non-production utilities for reproducible detector evaluation."""

from .manifest import DatasetRecord, build_record, load_manifest, write_manifest
from .metrics import BinaryEvaluation, evaluate_binary_classification
from .image_baseline import ImageBaselineResult, evaluate_image_baseline
from .splits import DatasetSplit, split_records
from .timing import LatencySummary, measure_latency

__all__ = [
    "BinaryEvaluation",
    "DatasetRecord",
    "DatasetSplit",
    "ImageBaselineResult",
    "LatencySummary",
    "build_record",
    "evaluate_binary_classification",
    "evaluate_image_baseline",
    "load_manifest",
    "measure_latency",
    "split_records",
    "write_manifest",
]
