from __future__ import annotations

from typing import Callable


Order = dict[str, object]
DiscountPolicy = Callable[[float], float]
TaxPolicy = Callable[[float], float]


def is_paid_order(order: Order) -> bool:
    return bool(order.get("paid", False))


def calculate_subtotal(order: Order) -> float:
    price = float(order.get("price", 0.0))
    quantity = int(order.get("qty", 0))
    return price * quantity


def standard_discount(subtotal: float) -> float:
    if subtotal >= 1000:
        return subtotal * 0.10
    return 0.0


def standard_tax(amount: float) -> float:
    return amount * 0.20


def process_order(
    order: Order,
    discount_policy: DiscountPolicy,
    tax_policy: TaxPolicy,
) -> dict[str, object]:
    subtotal = calculate_subtotal(order)

    discount = discount_policy(subtotal)

    taxable_amount = subtotal - discount
    tax = tax_policy(taxable_amount)

    total = taxable_amount + tax

    return {
        "id": order.get("id"),
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total,
    }


def process_paid_orders(
    orders: list[Order],
    discount_policy: DiscountPolicy,
    tax_policy: TaxPolicy,
) -> list[dict[str, object]]:
    paid_orders = filter(is_paid_order, orders)

    return [
        process_order(
            order,
            discount_policy,
            tax_policy,
        )
        for order in paid_orders
    ]


def calculate_revenue(
    processed_orders: list[dict[str, object]],
) -> float:
    return sum(
        float(order["total"])
        for order in processed_orders
    )


def main() -> None:
    orders: list[Order] = [
        {
            "id": 1,
            "paid": True,
            "price": 400.0,
            "qty": 3,
        },
        {
            "id": 2,
            "paid": False,
            "price": 250.0,
            "qty": 2,
        },
        {
            "id": 3,
            "paid": True,
            "price": 150.0,
            "qty": 4,
        },
    ]

    result = process_paid_orders(
        orders,
        standard_discount,
        standard_tax,
    )

    revenue = calculate_revenue(result)

    print("Processed orders:")
    for order in result:
        print(order)

    print(f"Revenue: {revenue:.2f}")


if __name__ == "__main__":
    main()
