"""Demonstrate ord/chr, slicing, join/split, find (PCAP 3.1-3.3)."""
# ord, chr (PCAP 3.2)
print("ord('A') =", ord("A"))
print("chr(65) =", chr(65))

# indexing, slicing, in
s = "Hello, World"
print("s[0:5] =", s[0:5])
print("'ell' in s =", "ell" in s)

# join, split (PCAP 3.3)
words = ["a", "b", "c"]
print("' '.join(words) =", " ".join(words))
print("'a b c'.split() =", "a b c".split())

# find, index, rfind
print("s.find('l') =", s.find("l"))
print("s.rfind('l') =", s.rfind("l"))
