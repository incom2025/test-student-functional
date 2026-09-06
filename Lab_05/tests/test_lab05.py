from itertools import islice

from core import (
    fib_stream,
    moving_average,
    running_sum,
    sliding_window,
    take,
)


def test_fib_stream_first_values():
    result = list(islice(fib_stream(), 10))

    assert result == [
        0, 1, 1, 2, 3,
        5, 8, 13, 21, 34,
    ]


def test_take():
    result = take(5, fib_stream())

    assert result == [0, 1, 1, 2, 3]


def test_sliding_window():
    result = list(sliding_window([1, 2, 3, 4, 5], 3))

    assert result == [
        (1, 2, 3),
        (2, 3, 4),
        (3, 4, 5),
    ]


def test_moving_average():
    result = list(moving_average([1, 2, 3, 4, 5], 3))

    assert result == [
        2.0,
        3.0,
        4.0,
    ]


def test_running_sum():
    result = list(running_sum([1, 2, 3, 4]))

    assert result == [
        1,
        3,
        6,
        10,
    ]


def test_generator_is_lazy():
    stream = fib_stream()

    assert next(stream) == 0
    assert next(stream) == 1
    assert next(stream) == 1


def test_invalid_window_size():
    try:
        list(sliding_window([1, 2, 3], 0))
    except ValueError:
        assert True
    else:
        assert False
