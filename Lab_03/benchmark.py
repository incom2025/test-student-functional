from time import perf_counter

from model import Item, make_order
from core import add_item


def benchmark_updates(iterations: int = 1000) -> float:
    item = Item(
        name="Test",
        price=100.0,
        quantity=1,
    )

    start = perf_counter()

    for index in range(iterations):
        order = make_order(order_id=index)
        add_item(order, item)

    end = perf_counter()

    return end - start


def main() -> None:
    elapsed = benchmark_updates()

    print(
        f"Immutable update benchmark: "
        f"{elapsed:.6f} seconds"
    )


if __name__ == "__main__":
    main()
