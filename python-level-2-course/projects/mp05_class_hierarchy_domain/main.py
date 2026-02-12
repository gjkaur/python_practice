"""Demo: create Product and OrderLine, show __dict__, hasattr."""
from models import Product, OrderLine

def main():
    p = Product("Widget", 9.99)
    print(p)
    print("__dict__:", p.__dict__)
    print("hasattr(name):", hasattr(p, "name"))
    line = OrderLine(p, 3)
    print("OrderLine total:", line.total())

if __name__ == "__main__":
    main()
