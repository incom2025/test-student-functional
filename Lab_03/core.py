from __future__ import annotations

from dataclasses import replace

from model import Item, Order


def add_item(order: Order, item: Item) -> Order:
    """Return a new order with an added item."""
    return replace(
        order,
        items=order.items + (item,),
    )


def remove_item(order: Order, item_name: str) -> Order:
    """Return a new order without items with the given name."""
    new_items = tuple(
        item
        for item in order.items
        if item.name != item_name
    )

    return replace(
        order,
        items=new_items,
    )


def add_tag(order: Order, tag: str) -> Order:
    """Return a new order with an added tag."""
    return replace(
        order,
        tags=order.tags | frozenset({tag}),
    )


def remove_tag(order: Order, tag: str) -> Order:
    """Return a new order without the given tag."""
    return replace(
        order,
        tags=order.tags - frozenset({tag}),
    )


def mark_paid(order: Order) -> Order:
    """Return a new paid order."""
    return replace(
        order,
        paid=True,
    )


def update_meta(order: Order, key: str, value: str) -> Order:
    """Return a new order with updated metadata."""
    new_meta = dict(order.meta)
    new_meta[key] = value

    return replace(
        order,
        meta=new_meta,
    )
