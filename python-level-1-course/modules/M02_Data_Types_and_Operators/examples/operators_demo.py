"""
Example: Numeric and boolean operators in practice.
"""
# Named constants (avoid magic numbers)
BASE_PRICE = 100.0
DISCOUNT_RATE = 0.15

quantity = 3
raw = BASE_PRICE * quantity
discount = raw * DISCOUNT_RATE if quantity >= 5 else 0.0
final = raw - discount

print(f"Quantity: {quantity}, Raw: {raw}, Discount: {discount}, Final: {final}")

# Boolean and comparison
is_eligible = quantity >= 5 and raw > 200
print("Eligible for bulk discount?", is_eligible)
