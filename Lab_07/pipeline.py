from __future__ import annotations

from functools import reduce
from typing import Any, Callable, Iterable


def pipeline(
    steps: Iterable[Callable[[Any], Any]],
    value: Any,
) -> Any:
    """
    Послідовно застосовує всі функції steps до value.
    Реалізація виконана через functools.reduce.
    """
    return reduce(
        lambda current, func: func(current),
        steps,
        value,
    )


if __name__ == "__main__":
    result = pipeline(
        [
            lambda x: x + 2,
            lambda x: x * 3,
            str,
        ],
        5,
    )

    print(result)
