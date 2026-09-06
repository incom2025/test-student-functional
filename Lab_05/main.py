from itertools import islice, takewhile, dropwhile

from core import (
    fib_stream,
    moving_average,
    running_sum,
    sliding_window,
    take,
)


def main() -> None:
    print("Laboratory work №5")
    print("Variant 1")
    print("Generators, iterators and lazy evaluation")
    print()

    # 1. Infinite Fibonacci generator + islice
    first_15 = list(islice(fib_stream(), 15))
    print("First 15 Fibonacci numbers:")
    print(first_15)
    print()

    # 2. Our lazy take()
    first_10 = take(10, fib_stream())
    print("First 10 Fibonacci numbers:")
    print(first_10)
    print()

    # 3. takewhile
    less_than_100 = list(
        takewhile(lambda x: x < 100, fib_stream())
    )
    print("Fibonacci numbers < 100:")
    print(less_than_100)
    print()

    # 4. dropwhile + islice
    greater_or_equal_20 = list(
        islice(
            dropwhile(lambda x: x < 20, fib_stream()),
            8,
        )
    )
    print("8 Fibonacci numbers starting from >= 20:")
    print(greater_or_equal_20)
    print()

    # 5. Sliding windows
    windows = list(
        sliding_window(range(1, 8), 3)
    )
    print("Sliding windows:")
    print(windows)
    print()

    # 6. Moving average
    averages = list(
        moving_average(range(1, 8), 3)
    )
    print("Moving averages:")
    print(averages)
    print()

    # 7. Lazy running sum
    sums = list(
        running_sum(range(1, 8))
    )
    print("Running sums:")
    print(sums)


if __name__ == "__main__":
    main()
