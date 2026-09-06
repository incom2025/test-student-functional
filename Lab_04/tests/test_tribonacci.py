import pytest

from core import (
    tribonacci_recursive,
    tribonacci_cached,
    tribonacci_iterative,
    reset_cache,
    cache_statistics,
)


def test_base_values() -> None:
    assert tribonacci_recursive(0) == 0
    assert tribonacci_recursive(1) == 1
    assert tribonacci_recursive(2) == 1


def test_same_results() -> None:
    for n in range(15):
        r1 = tribonacci_recursive(n)
        r2 = tribonacci_cached(n)
        r3 = tribonacci_iterative(n)

        assert r1 == r2 == r3


def test_iterative_values() -> None:
    assert tribonacci_iterative(3) == 2
    assert tribonacci_iterative(4) == 4
    assert tribonacci_iterative(5) == 7
    assert tribonacci_iterative(6) == 13


def test_cache() -> None:
    reset_cache()

    tribonacci_cached(15)
    stats = cache_statistics()

    assert stats is not None
    assert stats.misses > 0


def test_cache_clear() -> None:
    tribonacci_cached(10)

    reset_cache()
    stats = cache_statistics()

    assert stats.currsize == 0
