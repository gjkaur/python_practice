"""
CLI entrypoint for the Admission Eligibility Checker mini-project.
"""

from __future__ import annotations

from rules import classify_applicant
from validators import read_int_in_range, read_non_negative_int


def main() -> None:
    print("Admission Eligibility Checker")
    print("-----------------------------")

    age = read_int_in_range("Age: ", min_value=0, max_value=100)
    score = read_int_in_range("Test score (0-100): ", min_value=0, max_value=100)
    experience = read_non_negative_int("Years of relevant experience: ")

    decision, reason = classify_applicant(age=age, score=score, experience_years=experience)

    print()
    print(f"Decision: {decision}")
    print(f"Reason  : {reason}")


if __name__ == "__main__":
    main()

