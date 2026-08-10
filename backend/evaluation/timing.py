"""Small offline latency measurement helper."""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, median
from time import perf_counter
from typing import Callable, TypeVar


T = TypeVar("T")


@dataclass(frozen=True)
class LatencySummary:
    samples_ms: tuple[float, ...]
    mean_ms: float
    median_ms: float
    min_ms: float
    max_ms: float


def measure_latency(
    operation: Callable[[], T],
    *,
    repeats: int = 5,
    warmup: int = 1,
) -> LatencySummary:
    """Measure a no-argument operation; callers own model loading and inputs."""

    if repeats < 1 or warmup < 0:
        raise ValueError("repeats must be at least one and warmup cannot be negative")
    for _ in range(warmup):
        operation()

    samples = []
    for _ in range(repeats):
        started = perf_counter()
        operation()
        samples.append((perf_counter() - started) * 1000)

    values = tuple(samples)
    return LatencySummary(
        samples_ms=values,
        mean_ms=mean(values),
        median_ms=median(values),
        min_ms=min(values),
        max_ms=max(values),
    )
