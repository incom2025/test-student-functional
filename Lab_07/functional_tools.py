from __future__ import annotations

from functools import partial, singledispatch
from typing import Any


def has_min_score(
    student: dict[str, Any],
    min_score: float,
) -> bool:
    """Перевіряє мінімальний бал студента."""
    return float(student["score"]) >= min_score


passed_student = partial(
    has_min_score,
    min_score=60.0,
)

excellent_student = partial(
    has_min_score,
    min_score=90.0,
)


@singledispatch
def format_student(value: object) -> str:
    """Універсальне форматування значення."""
    return str(value)


@format_student.register
def _(value: dict) -> str:
    name = value.get("name", "Unknown")
    score = value.get("score", 0)

    return f"{name}: {score}"


@format_student.register
def _(value: list) -> str:
    return "\n".join(
        format_student(item)
        for item in value
    )
