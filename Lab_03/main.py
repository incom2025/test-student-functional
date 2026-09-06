from model import Item, make_order
from core import (
    add_item,
    remove_item,
    add_tag,
    remove_tag,
    mark_paid,
    update_meta,
)


def main() -> None:
    order = make_order(
        order_id=1,
        items=(),
        tags=frozenset(),
        meta={
            "customer": "Іван Петренко",
        },
        paid=False,
    )

    print("Початкове замовлення:")
    print(order)

    laptop = Item(
        name="Laptop",
        price=35000.0,
        quantity=1,
    )

    mouse = Item(
        name="Mouse",
        price=800.0,
        quantity=2,
    )

    order = add_item(order, laptop)
    order = add_item(order, mouse)

    print("\nПісля додавання товарів:")
    print(order)

    order = add_tag(order, "priority")
    order = add_tag(order, "online")

    print("\nПісля додавання тегів:")
    print(order)

    order = update_meta(
        order,
        "delivery",
        "Nova Poshta",
    )

    print("\nПісля оновлення meta:")
    print(order)

    order = mark_paid(order)

    print("\nПісля оплати:")
    print(order)

    order = remove_item(
        order,
        "Mouse",
    )

    order = remove_tag(
        order,
        "priority",
    )

    print("\nФінальний стан:")
    print(order)


if __name__ == "__main__":
    main()
