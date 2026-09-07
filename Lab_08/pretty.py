from __future__ import annotations

from model import Add, Div, Expr, Mul, Num, Sub


def pretty(expr: Expr) -> str:
    """Convert an expression tree to a readable string."""

    match expr:
        case Num(value):
            return str(value)

        case Add(left, right):
            return f"({pretty(left)} + {pretty(right)})"

        case Sub(left, right):
            return f"({pretty(left)} - {pretty(right)})"

        case Mul(left, right):
            return f"({pretty(left)} * {pretty(right)})"

        case Div(left, right):
            return f"({pretty(left)} / {pretty(right)})"

    raise TypeError(f"Unsupported expression: {expr!r}")


def prefix(expr: Expr) -> str:
    """Convert an expression to prefix notation."""

    match expr:
        case Num(value):
            return str(value)

        case Add(left, right):
            return f"+ {prefix(left)} {prefix(right)}"

        case Sub(left, right):
            return f"- {prefix(left)} {prefix(right)}"

        case Mul(left, right):
            return f"* {prefix(left)} {prefix(right)}"

        case Div(left, right):
            return f"/ {prefix(left)} {prefix(right)}"

    raise TypeError(f"Unsupported expression: {expr!r}")
