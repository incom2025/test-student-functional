from __future__ import annotations

from dataclasses import replace
from types import MappingProxyType

from model import Item, Order


def add_item(order: Order, item: Item) -> Order:
    return replace(
        order,
        items=order.items + (item,),
    )


def remove_item(order: Order, item_name: str) -> Order:
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
    return replace(
        order,
        tags=order.tags | frozenset({tag}),
    )


def remove_tag(order: Order, tag: str) -> Order:
    return replace(
        order,
        tags=order.tags - frozenset({tag}),
    )


def mark_paid(order: Order) -> Order:
    return replace(
        order,
        paid=True,
    )


def update_meta(
    order: Order,
    key: str,
    value: str,
) -> Order:
    new_meta = dict(order.meta)
    new_meta[key] = value

    return replace(
        order,
        meta=MappingProxyType(dict(new_meta)),
    )
