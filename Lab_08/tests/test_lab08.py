from model import Num, Add, Sub, Mul, Div
from evaluator import evaluate
from pretty import pretty, prefix


def test_num():
    assert evaluate(Num(10)) == 10


def test_add():
    expr = Add(Num(10), Num(5))
    assert evaluate(expr) == 15


def test_sub():
    expr = Sub(Num(20), Num(8))
    assert evaluate(expr) == 12


def test_mul():
    expr = Mul(Num(3), Num(4))
    assert evaluate(expr) == 12


def test_div():
    expr = Div(Num(20), Num(5))
    assert evaluate(expr) == 4


def test_complex_expression():
    expr = Div(
        Mul(
            Add(Num(10), Num(5)),
            Sub(Num(20), Num(8)),
        ),
        Num(3),
    )

    assert evaluate(expr) == 60


def test_pretty():
    expr = Add(Num(2), Num(3))
    assert pretty(expr) == "(2 + 3)"


def test_prefix():
    expr = Mul(Num(2), Num(5))
    assert prefix(expr) == "* 2 5"
