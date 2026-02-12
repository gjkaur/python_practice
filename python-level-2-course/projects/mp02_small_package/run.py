"""Run demo: import from package."""
from pkg import greet, add_one

if __name__ == "__main__":
    print(greet("World"))
    print(add_one(41))
