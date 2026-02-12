"""Demonstrate open, read, write, readline, readlines (PCAP 5.4-5.5)."""
import os
import errno

path = "demo_output.txt"
# Write
with open(path, "w", encoding="utf-8") as f:
    f.write("line 1\nline 2\nline 3\n")

# Read
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
print("read() =", repr(content[:20]))

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("readlines() =", lines)

# errno (PCAP 5.5)
try:
    open("nonexistent_file_xyz.txt")
except OSError as e:
    print("errno =", e.errno, "ENOENT =", errno.ENOENT)

# Cleanup
if os.path.exists(path):
    os.remove(path)
