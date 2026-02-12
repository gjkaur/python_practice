"""Practice: Comprehensions, lambdas, closures (PCAP 5.1-5.3).

Implement the functions. Run main() to test.
"""


# --- Task 1: List comprehension with if (PCAP 5.1) ---
def evens_up_to(n: int) -> list[int]:
    """Return list of even integers in range(n) using a list comprehension with if."""
    return [x for x in range(n) if x % 2 == 0]


# --- Task 2: map with lambda (PCAP 5.2) ---
def add_one_to_each(nums: list[int]) -> list[int]:
    """Return list with each element increased by 1. Use map and lambda."""
    return list(map(lambda x: x + 1, nums))


# --- Task 3: Closure (PCAP 5.3) ---
def make_multiplier(n: int):
    """Return a function that takes x and returns x * n."""
    def mul(x):
        return x * n
    return mul


def main() -> None:
    print("evens_up_to(10):", evens_up_to(10))
    print("add_one_to_each([1,2,3]):", add_one_to_each([1, 2, 3]))
    mul3 = make_multiplier(3)
    print("make_multiplier(3)(4):", mul3(4))


if __name__ == "__main__":
    main()
