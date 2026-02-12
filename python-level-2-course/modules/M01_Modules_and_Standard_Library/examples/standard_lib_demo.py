"""Demonstrate math, random, and platform (PCAP 1.2-1.4)."""
import math
import random
import platform
import sys

# math (PCAP 1.2)
print("math.sqrt(16) =", math.sqrt(16))
print("math.ceil(3.2) =", math.ceil(3.2))
print("math.floor(3.8) =", math.floor(3.8))
print("math.factorial(5) =", math.factorial(5))
print("math.hypot(3, 4) =", math.hypot(3, 4))

# random (PCAP 1.3)
random.seed(42)
print("random.random() =", random.random())
print("random.choice([1,2,3]) =", random.choice([1, 2, 3]))
print("random.sample(range(5), 3) =", random.sample(range(5), 3))

# platform (PCAP 1.4)
print("platform.system() =", platform.system())
print("platform.python_version_tuple() =", platform.python_version_tuple())

# dir and sys.path (PCAP 1.1)
print("dir(math)[:5] =", dir(math)[:5])
print("sys.path[0] =", sys.path[0])
