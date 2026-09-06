from __future__ import annotations

import ast
from pathlib import Path
from typing import Any


# ============================================================
# Laboratory work №2
# Functional Programming
# Higher-order functions, lambda, composition
# ============================================================

LAB02_VARIANTS: dict[str, dict[str, Any]] = {
    "1": {
        "title": "Клієнти інтернет-магазину",
        "keywords": [
            "client",
            "customer",
            "age",
            "city",
            "purchases",
            "total",
            "top",
        ],
        "filter_keywords": [
            "age",
            "adult",
            "filter",
            "accept",
        ],
        "calculation_keywords": [
            "purchases",
            "total",
            "sum",
            "factor",
            "city",
        ],
        "aggregation_keywords": [
            "count",
            "sum_total",
            "avg_total",
        ],
    },

    "2": {
        "title": "Успішність студентів",
        "keywords": [
            "student",
            "students",
            "group",
            "scores",
            "average",
            "bonus",
            "top",
        ],
        "filter_keywords": [
            "scores",
            "minimum",
            "filter",
            "accept",
        ],
        "calculation_keywords": [
            "average",
            "avg",
            "score",
            "bonus",
            "group",
        ],
        "aggregation_keywords": [
            "count",
            "sum_avg",
            "group_avg",
        ],
    },

    "3": {
        "title": "Продажі менеджерів",
        "keywords": [
            "manager",
            "sales",
            "region",
            "revenue",
            "rating",
            "factor",
        ],
        "filter_keywords": [
            "minimum",
            "sales",
            "filter",
            "threshold",
        ],
        "calculation_keywords": [
            "sales",
            "revenue",
            "factor",
            "region",
            "total",
        ],
        "aggregation_keywords": [
            "count",
            "revenue",
            "avg_sales",
        ],
    },

    "4": {
        "title": "Замовлення ресторану",
        "keywords": [
            "order",
            "restaurant",
            "waiter",
            "table",
            "items",
            "check",
            "service",
            "top",
        ],
        "filter_keywords": [
            "minimum",
            "check",
            "filter",
            "threshold",
        ],
        "calculation_keywords": [
            "items",
            "check",
            "total",
            "service",
            "factor",
        ],
        "aggregation_keywords": [
            "count",
            "sum_checks",
            "avg_check",
        ],
    },

    "5": {
        "title": "Спортивний рейтинг",
        "keywords": [
            "athlete",
            "sport",
            "category",
            "results",
            "points",
            "rating",
            "bonus",
        ],
        "filter_keywords": [
            "eligible",
            "admitted",
            "filter",
            "threshold",
        ],
        "calculation_keywords": [
            "result",
            "average",
            "best",
            "bonus",
            "points",
        ],
        "aggregation_keywords": [
            "count",
            "sum_points",
            "avg_points",
        ],
    },

    "6": {
        "title": "Рейтинг книг",
        "keywords": [
            "book",
            "title",
            "genre",
            "ratings",
            "rating",
            "top",
        ],
        "filter_keywords": [
            "rating",
            "minimum",
            "filter",
            "threshold",
        ],
        "calculation_keywords": [
            "rating",
            "average",
            "genre",
            "factor",
        ],
        "aggregation_keywords": [
            "count",
            "rating_sum",
            "avg_rating",
        ],
    },

    "7": {
        "title": "Аналіз товарів складу",
        "keywords": [
            "product",
            "stock",
            "warehouse",
            "category",
            "price",
            "inventory",
            "value",
        ],
        "filter_keywords": [
            "stock",
            "minimum",
            "filter",
            "threshold",
        ],
        "calculation_keywords": [
            "stock",
            "price",
            "value",
            "category",
            "factor",
        ],
        "aggregation_keywords": [
            "count",
            "inventory_value",
            "avg_value",
        ],
    },

    "8": {
        "title": "Банківські рахунки",
        "keywords": [
            "client",
            "bank",
            "transactions",
            "turnover",
            "city",
            "top",
        ],
        "filter_keywords": [
            "turnover",
            "minimum",
            "filter",
            "threshold",
        ],
        "calculation_keywords": [
            "transaction",
            "turnover",
            "city",
            "factor",
            "sum",
        ],
        "aggregation_keywords": [
            "count",
            "turnover",
            "avg_turnover",
        ],
    },

    "9": {
        "title": "Працівники компанії",
        "keywords": [
            "employee",
            "department",
            "hours",
            "monthly_hours",
            "top",
            "factor",
        ],
        "filter_keywords": [
            "hours",
            "minimum",
            "filter",
            "threshold",
        ],
        "calculation_keywords": [
            "hours",
            "monthly_hours",
            "department",
            "factor",
            "total",
        ],
        "aggregation_keywords": [
            "count",
            "total_hours",
            "avg_hours",
        ],
    },

    "10": {
        "title": "Курси онлайн-платформи",
        "keywords": [
            "course",
            "courses",
            "category",
            "enrollments",
            "rating",
            "top",
        ],
        "filter_keywords": [
            "enrollments",
            "minimum",
            "filter",
            "popular",
        ],
        "calculation_keywords": [
            "enrollments",
            "category",
            "factor",
            "total",
        ],
        "aggregation_keywords": [
            "count",
            "enrollments",
            "avg_enrollments",
        ],
    },

    "11": {
        "title": "Готельні бронювання",
        "keywords": [
            "booking",
            "guest",
            "city",
            "nights",
            "cost",
            "revenue",
            "top",
        ],
        "filter_keywords": [
            "booking",
            "filter",
            "minimum",
            "threshold",
        ],
        "calculation_keywords": [
            "nights",
            "cost",
            "city",
            "factor",
            "revenue",
        ],
        "aggregation_keywords": [
            "count",
            "revenue",
            "avg_booking",
        ],
    },

    "12": {
        "title": "Мобільні абоненти",
        "keywords": [
            "subscriber",
            "mobile",
            "tariff",
            "payments",
            "bonus",
            "rating",
        ],
        "filter_keywords": [
            "active",
            "payments",
            "filter",
            "minimum",
        ],
        "calculation_keywords": [
            "payments",
            "tariff",
            "bonus",
            "sum",
        ],
        "aggregation_keywords": [
            "count",
            "payments_sum",
            "avg_payment",
        ],
    },

    "13": {
        "title": "Доставка посилок",
        "keywords": [
            "parcel",
            "delivery",
            "sender",
            "region",
            "delivery_parts",
            "cost",
            "top",
        ],
        "filter_keywords": [
            "threshold",
            "delivery",
            "filter",
            "minimum",
        ],
        "calculation_keywords": [
            "delivery",
            "parts",
            "region",
            "factor",
            "cost",
        ],
        "aggregation_keywords": [
            "count",
            "delivery_sum",
            "avg_delivery",
        ],
    },

    "14": {
        "title": "Музичний каталог",
        "keywords": [
            "track",
            "music",
            "title",
            "genre",
            "listens",
            "rating",
            "top",
        ],
        "filter_keywords": [
            "listens",
            "popular",
            "filter",
            "minimum",
        ],
        "calculation_keywords": [
            "listens",
            "genre",
            "factor",
            "sum",
        ],
        "aggregation_keywords": [
            "count",
            "listens_sum",
            "avg_listens",
        ],
    },

    "15": {
        "title": "Результати лабораторних робіт",
        "keywords": [
            "student",
            "group",
            "lab_scores",
            "score",
            "average",
            "bonus",
            "top",
        ],
        "filter_keywords": [
            "admitted",
            "score",
            "filter",
            "threshold",
        ],
        "calculation_keywords": [
            "lab_scores",
            "score",
            "average",
            "bonus",
            "group",
        ],
        "aggregation_keywords": [
            "count",
            "total_score",
            "avg_score",
        ],
    },
}


# ============================================================
# Helpers
# ============================================================

def find_python_files(lab_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in lab_dir.rglob("*.py")
        if "__pycache__" not in path.parts
    )


def read_source(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ""


def collect_source(lab_dir: Path) -> str:
    return "\n".join(
        read_source(path).lower()
        for path in find_python_files(lab_dir)
    )


def parse_python_files(
    lab_dir: Path,
) -> list[tuple[Path, ast.AST]]:
    parsed: list[tuple[Path, ast.AST]] = []

    for path in find_python_files(lab_dir):
        source = read_source(path)

        if not source:
            continue

        try:
            tree = ast.parse(
                source,
                filename=str(path),
            )
        except SyntaxError:
            continue

        parsed.append((path, tree))

    return parsed


def count_lambdas(
    trees: list[tuple[Path, ast.AST]],
) -> int:
    return sum(
        1
        for _, tree in trees
        for node in ast.walk(tree)
        if isinstance(node, ast.Lambda)
    )


def count_functions(
    trees: list[tuple[Path, ast.AST]],
) -> int:
    return sum(
        1
        for _, tree in trees
        for node in ast.walk(tree)
        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
            ),
        )
    )


def has_typed_record(
    source_text: str,
    trees: list[tuple[Path, ast.AST]],
) -> bool:
    if "typeddict" in source_text:
        return True

    for _, tree in trees:
        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue

            for base in node.bases:
                if (
                    isinstance(base, ast.Name)
                    and base.id == "TypedDict"
                ):
                    return True

                if (
                    isinstance(base, ast.Attribute)
                    and base.attr == "TypedDict"
                ):
                    return True

    return False


def has_map_filter_or_generators(
    trees: list[tuple[Path, ast.AST]],
) -> bool:
    detected = 0

    for _, tree in trees:
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in {
                        "map",
                        "filter",
                    }:
                        detected += 1

            if isinstance(
                node,
                (
                    ast.ListComp,
                    ast.SetComp,
                    ast.DictComp,
                    ast.GeneratorExp,
                ),
            ):
                detected += 1

    return detected >= 2


def has_reduce(
    source_text: str,
    trees: list[tuple[Path, ast.AST]],
) -> bool:
    if "reduce" not in source_text:
        return False

    for _, tree in trees:
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue

            if (
                isinstance(node.func, ast.Name)
                and node.func.id == "reduce"
            ):
                return True

            if (
                isinstance(node.func, ast.Attribute)
                and node.func.attr == "reduce"
            ):
                return True

    return False


def has_compose_or_pipe(
    source_text: str,
    trees: list[tuple[Path, ast.AST]],
) -> bool:
    names = {
        "compose",
        "pipe",
        "pipeline",
        "build_pipeline",
    }

    for _, tree in trees:
        for node in ast.walk(tree):
            if not isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                ),
            ):
                continue

            if node.name.lower() in names:
                return True

            if (
                "compose" in node.name.lower()
                or "pipeline" in node.name.lower()
            ):
                return True

    return (
        "compose(" in source_text
        or "pipe(" in source_text
        or "build_pipeline" in source_text
    )


def count_transformations(
    trees: list[tuple[Path, ast.AST]],
) -> int:
    count = 0

    for _, tree in trees:
        for node in ast.walk(tree):
            if not isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                ),
            ):
                continue

            meaningful = any(
                isinstance(
                    child,
                    (
                        ast.Return,
                        ast.Yield,
                        ast.YieldFrom,
                        ast.ListComp,
                        ast.GeneratorExp,
                        ast.Call,
                        ast.If,
                        ast.For,
                    ),
                )
                for child in ast.walk(node)
            )

            if meaningful:
                count += 1

    return count


def has_sorted_with_complex_key(
    source_text: str,
    trees: list[tuple[Path, ast.AST]],
) -> bool:
    for _, tree in trees:
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue

            is_sorted = (
                isinstance(node.func, ast.Name)
                and node.func.id == "sorted"
            )

            if not is_sorted:
                continue

            for keyword in node.keywords:
                if keyword.arg != "key":
                    continue

                if isinstance(keyword.value, ast.Lambda):
                    if isinstance(
                        keyword.value.body,
                        (
                            ast.Tuple,
                            ast.List,
                        ),
                    ):
                        return True

    return (
        "sorted(" in source_text
        and "lambda" in source_text
    )


def has_top_n_logic(
    source_text: str,
    trees: list[tuple[Path, ast.AST]],
) -> bool:
    if "islice" in source_text:
        return True

    if "top_n" in source_text or "topn" in source_text:
        return True

    for _, tree in trees:
        for node in ast.walk(tree):
            if isinstance(node, ast.Subscript):
                if isinstance(node.slice, ast.Slice):
                    return True

    return False


def has_domain_keywords(
    source_text: str,
    keywords: list[str],
    minimum_hits: int = 3,
) -> bool:
    hits = sum(
        keyword in source_text
        for keyword in keywords
    )

    return hits >= minimum_hits


def has_filtering_logic(
    source_text: str,
    trees: list[tuple[Path, ast.AST]],
    keywords: list[str],
) -> bool:
    keyword_hit = any(
        keyword in source_text
        for keyword in keywords
    )

    structural_hit = False

    for _, tree in trees:
        for node in ast.walk(tree):
            if isinstance(
                node,
                (
                    ast.If,
                    ast.Compare,
                    ast.ListComp,
                    ast.GeneratorExp,
                ),
            ):
                structural_hit = True

            if isinstance(node, ast.Call):
                if (
                    isinstance(node.func, ast.Name)
                    and node.func.id == "filter"
                ):
                    structural_hit = True

    return keyword_hit and structural_hit


def has_calculation_logic(
    source_text: str,
    trees: list[tuple[Path, ast.AST]],
    keywords: list[str],
) -> bool:
    keyword_hit = any(
        keyword in source_text
        for keyword in keywords
    )

    arithmetic_hit = False

    for _, tree in trees:
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp):
                if isinstance(
                    node.op,
                    (
                        ast.Add,
                        ast.Sub,
                        ast.Mult,
                        ast.Div,
                        ast.FloorDiv,
                        ast.Mod,
                    ),
                ):
                    arithmetic_hit = True
                    break

    return keyword_hit and arithmetic_hit


def has_aggregation_keywords(
    source_text: str,
    keywords: list[str],
) -> bool:
    hits = sum(
        keyword in source_text
        for keyword in keywords
    )

    return hits >= 2


def has_io_separation(lab_dir: Path) -> bool:
    names = {
        path.name.lower()
        for path in find_python_files(lab_dir)
    }

    has_core = (
        "core.py" in names
        or "lab2.py" in names
    )

    has_io = (
        "app.py" in names
        or "main.py" in names
    )

    return has_core and has_io


# ============================================================
# Main checker
# ============================================================

def check_variant(
    lab_dir: Path,
    variant: str,
) -> list[dict[str, Any]]:
    """
    Static analysis of Functional Programming Lab_02.

    checker.py uses the returned score as the
    variant-specific part of the 50-point code grade.
    """

    config = LAB02_VARIANTS.get(str(variant))

    if config is None:
        return [
            {
                "name": "variant_supported",
                "passed": False,
                "score": 0,
                "max_score": 20,
                "message": (
                    f"Variant {variant} is not configured "
                    "for Functional Programming Lab_02."
                ),
            }
        ]

    trees = parse_python_files(lab_dir)
    source_text = collect_source(lab_dir)

    lambda_count = count_lambdas(trees)
    function_count = count_functions(trees)
    transformations = count_transformations(trees)

    typed_record_ok = has_typed_record(
        source_text,
        trees,
    )

    map_filter_ok = has_map_filter_or_generators(
        trees
    )

    composition_ok = has_compose_or_pipe(
        source_text,
        trees,
    )

    reduce_ok = has_reduce(
        source_text,
        trees,
    )

    sort_ok = has_sorted_with_complex_key(
        source_text,
        trees,
    )

    top_n_ok = has_top_n_logic(
        source_text,
        trees,
    )

    domain_ok = has_domain_keywords(
        source_text,
        config["keywords"],
    )

    filter_ok = has_filtering_logic(
        source_text,
        trees,
        config["filter_keywords"],
    )

    calculation_ok = has_calculation_logic(
        source_text,
        trees,
        config["calculation_keywords"],
    )

    aggregation_ok = (
        reduce_ok
        and has_aggregation_keywords(
            source_text,
            config["aggregation_keywords"],
        )
    )

    io_separation_ok = has_io_separation(
        lab_dir
    )

    checks: list[dict[str, Any]] = []

    # --------------------------------------------------------
    # Informational
    # --------------------------------------------------------

    checks.append(
        {
            "name": "variant_supported",
            "passed": True,
            "score": 0,
            "max_score": 0,
            "message": (
                f"Variant {variant}: "
                f"{config['title']}"
            ),
        }
    )

    # --------------------------------------------------------
    # 1. Typed record — 3
    # --------------------------------------------------------

    checks.append(
        {
            "name": "lab02_typed_record",
            "passed": typed_record_ok,
            "score": 3 if typed_record_ok else 0,
            "max_score": 3,
            "message": (
                "TypedDict or equivalent typed record "
                + (
                    "detected."
                    if typed_record_ok
                    else "not detected."
                )
            ),
        }
    )

    # --------------------------------------------------------
    # 2. Transformations + composition — 4
    # --------------------------------------------------------

    transformations_ok = (
        transformations >= 4
        and composition_ok
        and domain_ok
    )

    checks.append(
        {
            "name": "lab02_transformations",
            "passed": transformations_ok,
            "score": 4 if transformations_ok else 0,
            "max_score": 4,
            "message": (
                f"Functions: {function_count}; "
                f"transformations: {transformations}; "
                f"composition: {composition_ok}; "
                f"domain vocabulary: {domain_ok}."
            ),
        }
    )

    # --------------------------------------------------------
    # 3. map/filter/generators — 3
    # --------------------------------------------------------

    map_filter_domain_ok = (
        map_filter_ok
        and filter_ok
        and calculation_ok
    )

    checks.append(
        {
            "name": "lab02_map_filter_pipeline",
            "passed": map_filter_domain_ok,
            "score": 3 if map_filter_domain_ok else 0,
            "max_score": 3,
            "message": (
                f"map/filter/generator usage: {map_filter_ok}; "
                f"variant filtering: {filter_ok}; "
                f"variant calculation: {calculation_ok}."
            ),
        }
    )

    # --------------------------------------------------------
    # 4. lambda — 2
    # --------------------------------------------------------

    lambda_ok = lambda_count >= 2

    checks.append(
        {
            "name": "lab02_lambda",
            "passed": lambda_ok,
            "score": 2 if lambda_ok else 0,
            "max_score": 2,
            "message": (
                f"Lambda expressions found: "
                f"{lambda_count}. "
                "At least 2 are required."
            ),
        }
    )

    # --------------------------------------------------------
    # 5. sorting + Top-N — 3
    # --------------------------------------------------------

    sorting_top_ok = (
        sort_ok
        and top_n_ok
    )

    checks.append(
        {
            "name": "lab02_sort_top_n",
            "passed": sorting_top_ok,
            "score": 3 if sorting_top_ok else 0,
            "max_score": 3,
            "message": (
                f"Two-key/functional sorting: {sort_ok}; "
                f"Top-N logic: {top_n_ok}."
            ),
        }
    )

    # --------------------------------------------------------
    # 6. reduce + statistics — 3
    # --------------------------------------------------------

    checks.append(
        {
            "name": "lab02_reduce_stats",
            "passed": aggregation_ok,
            "score": 3 if aggregation_ok else 0,
            "max_score": 3,
            "message": (
                f"reduce detected: {reduce_ok}; "
                f"required aggregation vocabulary: "
                f"{aggregation_ok}."
            ),
        }
    )

    # --------------------------------------------------------
    # 7. clean core / I/O separation — 2
    # --------------------------------------------------------

    checks.append(
        {
            "name": "lab02_io_separation",
            "passed": io_separation_ok,
            "score": 2 if io_separation_ok else 0,
            "max_score": 2,
            "message": (
                "Separate core and I/O modules "
                + (
                    "detected."
                    if io_separation_ok
                    else "not detected."
                )
            ),
        }
    )

    return checks
