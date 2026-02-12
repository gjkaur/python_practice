"""CLI entrypoint: print report using math, random, platform."""
from report import build_report

def main():
    report = build_report()
    print("=== Multi-Module CLI Report ===")
    print("Platform:", report["platform"]["system"])
    print("Python version tuple:", report["platform"]["version_tuple"])
    print("Math (sqrt, ceil, floor of 10.7):", report["math"])
    print("Random sample:", report["random"])
    print("==============================")

if __name__ == "__main__":
    main()
