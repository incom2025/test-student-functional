from __future__ import annotations

from model import Add, Div, Expr, Mul, Num, Sub


def evaluate(expr: Expr) -> float:
    """Evaluate an arithmetic expression using pattern matching."""

    match expr:
        case Num(value):
            return value

        case Add(left, right):
            return evaluate(left) + evaluate(right)

        case Sub(left, right):
            return evaluate(left) - evaluate(right)

        case Mul(left, right):
            return evaluate(left) * evaluate(right)

        case Div(left, right):
            denominator = evaluate(right)

            if denominator == 0:
                raise ZeroDivisionError("division by zero")

            return evaluate(left) / denominator

    raise TypeError(f"Unsupported expression: {expr!r}")


def is_constant(expr: Expr) -> bool:
    """Check whether the expression consists only of constants."""

    match expr:
        case Num():
            return True

        case Add(left, right):
            return is_constant(left) and is_constant(right)

        case Sub(left, right):
            return is_constant(left) and is_constant(right)

        case Mul(left, right):
            return is_constant(left) and is_constant(right)

        case Div(left, right):
            return is_constant(left) and is_constant(right)

    return False


def contains_zero(expr: Expr) -> bool:
    """Check whether the expression tree contains Num(0)."""

    match expr:
        case Num(value):
            return value == 0

        case Add(left, right) | Sub(left, right) | Mul(left, right) | Div(left, right):
            return contains_zero(left) or contains_zero(right)

    return False


def fold_constants(expr: Expr) -> Expr:
    """Fold constant subexpressions."""

    match expr:
        case Num():
            return expr

        case Add(left, right):
            left_folded = fold_constants(left)
            right_folded = fold_constants(right)
            return Num(
                evaluate(Add(left_folded, right_folded))
            )

        case Sub(left, right):
            left_folded = fold_constants(left)
            right_folded = fold_constants(right)
            return Num(
                evaluate(Sub(left_folded, right_folded))
            )

        case Mul(left, right):
            left_folded = fold_constants(left)
            right_folded = fold_constants(right)
            return Num(
                evaluate(Mul(left_folded, right_folded))
            )

        case Div(left, right):
            left_folded = fold_constants(left)
            right_folded = fold_constants(right)
            return Num(
                evaluate(Div(left_folded, right_folded))
            )

    raise TypeError(f"Unsupported expression: {expr!r}")
