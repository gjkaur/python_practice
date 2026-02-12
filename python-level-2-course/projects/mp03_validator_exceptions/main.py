"""CLI: validate input and catch custom exceptions."""
from validators import validate_non_empty, validate_int
from exceptions import ValidationError, RequiredError, FormatError

def main():
    try:
        name = input("Name (required): ").strip()
        validate_non_empty(name, "Name")
        age_str = input("Age (integer): ").strip()
        age = validate_int(age_str, "Age")
        print(f"OK: {name}, {age}")
    except RequiredError as e:
        print("RequiredError:", e.args)
    except FormatError as e:
        print("FormatError:", e.args)
    except ValidationError as e:
        print("ValidationError:", e.args)

if __name__ == "__main__":
    main()
