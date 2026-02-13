"""
PCPP 1.4: Practice Exercises - Decorators & Extended Arguments

Complete the exercises below to practice decorators and extended arguments.
"""

import functools
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])


# Exercise 1: Extended Arguments
# TODO: Create a function `calculate_total` that:
#   - Accepts *args (prices as floats)
#   - Accepts **kwargs (discount as float, tax_rate as float)
#   - Calculates total: sum(args) * (1 - discount) * (1 + tax_rate)
#   - Returns the total

def calculate_total(*args: float, **kwargs: float) -> float:
    """Calculate total with discount and tax."""
    # TODO: Implement function
    pass


# Exercise 2: Closure - Function Factory
# TODO: Create a function `make_power(n)` that returns a function
#   The returned function should raise its argument to the nth power
#   Example: power_3 = make_power(3); power_3(2) returns 8

def make_power(n: int) -> Callable[[int], int]:
    """Create a function that raises to the nth power."""
    # TODO: Implement closure
    pass


# Exercise 3: Simple Decorator
# TODO: Create a decorator `@count_calls` that:
#   - Tracks how many times a function is called
#   - Stores count in function.__call_count__
#   - Prints count each time function is called

def count_calls(func: F) -> F:
    """Decorator that counts function calls."""
    # TODO: Implement decorator
    pass


# Exercise 4: Decorator with Arguments
# TODO: Create a decorator `@delay(seconds)` that:
#   - Accepts delay time in seconds
#   - Waits before calling the function
#   - Uses time.sleep() for delay

import time

def delay(seconds: float) -> Callable[[F], F]:
    """Decorator factory that delays function execution."""
    # TODO: Implement three-level function pattern
    pass


# Exercise 5: Class Decorator
# TODO: Create a class `Cache` that:
#   - Acts as a decorator
#   - Caches function results in a dictionary
#   - Uses function arguments as cache key
#   - Returns cached result if available

class Cache:
    """Class decorator that caches function results."""
    # TODO: Implement class decorator with __call__
    pass


# Exercise 6: Decorator Stacking
# TODO: Create two decorators:
#   - @log_args: prints function arguments before calling
#   - @log_result: prints function result after calling
#   Apply both to a function and demonstrate stacking

def log_args(func: F) -> F:
    """Decorator that logs function arguments."""
    # TODO: Implement
    pass


def log_result(func: F) -> F:
    """Decorator that logs function result."""
    # TODO: Implement
    pass


if __name__ == "__main__":
    print("Complete the exercises above!")
    
    # Test your implementations:
    # total = calculate_total(10, 20, 30, discount=0.1, tax_rate=0.08)
    # print(f"Total: {total}")
    # 
    # power_3 = make_power(3)
    # print(f"2^3 = {power_3(2)}")
    # 
    # @count_calls
    # def test_func():
    #     pass
    # test_func()
    # test_func()
    # print(f"Call count: {test_func.__call_count__}")
