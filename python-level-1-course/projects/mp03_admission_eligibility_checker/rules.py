"""
Eligibility rules for the Admission Eligibility Checker.

All functions here should be pure (no I/O).
"""

from __future__ import annotations


def classify_applicant(age: int, score: int, experience_years: int) -> tuple[str, str]:
    """
    Classify an applicant as ACCEPTED, WAITLISTED, or REJECTED.

    Policy (example):
    - Reject if age < 16.
    - ACCEPTED if:
        - score >= 85 and experience_years >= 1, or
        - score >= 90 regardless of experience.
    - WAITLISTED if:
        - 70 <= score < 85, or
        - score >= 85 and experience_years == 0.
    - Otherwise REJECTED.
    """
    if age < 16:
        return "REJECTED", "Age below minimum requirement."

    if score >= 90:
        return "ACCEPTED", "Strong test score (>= 90)."

    if score >= 85 and experience_years >= 1:
        return "ACCEPTED", "High test score and relevant experience."

    if 70 <= score < 85:
        return "WAITLISTED", "Moderate test score; consider for waitlist."

    if score >= 85 and experience_years == 0:
        return "WAITLISTED", "High score but no relevant experience yet."

    return "REJECTED", "Test score below threshold."

