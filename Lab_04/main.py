from time import perf_counter

from core import (
    tribonacci_recursive,
    tribonacci_cached,
    tribonacci_iterative,
    reset_cache,
    cache_statistics,
)


def main() -> None:
    n = 25

    print(f"Tribonacci for n = {n}")

    start = perf_counter()
    recursive_result = tribonacci_recursive(n)
    recursive_time = perf_counter() - start

    reset_cache()

    start = perf_counter()
    cached_result = tribonacci_cached(n)
    cached_time = perf_counter() - start

    start = perf_counter()
    iterative_result = tribonacci_iterative(n)
    iterative_time = perf_counter() - start

    print("\nResults:")
    print("Recursive:", recursive_result)
    print("Memoized :", cached_result)
    print("Iterative:", iterative_result)

    print("\nPerformance:")
    print(f"Recursive time: {recursive_time:.6f} s")
    print(f"Memoized time : {cached_time:.6f} s")
    print(f"Iterative time: {iterative_time:.6f} s")

    print("\nCache statistics:")
    print(cache_statistics())


if __name__ == "__main__":
    main()
