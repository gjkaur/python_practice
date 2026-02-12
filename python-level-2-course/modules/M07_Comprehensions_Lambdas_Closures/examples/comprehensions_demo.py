"""Demonstrate list comprehensions, lambda, map, filter, closure (PCAP 5.1-5.3)."""
# List comprehension with if (PCAP 5.1)
evens = [x for x in range(10) if x % 2 == 0]
print("evens =", evens)

# Lambda and map/filter (PCAP 5.2)
sq = list(map(lambda x: x * x, [1, 2, 3]))
print("map(sq) =", sq)
pos = list(filter(lambda x: x > 0, [-1, 0, 1, 2]))
print("filter(pos) =", pos)

# Closure (PCAP 5.3)
def make_adder(n):
    def add(x):
        return x + n
    return add
add2 = make_adder(2)
print("add2(5) =", add2(5))
