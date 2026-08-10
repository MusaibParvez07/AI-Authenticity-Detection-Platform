"""Dataset manifest primitives used by offline evaluation only."""

from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class DatasetRecord:
    """One labelled (or deliberately unlabelled) evaluation sample."""

    path: str
    modality: str
    label: str | None = None
    source: str | None = None
    generator_family: str | None = None
    transformations: tuple[str, ...] = ()
    sha256: str | None = None
    group_id: str | None = None

    def to_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["transformations"] = list(self.transformations)
        return data


def sha256_file(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    """Return a content hash suitable for duplicate and leakage checks."""

    digest = hashlib.sha256()
    with Path(path).open("rb") as file:
        while chunk := file.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def build_record(
    path: str | Path,
    *,
    modality: str,
    label: str | None = None,
    source: str | None = None,
    generator_family: str | None = None,
    transformations: Iterable[str] = (),
    group_id: str | None = None,
) -> DatasetRecord:
    """Build a record from an existing file without guessing its metadata."""

    sample_path = Path(path)
    if not sample_path.is_file():
        raise FileNotFoundError(sample_path)
    if not modality.strip():
        raise ValueError("modality must be provided")

    content_hash = sha256_file(sample_path)
    return DatasetRecord(
        path=str(sample_path),
        modality=modality,
        label=label,
        source=source,
        generator_family=generator_family,
        transformations=tuple(transformations),
        sha256=content_hash,
        group_id=group_id or content_hash,
    )


def write_manifest(records: Iterable[DatasetRecord], path: str | Path) -> Path:
    """Write records as JSONL or CSV; the extension selects the format."""

    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    rows = [record.to_dict() for record in records]

    if destination.suffix == ".jsonl":
        with destination.open("w", encoding="utf-8") as file:
            for row in rows:
                file.write(json.dumps(row, sort_keys=True) + "\n")
        return destination

    if destination.suffix == ".csv":
        fields = list(DatasetRecord.__dataclass_fields__)
        with destination.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for row in rows:
                row["transformations"] = json.dumps(row["transformations"])
                writer.writerow(row)
        return destination

    raise ValueError("manifest path must end in .jsonl or .csv")


def load_manifest(path: str | Path) -> list[DatasetRecord]:
    """Load a JSONL or CSV manifest without inferring missing labels."""

    source = Path(path)
    if source.suffix == ".jsonl":
        with source.open(encoding="utf-8") as file:
            rows = [json.loads(line) for line in file if line.strip()]
    elif source.suffix == ".csv":
        with source.open(newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
    else:
        raise ValueError("manifest path must end in .jsonl or .csv")

    return [_record_from_row(row) for row in rows]


def _record_from_row(row: dict[str, object]) -> DatasetRecord:
    transformations = row.get("transformations") or ()
    if isinstance(transformations, str):
        transformations = json.loads(transformations) if transformations else []
    if not isinstance(transformations, list | tuple):
        raise ValueError("transformations must be a list")

    def optional(name: str) -> str | None:
        value = row.get(name)
        return str(value) if value not in (None, "") else None

    path = optional("path")
    modality = optional("modality")
    if not path or not modality:
        raise ValueError("each manifest record needs path and modality")

    return DatasetRecord(
        path=path,
        modality=modality,
        label=optional("label"),
        source=optional("source"),
        generator_family=optional("generator_family"),
        transformations=tuple(str(item) for item in transformations),
        sha256=optional("sha256"),
        group_id=optional("group_id"),
    )
