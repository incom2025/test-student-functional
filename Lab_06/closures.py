from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def make_call_counter() -> Callable[[], int]:
    """Closure that stores the number of calls."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def make_multiplier(factor: float) -> Callable[[float], float]:
    """Create a function that multiplies a value by factor."""

    def multiply(value: float) -> float:
        return value * factor

    return multiply


def make_threshold_checker(
    threshold: float,
) -> Callable[[float], bool]:
    """Create a predicate with a captured threshold."""

    def check(value: float) -> bool:
        return value >= threshold

    return check


def make_named_counter(
    name: str,
) -> Callable[[], tuple[str, int]]:
    """Stateful closure with nonlocal state."""
    calls = 0

    def count_calls() -> tuple[str, int]:
        nonlocal calls
        calls += 1
        return name, calls

    return count_calls
