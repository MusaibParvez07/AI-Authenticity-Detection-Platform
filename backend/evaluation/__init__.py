"""Non-production utilities for reproducible detector evaluation."""

from .manifest import DatasetRecord, build_record, load_manifest, write_manifest
from .metrics import BinaryEvaluation, evaluate_binary_classification
from .splits import DatasetSplit, split_records
from .timing import LatencySummary, measure_latency

__all__ = [
    "BinaryEvaluation",
    "DatasetRecord",
    "DatasetSplit",
    "LatencySummary",
    "build_record",
    "evaluate_binary_classification",
    "load_manifest",
    "measure_latency",
    "split_records",
    "write_manifest",
]
