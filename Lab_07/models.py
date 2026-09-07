from __future__ import annotations

from dataclasses import dataclass
from functools import total_ordering


@total_ordering
@dataclass
class StudentRank:
    """
    Представляє студента та його підсумковий бал.

    Порівняння виконується за полем score.
    """

    name: str
    score: float

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StudentRank):
            return NotImplemented

        return self.score == other.score

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, StudentRank):
            return NotImplemented

        return self.score < other.score


def rank_students(
    students: list[dict],
) -> list[StudentRank]:
    """
    Перетворює список словників на StudentRank
    та сортує студентів за спаданням бала.
    """

    ranked = [
        StudentRank(
            name=str(student["name"]),
            score=float(student["score"]),
        )
        for student in students
    ]

    return sorted(ranked, reverse=True)

def top_n(
    students: list[StudentRank],
    n: int = 3,
) -> list[StudentRank]:
    """
    Повертає Top-N студентів за балом.
    """
    return sorted(
        students,
        reverse=True,
    )[:n]
if __name__ == "__main__":
    students = [
        {"name": "Anna", "score": 92},
        {"name": "Ivan", "score": 78},
        {"name": "Maria", "score": 96},
    ]

    for student in rank_students(students):
        print(student)
