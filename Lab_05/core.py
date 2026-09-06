from __future__ import annotations

from collections import deque
from itertools import accumulate, islice
from typing import Iterable, Iterator


def fib_stream() -> Iterator[int]:
    """Infinite Fibonacci generator."""
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def take(n: int, iterable: Iterable[int]) -> list[int]:
    """Take first n values lazily."""
    if n <= 0:
        return []

    return list(islice(iterable, n))


def drop(n: int, iterable: Iterable[int]) -> Iterator[int]:
    """Skip first n values lazily."""
    if n <= 0:
        yield from iterable
        return

    iterator = iter(iterable)

    for _ in range(n):
        try:
            next(iterator)
        except StopIteration:
            return

    yield from iterator


def sliding_window(
    iterable: Iterable[int],
    size: int,
) -> Iterator[tuple[int, ...]]:
    """Yield overlapping windows lazily."""
    if size <= 0:
        raise ValueError("size must be positive")

    iterator = iter(iterable)
    window = deque(islice(iterator, size), maxlen=size)

    if len(window) < size:
        return

    yield tuple(window)

    for item in iterator:
        window.append(item)
        yield tuple(window)


def moving_average(
    iterable: Iterable[int],
    size: int,
) -> Iterator[float]:
    """Lazy moving average based on sliding windows."""
    for window in sliding_window(iterable, size):
        yield sum(window) / size


def running_sum(
    iterable: Iterable[int],
) -> Iterator[int]:
    """Lazy cumulative sums."""
    yield from accumulate(iterable)
