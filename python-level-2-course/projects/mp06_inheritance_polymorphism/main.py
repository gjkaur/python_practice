"""Demo: polymorphism and isinstance."""
from models import Product, DiscountedProduct

def main():
    products = [
        Product("A", 10.0),
        DiscountedProduct("B", 10.0, 0.1),
    ]
    for p in products:
        print(p)
        print("  isinstance(Product):", isinstance(p, Product))
        print("  get_price():", p.get_price())

if __name__ == "__main__":
    main()
