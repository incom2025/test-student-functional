from core import (
    build_pipeline,
    top_n_clients,
    calculate_statistics,
)


def main() -> None:
    clients = [
        {
            "name": "Anna",
            "age": 25,
            "city": "Kyiv",
            "purchases": [120.0, 80.0, 300.0],
        },
        {
            "name": "Bohdan",
            "age": 17,
            "city": "Lviv",
            "purchases": [50.0, 70.0],
        },
        {
            "name": "Olena",
            "age": 31,
            "city": "Lviv",
            "purchases": [400.0, 150.0],
        },
        {
            "name": "Andrii",
            "age": 22,
            "city": "Odesa",
            "purchases": [200.0, 100.0, 50.0],
        },
        {
            "name": "Iryna",
            "age": 28,
            "city": "Kyiv",
            "purchases": [600.0, 250.0],
        },
    ]

    pipeline = build_pipeline()

    results = list(pipeline(clients))

    top_clients = top_n_clients(results, 3)

    statistics = calculate_statistics(results)

    print("=== CLIENT PROCESSING RESULTS ===")

    for client in results:
        print(
            f'{client["name"]}: '
            f'{client["city"]}, '
            f'total = {client["total"]:.2f}'
        )

    print("\n=== TOP 3 CLIENTS ===")

    for client in top_clients:
        print(
            f'{client["name"]}: '
            f'{client["total"]:.2f}'
        )

    print("\n=== STATISTICS ===")
    print(f'Count: {statistics["count"]:.0f}')
    print(f'Sum: {statistics["sum_total"]:.2f}')
    print(f'Average: {statistics["avg_total"]:.2f}')


if __name__ == "__main__":
    main()
