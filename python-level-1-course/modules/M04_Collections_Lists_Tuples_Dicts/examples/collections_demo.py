"""
Example: Lists, tuples, and dicts in practice.
"""
# List: ordered, mutable
scores = [70, 85, 90]
scores.append(75)
print("Scores:", scores)

# Tuple: immutable record
student = ("Alice", 85)
name, score = student
print(f"{name}: {score}")

# Dict: key-value storage
by_name = {"Alice": 85, "Bob": 70}
by_name["Charlie"] = 90
print("By name:", by_name)
