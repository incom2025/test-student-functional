from __future__ import annotations

import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar, Any

P = ParamSpec("P")
R = TypeVar("R")


def timed(func: Callable[P, R]) -> Callable[P, R]:
    """Decorator that measures function execution time."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        print(f"{func.__name__}: {elapsed:.6f} s")
        return result

    return wrapper


def ttl_cache(
    ttl: float = 5.0,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Simple cache decorator with TTL and cache invalidation."""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        cache: dict[Any, tuple[float, R]] = {}

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            key = (args, tuple(sorted(kwargs.items())))
            now = time.monotonic()

            if key in cache:
                created_at, value = cache[key]

                if now - created_at < ttl:
                    return value

                del cache[key]

            result = func(*args, **kwargs)
            cache[key] = (now, result)

            return result

        def cache_clear() -> None:
            """Clear all cached values."""
            cache.clear()

        def cache_invalidate(
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> None:
            """Remove one cached value."""
            key = (args, tuple(sorted(kwargs.items())))
            cache.pop(key, None)

        wrapper.cache_clear = cache_clear  # type: ignore[attr-defined]
        wrapper.cache_invalidate = cache_invalidate  # type: ignore[attr-defined]

        return wrapper

    return decorator


def inject(
    dependency: object,
) -> Callable[[Callable[..., R]], Callable[..., R]]:
    """Simple dependency-injection decorator."""

    def decorator(func: Callable[..., R]) -> Callable[..., R]:

        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> R:
            return func(dependency, *args, **kwargs)

        return wrapper

    return decorator


@timed
def calculate_sum(n: int) -> int:
    """Example function for the timing decorator."""
    return sum(range(n))


@ttl_cache(ttl=10.0)
def fibonacci(n: int) -> int:
    """Calculate Fibonacci number recursively."""
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
