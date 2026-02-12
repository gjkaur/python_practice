# STARTER SCRIPT FOR MP07 - Functional Refactor
# Refactor this into main.py + services/converters + validators. Preserve behavior.

print("Unit Converter")
print("--------------")
print("1) Celsius to Fahrenheit")
print("2) Fahrenheit to Celsius")
print("3) Kilometers to Miles")
print("4) Miles to Kilometers")
print("0) Exit")

choice = input("Choose an option: ").strip()

if choice == "1":
    raw = input("Enter value in Celsius: ")
    try:
        c = float(raw)
        result = c * 9.0 / 5.0 + 32.0
        print(f"Result: {result:.2f} F")
    except ValueError:
        print("Invalid number. Please try again.")
elif choice == "2":
    raw = input("Enter value in Fahrenheit: ")
    try:
        f = float(raw)
        result = (f - 32.0) * 5.0 / 9.0
        print(f"Result: {result:.2f} C")
    except ValueError:
        print("Invalid number. Please try again.")
elif choice == "3":
    raw = input("Enter distance in kilometers: ")
    try:
        km = float(raw)
        result = km * 0.621371
        print(f"Result: {result:.2f} miles")
    except ValueError:
        print("Invalid number. Please try again.")
elif choice == "4":
    raw = input("Enter distance in miles: ")
    try:
        miles = float(raw)
        result = miles / 0.621371
        print(f"Result: {result:.2f} km")
    except ValueError:
        print("Invalid number. Please try again.")
elif choice == "0":
    print("Goodbye.")
else:
    print("Invalid choice. Please try again.")
