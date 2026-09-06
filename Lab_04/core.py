from __future__ import annotations

from functools import lru_cache


def tribonacci_recursive(n: int) -> int:
    """Recursive Tribonacci implementation."""
    if n == 0:
        return 0
    if n in (1, 2):
        return 1

    return (
        tribonacci_recursive(n - 1)
        + tribonacci_recursive(n - 2)
        + tribonacci_recursive(n - 3)
    )


@lru_cache(maxsize=None)
def tribonacci_cached(n: int) -> int:
    """Memoized recursive Tribonacci implementation."""
    if n == 0:
        return 0
    if n in (1, 2):
        return 1

    return (
        tribonacci_cached(n - 1)
        + tribonacci_cached(n - 2)
        + tribonacci_cached(n - 3)
    )


def tribonacci_iterative(n: int) -> int:
    """Iterative Tribonacci implementation."""
    if n == 0:
        return 0
    if n in (1, 2):
        return 1

    a, b, c = 0, 1, 1

    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c


def reset_cache() -> None:
    tribonacci_cached.cache_clear()


def cache_statistics():
    return tribonacci_cached.cache_info()
