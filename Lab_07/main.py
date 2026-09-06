from models import StudentRank, rank_students
from pipeline import pipeline


def normalize_score(student: dict) -> dict:
    """Перетворює score на float."""
    return {
        **student,
        "score": float(student["score"]),
    }


def add_status(student: dict) -> dict:
    """Додає статус залежно від бала."""
    score = student["score"]

    if score >= 90:
        status = "excellent"
    elif score >= 75:
        status = "good"
    elif score >= 60:
        status = "satisfactory"
    else:
        status = "failed"

    return {
        **student,
        "status": status,
    }


def process_students(students: list[dict]) -> list[StudentRank]:
    """
    Обробка студентів через композицію функцій.
    """

    process = pipeline(
        normalize_score,
        add_status,
    )

    processed = [
        process(student)
        for student in students
    ]

    return rank_students(processed)


def main() -> None:
    students = [
        {"name": "Anna", "score": 92},
        {"name": "Ivan", "score": 78},
        {"name": "Maria", "score": 96},
        {"name": "Petro", "score": 64},
    ]

    ranked = process_students(students)

    print("Student ranking:")
    for number, student in enumerate(ranked, start=1):
        print(
            f"{number}. "
            f"{student.name}: "
            f"{student.score}"
        )


if __name__ == "__main__":
    main()
