"""
In-memory repository for managing student scores.
"""

from __future__ import annotations

from typing import Dict


Scores = Dict[str, int]


def normalize_name(name: str) -> str:
    """Normalize student name for use as a key."""
    return name.strip()


def add_or_update_student(scores: Scores, name: str, score: int) -> None:
    """Add a new student or update an existing student's score."""
    key = normalize_name(name)
    scores[key] = score


def get_all_students(scores: Scores) -> Scores:
    """Return a shallow copy of all student scores."""
    return dict(scores)

