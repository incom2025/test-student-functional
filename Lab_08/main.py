from model import Num, Add, Sub, Mul, Div
from evaluator import evaluate
from pretty import pretty, prefix


def main() -> None:
    # (10 + 5) * (20 - 8) / 3
    expression = Div(
        Mul(
            Add(Num(10), Num(5)),
            Sub(Num(20), Num(8)),
        ),
        Num(3),
    )

    print("Laboratory work №8")
    print("Functional Programming")
    print()

    print("Expression:")
    print(pretty(expression))

    print()
    print("Prefix form:")
    print(prefix(expression))

    print()
    print("Result:")
    print(evaluate(expression))


if __name__ == "__main__":
    main()
