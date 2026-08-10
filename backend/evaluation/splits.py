"""Leakage-aware, reproducible dataset splitting for offline evaluation."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable

from sklearn.model_selection import train_test_split

from .manifest import DatasetRecord


@dataclass(frozen=True)
class DatasetSplit:
    train: tuple[DatasetRecord, ...]
    validation: tuple[DatasetRecord, ...]
    test: tuple[DatasetRecord, ...]


def split_records(
    records: Iterable[DatasetRecord],
    *,
    validation_size: float = 0.10,
    test_size: float = 0.20,
    seed: int = 42,
) -> DatasetSplit:
    """Split labelled samples by group, never allowing a group across splits.

    A group must contain samples from one class only. Mixed-label groups are
    rejected because splitting them would make the benchmark ambiguous.
    """

    records = tuple(records)
    _validate_sizes(validation_size, test_size)
    if not records:
        raise ValueError("cannot split an empty manifest")
    if any(not record.label for record in records):
        raise ValueError("all records need reviewed labels before supervised splitting")
    if any(not record.group_id for record in records):
        raise ValueError("all records need a group_id for leakage-safe splitting")

    grouped: dict[str, list[DatasetRecord]] = defaultdict(list)
    for record in records:
        grouped[record.group_id].append(record)

    group_ids: list[str] = []
    group_labels: list[str] = []
    for group_id, members in grouped.items():
        labels = {member.label for member in members}
        if len(labels) != 1:
            raise ValueError(f"group {group_id!r} contains conflicting labels")
        group_ids.append(group_id)
        group_labels.append(next(iter(labels)))

    _validate_class_support(group_labels)
    try:
        train_validation_ids, test_ids = train_test_split(
            group_ids,
            test_size=test_size,
            random_state=seed,
            stratify=group_labels,
        )
        label_by_group = dict(zip(group_ids, group_labels, strict=True))
        train_validation_labels = [label_by_group[item] for item in train_validation_ids]
        validation_relative_size = validation_size / (1 - test_size)
        train_ids, validation_ids = train_test_split(
            train_validation_ids,
            test_size=validation_relative_size,
            random_state=seed,
            stratify=train_validation_labels,
        )
    except ValueError as error:
        raise ValueError(
            "not enough labelled groups for the requested stratified split; "
            "add groups per class or adjust split sizes"
        ) from error

    membership = {
        "train": set(train_ids),
        "validation": set(validation_ids),
        "test": set(test_ids),
    }
    return DatasetSplit(
        train=tuple(record for record in records if record.group_id in membership["train"]),
        validation=tuple(
            record for record in records if record.group_id in membership["validation"]
        ),
        test=tuple(record for record in records if record.group_id in membership["test"]),
    )


def _validate_sizes(validation_size: float, test_size: float) -> None:
    if validation_size <= 0 or test_size <= 0:
        raise ValueError("validation_size and test_size must be greater than zero")
    if validation_size + test_size >= 1:
        raise ValueError("validation_size + test_size must be less than one")


def _validate_class_support(labels: list[str | None]) -> None:
    counts: dict[str | None, int] = defaultdict(int)
    for label in labels:
        counts[label] += 1
    if len(counts) < 2:
        raise ValueError("a benchmark needs at least two labels")
    if min(counts.values()) < 3:
        raise ValueError("each label needs at least three independent groups")
