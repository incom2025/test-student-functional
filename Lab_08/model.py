from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Protocol, TypeAlias


@dataclass(frozen=True)
class Num:
    value: float


@dataclass(frozen=True)
class Add:
    left: "Expr"
    right: "Expr"


@dataclass(frozen=True)
class Sub:
    left: "Expr"
    right: "Expr"


@dataclass(frozen=True)
class Mul:
    left: "Expr"
    right: "Expr"


@dataclass(frozen=True)
class Div:
    left: "Expr"
    right: "Expr"


Expr: TypeAlias = Num | Add | Sub | Mul | Div

Operation: TypeAlias = str


class ExprOperation(Protocol):
    def __call__(self, expr: Expr) -> float:
        ...
