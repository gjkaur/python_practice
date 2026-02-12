"""Demonstrate inheritance, isinstance, override, __str__ (PCAP 4.5)."""

class Animal:
    def __init__(self, name: str):
        self.name = name
    def speak(self) -> str:
        return "?"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof"
    def __str__(self) -> str:
        return f"Dog({self.name})"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow"

# Polymorphism
animals = [Dog("Rex"), Cat("Felix")]
for a in animals:
    print(a.name, a.speak())
    print("isinstance(a, Animal) =", isinstance(a, Animal))

d = Dog("Rex")
print(str(d))
