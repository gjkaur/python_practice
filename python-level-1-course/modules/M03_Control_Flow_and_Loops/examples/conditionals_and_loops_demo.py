"""
Example: Conditionals and loop patterns.
"""
# Menu loop pattern (concept only; no input here)
OPTIONS = ["View", "Add", "Exit"]

for i, opt in enumerate(OPTIONS, start=1):
    print(f"{i}) {opt}")

# Guard clause style
def max_of_three(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    if b >= c:
        return b
    return c

print("max_of_three(1, 3, 2) =", max_of_three(1, 3, 2))
