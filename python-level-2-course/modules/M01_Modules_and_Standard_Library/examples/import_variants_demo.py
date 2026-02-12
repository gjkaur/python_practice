"""Demonstrate all import variants (PCAP 1.1)."""
# Style 1: import module → qualified names
import math
print("import math → math.sqrt(25) =", math.sqrt(25))

# Style 2: from module import name(s)
from math import floor, ceil, factorial
print("from math import floor, ceil → floor(4.7) =", floor(4.7), "ceil(4.2) =", ceil(4.2))

# Style 3: from module import name as alias
from math import sqrt as sq
print("from math import sqrt as sq → sq(36) =", sq(36))

# dir() to see what we have in current scope (includes floor, ceil, factorial, sq, math)
names_from_math = [n for n in dir() if n in ("floor", "ceil", "factorial", "sq", "math")]
print("Names we got from math-related imports:", names_from_math)
