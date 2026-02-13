"""
PCPP 1.1, 1.3: Practice Exercises - Advanced OOP Foundations

Complete the exercises below to practice OOP concepts.
"""


# Exercise 1: Create a class hierarchy
# TODO: Create a base class `Animal` with:
#   - Class variable `total_animals` (counter)
#   - Instance variables: `name`, `species`
#   - `__init__` method that increments `total_animals`
#   - `__str__` method returning "name (species)"

class Animal:
    """Base class for animals."""
    # TODO: Add class variable total_animals
    
    # TODO: Add __init__ method
    
    # TODO: Add __str__ method
    
    pass


# Exercise 2: Create subclasses
# TODO: Create `Dog` class inheriting from `Animal`
#   - Add instance variable `breed`
#   - Add method `bark()` returning "Woof!"

class Dog(Animal):
    """Dog class."""
    # TODO: Implement Dog class
    
    pass


# Exercise 3: Create another subclass
# TODO: Create `Cat` class inheriting from `Animal`
#   - Add method `meow()` returning "Meow!"

class Cat(Animal):
    """Cat class."""
    # TODO: Implement Cat class
    
    pass


# Exercise 4: Use reflection functions
def check_animal_types(animal: Animal) -> None:
    """Check the type of an animal using isinstance and issubclass.
    
    Args:
        animal: An Animal instance
    """
    # TODO: Use isinstance() to check if animal is Dog, Cat, or Animal
    # Print the results
    
    # TODO: Use issubclass() to check if Dog is subclass of Animal
    # Print the results
    
    pass


# Exercise 5: Demonstrate MRO
def show_inheritance_hierarchy() -> None:
    """Display the Method Resolution Order for Dog and Cat classes."""
    # TODO: Print Dog.__mro__
    # TODO: Print Cat.__mro__
    
    pass


# Exercise 6: Polymorphism
def make_animals_speak(animals: list[Animal]) -> None:
    """Demonstrate polymorphism - different animals make different sounds.
    
    Args:
        animals: List of Animal instances
    """
    # TODO: Iterate through animals
    # For each animal, check its type and call appropriate method (bark or meow)
    # Use isinstance() to check type
    
    pass


# Exercise 7: Composition
class Owner:
    """Owner class for composition example."""
    
    def __init__(self, name: str) -> None:
        """Initialize an Owner instance.
        
        Args:
            name: Owner's name
        """
        self.name = name


# TODO: Modify Dog class to include an Owner (composition)
# Add an `owner` attribute to Dog class
# Add a method `get_owner_name()` that returns owner's name


if __name__ == "__main__":
    # Test your implementations here
    
    # Create some animals
    # dog = Dog("Buddy", "Golden Retriever")
    # cat = Cat("Whiskers")
    
    # Test reflection
    # check_animal_types(dog)
    
    # Test MRO
    # show_inheritance_hierarchy()
    
    # Test polymorphism
    # animals = [dog, cat]
    # make_animals_speak(animals)
    
    print("Complete the exercises above!")
