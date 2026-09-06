import pytest
from dataclasses import FrozenInstanceError

from model import Item, make_order
from core import add_item, add_tag, mark_paid


def test_order_is_immutable() -> None:
    order = make_order(
        order_id=1,
        meta={"customer": "Ivan"},
    )

    with pytest.raises(FrozenInstanceError):
        order.paid = True


def test_meta_is_read_only() -> None:
    order = make_order(
        order_id=1,
        meta={"customer": "Ivan"},
    )

    with pytest.raises(TypeError):
        order.meta["customer"] = "Petro"


def test_updates_return_new_object() -> None:
    order = make_order(order_id=1)

    item = Item(
        name="Laptop",
        price=35000.0,
        quantity=1,
    )

    updated = add_item(order, item)

    assert updated is not order
    assert order.items == ()
    assert len(updated.items) == 1


def test_tag_update_does_not_mutate_original() -> None:
    order = make_order(order_id=1)

    updated = add_tag(order, "priority")

    assert updated is not order
    assert "priority" not in order.tags
    assert "priority" in updated.tags


def test_paid_update_returns_new_order() -> None:
    order = make_order(order_id=1)

    updated = mark_paid(order)

    assert updated is not order
    assert order.paid is False
    assert updated.paid is True


def test_hashability() -> None:
    item = Item(
        name="Mouse",
        price=800.0,
        quantity=1,
    )

    assert isinstance(hash(item), int)
