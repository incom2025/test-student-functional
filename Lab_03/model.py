from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping


@dataclass(frozen=True, slots=True)
class Item:
    name: str
    price: float
    quantity: int


@dataclass(frozen=True, slots=True)
class Order:
    order_id: int
    items: tuple[Item, ...]
    tags: frozenset[str]
    meta: Mapping[str, str]
    paid: bool = False


def make_order(
    order_id: int,
    items: tuple[Item, ...] = (),
    tags: frozenset[str] = frozenset(),
    meta: dict[str, str] | None = None,
    paid: bool = False,
) -> Order:
    safe_meta = MappingProxyType(
        dict(meta or {})
    )

    return Order(
        order_id=order_id,
        items=items,
        tags=tags,
        meta=safe_meta,
        paid=paid,
    )


def subtotal(order: Order) -> float:
    return sum(
        item.price * item.quantity
        for item in order.items
    )
