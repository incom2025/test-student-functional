from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


def load_students(path: str | Path) -> list[dict[str, Any]]:
    """
    Завантажує дані студентів із JSON або CSV.
    Формат визначається за розширенням файлу.
    """
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    suffix = file_path.suffix.lower()

    if suffix == ".json":
        return _load_json(file_path)

    if suffix == ".csv":
        return _load_csv(file_path)

    raise ValueError(
        f"Unsupported file format: {suffix}"
    )


def _load_json(path: Path) -> list[dict[str, Any]]:
    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError(
            "JSON must contain a list of students"
        )

    return data


def _load_csv(path: Path) -> list[dict[str, Any]]:
    with path.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as file:
        reader = csv.DictReader(file)
        return list(reader)


if __name__ == "__main__":
    print("Student data loader is ready.")
