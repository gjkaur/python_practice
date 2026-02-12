"""
Example: Reusable functions and clear signatures.
"""
def discounted_price(amount: float, discount_rate: float) -> float:
    """Single responsibility: compute price after discount."""
    return amount * (1 - discount_rate)

def format_price(amount: float) -> str:
    """Format for display."""
    return f"${amount:.2f}"

# Use them together
price = 100.0
final = discounted_price(price, 0.15)
print(format_price(final))
