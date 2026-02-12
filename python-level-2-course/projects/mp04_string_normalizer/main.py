"""CLI: normalize string and show codepoint info."""
from normalizer import normalize_whitespace, normalize_case, codepoint_info

def main():
    line = input("Enter text: ")
    print("Normalized whitespace:", normalize_whitespace(line))
    print("Lowercase:", normalize_case(line))
    print("First 5 codepoints:", codepoint_info(line))
    sub = input("Substring to find: ")
    idx = line.find(sub)
    print(f"find({sub!r}) =", idx)

if __name__ == "__main__":
    main()
