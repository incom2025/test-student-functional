from closures import make_counter, make_multiplier
from decorators import calculate_sum, fibonacci


def test_counter() -> None:
    counter = make_counter()

    assert counter() == 1
    assert counter() == 2
    assert counter() == 3


def test_independent_counters() -> None:
    first = make_counter()
    second = make_counter()

    assert first() == 1
    assert first() == 2
    assert second() == 1


def test_multiplier() -> None:
    double = make_multiplier(2)
    triple = make_multiplier(3)

    assert double(5) == 10
    assert triple(5) == 15


def test_calculate_sum() -> None:
    assert calculate_sum(10) == 45
    assert calculate_sum(100) == 4950


def test_fibonacci() -> None:
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_fibonacci_cache_clear() -> None:
    assert fibonacci(10) == 55

    fibonacci.cache_clear()

    assert fibonacci(10) == 55
