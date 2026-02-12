"""
Statistics helpers for student scores.
"""

from __future__ import annotations

from typing import Iterable, Optional


def compute_min(scores: Iterable[int]) -> Optional[int]:
    """Return the minimum score, or None if there are no scores."""
    scores_list = list(scores)
    return min(scores_list) if scores_list else None


def compute_max(scores: Iterable[int]) -> Optional[int]:
    """Return the maximum score, or None if there are no scores."""
    scores_list = list(scores)
    return max(scores_list) if scores_list else None


def compute_average(scores: Iterable[int]) -> Optional[float]:
    """Return the average score, or None if there are no scores."""
    scores_list = list(scores)
    if not scores_list:
        return None
    return sum(scores_list) / len(scores_list)

