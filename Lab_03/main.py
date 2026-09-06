from model import Item, Order
from core import (
    add_item,
    remove_item,
    add_tag,
    remove_tag,
    mark_paid,
    update_meta,
)


def main() -> None:
    # Початкове замовлення
    order = Order(
        number=1,
        customer="Іван Петренко",
        items=(),
        tags=frozenset(),
        paid=False,
        meta={},
    )

    print("Початкове замовлення:")
    print(order)

    # Створюємо товари
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

    # Додаємо товари
    order = add_item(order, laptop)
    order = add_item(order, mouse)

    print("\nПісля додавання товарів:")
    print(order)

    # Додаємо теги
    order = add_tag(order, "priority")
    order = add_tag(order, "online")

    print("\nПісля додавання тегів:")
    print(order)

    # Оновлюємо метадані
    order = update_meta(
        order,
        "delivery",
        "Nova Poshta",
    )

    print("\nПісля оновлення meta:")
    print(order)

    # Позначаємо замовлення оплаченим
    order = mark_paid(order)

    print("\nПісля оплати:")
    print(order)

    # Видаляємо товар
    order = remove_item(order, "Mouse")

    # Видаляємо тег
    order = remove_tag(order, "priority")

    print("\nФінальний стан:")
    print(order)


if __name__ == "__main__":
    main()
