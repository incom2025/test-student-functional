from models import StudentRank, rank_students
from pipeline import pipeline
from main import normalize_score, add_status, process_students


def test_pipeline():
    process = pipeline(
        lambda x: x + 1,
        lambda x: x * 2,
    )

    assert process(3) == 8


def test_student_rank_comparison():
    anna = StudentRank("Anna", 90)
    ivan = StudentRank("Ivan", 80)

    assert anna > ivan
    assert ivan < anna
    assert StudentRank("A", 90) == StudentRank("B", 90)


def test_rank_students():
    students = [
        {"name": "Ivan", "score": 78},
        {"name": "Maria", "score": 96},
        {"name": "Anna", "score": 92},
    ]

    result = rank_students(students)

    assert len(result) == 3
    assert result[0].name == "Maria"
    assert result[0].score == 96
    assert result[1].name == "Anna"
    assert result[2].name == "Ivan"


def test_normalize_score():
    student = {
        "name": "Anna",
        "score": "92",
    }

    result = normalize_score(student)

    assert result["name"] == "Anna"
    assert result["score"] == 92.0


def test_add_status_excellent():
    student = {
        "name": "Anna",
        "score": 92.0,
    }

    result = add_status(student)

    assert result["status"] == "excellent"


def test_add_status_good():
    student = {
        "name": "Ivan",
        "score": 78.0,
    }

    result = add_status(student)

    assert result["status"] == "good"


def test_add_status_satisfactory():
    student = {
        "name": "Petro",
        "score": 64.0,
    }

    result = add_status(student)

    assert result["status"] == "satisfactory"


def test_add_status_failed():
    student = {
        "name": "Oleh",
        "score": 40.0,
    }

    result = add_status(student)

    assert result["status"] == "failed"


def test_process_students():
    students = [
        {"name": "Ivan", "score": 78},
        {"name": "Maria", "score": 96},
        {"name": "Anna", "score": 92},
    ]

    result = process_students(students)

    assert len(result) == 3
    assert result[0].name == "Maria"
    assert result[1].name == "Anna"
    assert result[2].name == "Ivan"
