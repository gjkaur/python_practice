"""
Example: Lexis, syntax, and semantics in practice.
- Lexis: identifiers, literals, operators
- Syntax: assignment, expression, block
- Semantics: binding and execution
"""
# Constants (PEP 8: UPPER_SNAKE_CASE)
GREETING = "Welcome"

# Variable (snake_case)
user_name = "Alice"

# Semantics: evaluate expression and print
print(GREETING + ", " + user_name + "!")

# Block: indentation defines scope
if user_name:
    print("Name is non-empty.")
