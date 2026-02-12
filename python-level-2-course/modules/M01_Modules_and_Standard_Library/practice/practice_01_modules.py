"""Practice: Modules and standard library (PCAP 1.1-1.4).

Complete each function or task. Run the file and uncomment the assertions at the bottom to check.
"""
import math
import random
import platform
import sys


# --- Task 1: math (PCAP 1.2) ---
def floor_ceil_demo(value: float) -> tuple[int, int]:
    """Return (floor(value), ceil(value)) using the math module."""
    return (math.floor(value), math.ceil(value))


# --- Task 2: dir() (PCAP 1.1) ---
def first_n_math_names(n: int = 8) -> list:
    """Return the first n names from dir(math) (as a list)."""
    return dir(math)[:n]


# --- Task 3: platform (PCAP 1.4) ---
def platform_report() -> dict:
    """Return a dict with keys 'system', 'machine', 'version_tuple' and their values from the platform module."""
    return {
        "system": platform.system(),
        "machine": platform.machine(),
        "version_tuple": platform.python_version_tuple(),
    }


# --- Task 4: random with seed (PCAP 1.3) ---
def two_choices_with_seed(seed: int, choices: list) -> tuple:
    """Set random.seed(seed), then return (random.choice(choices), random.choice(choices))."""
    random.seed(seed)
    a = random.choice(choices)
    b = random.choice(choices)
    return (a, b)


# --- Task 5: hypot (PCAP 1.2) ---
def distance_origin(x: float, y: float) -> float:
    """Return the distance from (0, 0) to (x, y) using math.hypot."""
    return math.hypot(x, y)


# --- Task 6: sys.path (PCAP 1.1) ---
def first_sys_path_entry() -> str:
    """Return the first entry in sys.path."""
    return sys.path[0]


# --- Task 7: math names starting with 'f' ---
def math_names_starting_with_f() -> list:
    """Return a list of names in dir(math) that start with the letter 'f'."""
    return [n for n in dir(math) if n.startswith("f")]


def main() -> None:
    print("floor_ceil_demo(7.3) =", floor_ceil_demo(7.3))
    print("first_n_math_names(5) =", first_n_math_names(5))
    print("platform_report() =", platform_report())
    print("two_choices_with_seed(0, ['a','b','c']) =", two_choices_with_seed(0, ["a", "b", "c"]))
    print("distance_origin(1, 1) =", distance_origin(1, 1))
    print("first_sys_path_entry() =", first_sys_path_entry()[:50], "...")
    print("math_names_starting_with_f() =", math_names_starting_with_f())


if __name__ == "__main__":
    main()
    # Uncomment to self-check:
    # assert floor_ceil_demo(7.3) == (7, 8)
    # assert distance_origin(3, 4) == 5.0
    # assert len(math_names_starting_with_f()) >= 4
