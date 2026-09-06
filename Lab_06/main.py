from closures import make_call_counter, make_multiplier
from decorators import calculate_sum, fibonacci


def main() -> None:
    print("=== Laboratory work №6 ===")
    print("Closures and decorators")

    # -----------------------------
    # Closure: counter
    # -----------------------------
    print("\n1. Counter closure")

    counter = make_call_counter()

    print(counter())
    print(counter())
    print(counter())

    # -----------------------------
    # Closure: multiplier
    # -----------------------------
    print("\n2. Multiplier closure")

    double = make_multiplier(2)
    triple = make_multiplier(3)

    print("double(10) =", double(10))
    print("triple(10) =", triple(10))

    # -----------------------------
    # Timing decorator
    # -----------------------------
    print("\n3. Timing decorator")

    result = calculate_sum(100000)

    print("sum =", result)

    # -----------------------------
    # Cache decorator
    # -----------------------------
    print("\n4. TTL cache")

    print("fibonacci(10) =", fibonacci(10))
    print("fibonacci(10) cached =", fibonacci(10))

    print("\nLaboratory work completed successfully.")


if __name__ == "__main__":
    main()
