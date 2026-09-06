from __future__ import annotations

from functools import reduce
from typing import Callable, Iterable, TypedDict


class Client(TypedDict):
    name: str
    age: int
    city: str
    purchases: list[float]


class ClientResult(TypedDict):
    name: str
    age: int
    city: str
    total: float


Transform = Callable[[Iterable[Client]], Iterable[Client]]
ResultTransform = Callable[[Iterable[ClientResult]], Iterable[ClientResult]]


def is_adult(client: Client) -> bool:
    return client["age"] >= 18


def calculate_total(client: Client) -> ClientResult:
    total = sum(client["purchases"])

    return {
        "name": client["name"],
        "age": client["age"],
        "city": client["city"],
        "total": total,
    }


def apply_city_factor(client: ClientResult) -> ClientResult:
    factors = {
        "Kyiv": 1.10,
        "Lviv": 1.05,
        "Odesa": 1.03,
    }

    factor = factors.get(client["city"], 1.0)

    return {
        **client,
        "total": client["total"] * factor,
    }


def filter_adults(clients: Iterable[Client]) -> list[Client]:
    return list(
        filter(
            is_adult,
            clients,
        )
    )


def calculate_totals(
    clients: Iterable[Client],
) -> list[ClientResult]:
    return list(
        map(
            calculate_total,
            clients,
        )
    )


def apply_city_factors(
    clients: Iterable[ClientResult],
) -> list[ClientResult]:
    return list(
        map(
            apply_city_factor,
            clients,
        )
    )


def sort_clients(
    clients: Iterable[ClientResult],
) -> list[ClientResult]:
    return sorted(
        clients,
        key=lambda client: (
            -client["total"],
            client["name"],
        ),
    )


def top_n_clients(
    clients: Iterable[ClientResult],
    n: int,
) -> list[ClientResult]:
    return list(clients)[:n]


def compose(
    *functions: Callable,
) -> Callable:
    def composed(value):
        result = value

        for function in functions:
            result = function(result)

        return result

    return composed


def build_pipeline() -> Callable:
    return compose(
        filter_adults,
        calculate_totals,
        apply_city_factors,
        sort_clients,
    )


def calculate_statistics(
    clients: Iterable[ClientResult],
) -> dict[str, float]:
    clients_list = list(clients)

    count = len(clients_list)

    sum_total = reduce(
        lambda acc, client: acc + client["total"],
        clients_list,
        0.0,
    )

    avg_total = (
        sum_total / count
        if count > 0
        else 0.0
    )

    return {
        "count": float(count),
        "sum_total": sum_total,
        "avg_total": avg_total,
    }
