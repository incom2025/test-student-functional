from __future__ import annotations

from functools import reduce
from typing import Any, Callable


def pipeline(
    *steps: Callable[[Any], Any],
) -> Callable[[Any], Any]:
    """
    Створює функціональний конвеєр через functools.reduce.

    Приклад:
        process = pipeline(
            normalize,
            validate,
            transform,
        )

        result = process(value)
    """

    def apply(value: Any) -> Any:
        return reduce(
            lambda current, func: func(current),
            steps,
            value,
        )

    return apply


if __name__ == "__main__":
    process = pipeline(
        lambda x: x + 2,
        lambda x: x * 3,
        str,
    )

    print(process(5))
