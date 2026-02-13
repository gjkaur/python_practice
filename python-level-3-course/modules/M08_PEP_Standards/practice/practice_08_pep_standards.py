"""
PCPP 2.1, 2.2, 2.3: Practice Exercises - PEP Standards

Refactor the code below to follow PEP 8, PEP 257, and PEP 484.
"""

# TODO: Refactor this code to be PEP 8/257/484 compliant

class badclass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def calc(self):
        return self.x+self.y

def badfunction(a,b,c=None):
    if c is None:
        return a*b
    else:
        return a*b*c

# TODO: Add proper:
# - Naming conventions (PEP 8)
# - Docstrings (PEP 257)
# - Type hints (PEP 484)
# - Spacing and formatting (PEP 8)
# - Line length compliance

# Refactored versions:

class GoodClass:
    """Properly named class with docstring."""
    # TODO: Implement with PEP 8/257/484 compliance
    pass


def good_function(a: int, b: int, c: Optional[int] = None) -> int:
    """Properly documented function with type hints."""
    # TODO: Implement with PEP 8/257/484 compliance
    pass


if __name__ == "__main__":
    print("Refactor the code above to be PEP compliant!")
