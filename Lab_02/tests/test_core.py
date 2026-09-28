from copy import deepcopy

import pytest

from core import build_pipeline, compose, reduce_stats


DATA = [
    {"id": 1, "name": "  anna smith ", "age": 21, "city": "Delhi",
     "purchases": [100.0, 50.0]},
    {"id": 2, "name": "john brown", "age": 17, "city": "London",
     "purchases": [1000.0]},
    {"id": 3, "name": "maria green", "age": 30, "city": "London",
     "purchases": [120.0, 80.0]},
    {"id": 4, "name": "peter white", "age": 25, "city": "Delhi",
     "purchases": [90.0, 110.0]},
]


def test_top_n_and_order() -> None:
    result = build_pipeline(top_n=2, city="Delhi", factor=1.1)(DATA)
    assert [record["id"] for record in result] == [4, 3]
    assert result[0]["total"] == pytest.approx(220.0)
    assert result[1]["total"] == pytest.approx(200.0)


def test_input_is_not_mutated() -> None:
    original = deepcopy(DATA)
    build_pipeline(top_n=3, city="Delhi", factor=1.1)(DATA)
    assert DATA == original


def test_reduce_stats() -> None:
    records = [
        {"id": 1, "total": 100.0},
        {"id": 2, "total": 200.0},
        {"id": 3, "total": 300.0},
    ]
    stats = reduce_stats(records)
    assert stats["count"] == 3
    assert stats["sum_total"] == 600.0
    assert stats["avg_total"] == 200.0


def test_compose() -> None:
    double = lambda x: x * 2
    plus_one = lambda x: x + 1
    function = compose(double, plus_one)
    assert function(3) == 8
