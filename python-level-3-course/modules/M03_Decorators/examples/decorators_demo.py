"""
PCPP 1.4: Decorators & Extended Arguments Demo

Demonstrates:
- Extended function arguments (*args, **kwargs)
- Closures
- Function decorators
- Decorators with arguments
- Class decorators
"""

import functools
import time
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])


# PCPP 1.4: Extended Function Arguments
def sum_all(*args: float) -> float:
    """PCPP 1.4: Function accepting variable positional arguments."""
    return sum(args)


def create_user(name: str, email: str, **kwargs: Any) -> dict[str, Any]:
    """PCPP 1.4: Function accepting variable keyword arguments.
    
    Args:
        name: User's name
        email: User's email
        **kwargs: Additional user attributes (age, city, etc.)
    """
    user = {'name': name, 'email': email}
    user.update(kwargs)
    return user


def forward_arguments(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """PCPP 1.4: Forwarding arguments to another function."""
    return func(*args, **kwargs)


# PCPP 1.4: Closures
def make_multiplier(n: int) -> Callable[[int], int]:
    """PCPP 1.4: Closure - function factory that captures 'n'."""
    def multiply(x: int) -> int:
        # Inner function has access to 'n' from outer scope
        return x * n
    return multiply


def make_counter() -> Callable[[], int]:
    """PCPP 1.4: Closure with mutable state."""
    count = 0  # Captured variable
    
    def counter() -> int:
        nonlocal count  # Modify outer variable
        count += 1
        return count
    
    return counter


# PCPP 1.4: Simple Function Decorator
def timer(func: F) -> F:
    """PCPP 1.4: Decorator that measures function execution time."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper  # type: ignore


@timer
def slow_function() -> None:
    """Example function to be timed."""
    time.sleep(0.1)
    print("Function executed")


# PCPP 1.4: Decorator with Arguments (Three-Level Function)
def repeat(n: int) -> Callable[[F], F]:
    """PCPP 1.4: Decorator factory - returns a decorator.
    
    Args:
        n: Number of times to repeat function call
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            results = []
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results[-1]  # Return last result
        return wrapper  # type: ignore
    return decorator


@repeat(3)
def greet(name: str) -> str:
    """Greet function that will be repeated."""
    print(f"Hello, {name}!")
    return f"Greeted {name}"


# PCPP 1.4: Class-Based Decorator
class Logger:
    """PCPP 1.4: Class decorator using __call__ method."""
    
    def __init__(self, module_name: str) -> None:
        """Initialize logger decorator.
        
        Args:
            module_name: Name of the module being logged
        """
        self.module_name = module_name
    
    def __call__(self, func: F) -> F:
        """PCPP 1.4: Make class instance callable as decorator."""
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"[{self.module_name}] Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{self.module_name}] {func.__name__} completed")
            return result
        return wrapper  # type: ignore


@Logger("math_utils")
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# PCPP 1.4: Advanced Decorator - Retry with Exponential Backoff
def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable[[F], F]:
    """Decorator that retries function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Initial delay between retries (seconds)
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                        time.sleep(current_delay)
                        current_delay *= 2  # Exponential backoff
            
            raise last_exception  # type: ignore
        return wrapper  # type: ignore
    return decorator


@retry(max_attempts=3, delay=0.5)
def unreliable_function() -> str:
    """Function that may fail."""
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"


# PCPP 1.4: Decorator Stacking
def validate_input(validator: Callable[[Any], bool]) -> Callable[[F], F]:
    """Decorator that validates function arguments."""
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for arg in args:
                if not validator(arg):
                    raise ValueError(f"Invalid argument: {arg}")
            return func(*args, **kwargs)
        return wrapper  # type: ignore
    return decorator


@timer
@validate_input(lambda x: x > 0)
def calculate_square_root(x: float) -> float:
    """Calculate square root of positive number."""
    return x ** 0.5


if __name__ == "__main__":
    print("=== Extended Arguments ===")
    print(f"sum_all(1, 2, 3, 4): {sum_all(1, 2, 3, 4)}")
    
    user = create_user("Alice", "alice@example.com", age=30, city="New York")
    print(f"User: {user}")
    
    print("\n=== Closures ===")
    multiply_by_5 = make_multiplier(5)
    print(f"multiply_by_5(10): {multiply_by_5(10)}")
    
    counter = make_counter()
    print(f"counter(): {counter()}")
    print(f"counter(): {counter()}")
    
    print("\n=== Simple Decorator ===")
    slow_function()
    
    print("\n=== Decorator with Arguments ===")
    result = greet("World")
    print(f"Result: {result}")
    
    print("\n=== Class Decorator ===")
    result = add(5, 3)
    print(f"Result: {result}")
    
    print("\n=== Retry Decorator ===")
    try:
        result = unreliable_function()
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Failed after retries: {e}")
    
    print("\n=== Decorator Stacking ===")
    try:
        result = calculate_square_root(16)
        print(f"Square root of 16: {result}")
    except ValueError as e:
        print(f"Validation error: {e}")
