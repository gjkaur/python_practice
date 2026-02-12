"""
Example: String parsing and formatting.
"""
# Parse "name: score" style line
def parse_score_line(line: str) -> tuple[str, int]:
    name_part, score_part = line.split(":")
    return name_part.strip(), int(score_part.strip())

line = "Alice : 85"
name, score = parse_score_line(line)
print(f"Name: {name}, Score: {score}")

# Normalize input for comparison
raw = "  YES  "
if raw.strip().upper() == "YES":
    print("Normalized to YES")
