"""
PCPP 1.1, 1.3: Advanced OOP Foundations Demo

Demonstrates:
- OOP terminology and reflection (isinstance, issubclass)
- Class variables vs instance variables
- Inheritance hierarchies
- Method Resolution Order (MRO)
- Polymorphism and composition
"""


# PCPP 1.1: OOP Terminology and Reflection
class Vehicle:
    """Base class demonstrating class variables and instance variables."""
    
    # Class variable: shared across all instances
    total_vehicles = 0
    
    def __init__(self, make: str, model: str, year: int) -> None:
        """Initialize a Vehicle instance.
        
        Args:
            make: Manufacturer name
            model: Model name
            year: Manufacturing year
        """
        # Instance variables: unique to each instance
        self.make = make
        self.model = model
        self.year = year
        
        # Increment class variable
        Vehicle.total_vehicles += 1
    
    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self) -> str:
        """Developer-friendly string representation."""
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"


# PCPP 1.3: Inheritance
class Car(Vehicle):
    """Car class inheriting from Vehicle."""
    
    def __init__(self, make: str, model: str, year: int, doors: int = 4) -> None:
        """Initialize a Car instance.
        
        Args:
            make: Manufacturer name
            model: Model name
            year: Manufacturing year
            doors: Number of doors (default: 4)
        """
        super().__init__(make, model, year)
        self.doors = doors
    
    def honk(self) -> str:
        """Make the car honk."""
        return "Beep beep!"


class Motorcycle(Vehicle):
    """Motorcycle class inheriting from Vehicle."""
    
    def __init__(self, make: str, model: str, year: int, engine_size: float) -> None:
        """Initialize a Motorcycle instance.
        
        Args:
            make: Manufacturer name
            model: Model name
            year: Manufacturing year
            engine_size: Engine size in cubic centimeters
        """
        super().__init__(make, model, year)
        self.engine_size = engine_size
    
    def rev_engine(self) -> str:
        """Rev the motorcycle engine."""
        return "Vroom vroom!"


# PCPP 1.3: Multiple Inheritance
class Flyable:
    """Mixin class for flying capability."""
    
    def fly(self) -> str:
        """Make the object fly."""
        return "Flying through the air!"


class FlyingVehicle(Vehicle, Flyable):
    """Vehicle that can fly - demonstrates multiple inheritance."""
    
    def __init__(self, make: str, model: str, year: int, max_altitude: int) -> None:
        """Initialize a FlyingVehicle instance.
        
        Args:
            make: Manufacturer name
            model: Model name
            year: Manufacturing year
            max_altitude: Maximum altitude in feet
        """
        super().__init__(make, model, year)
        self.max_altitude = max_altitude


# PCPP 1.3: Composition vs Inheritance
class Engine:
    """Engine class - used for composition."""
    
    def __init__(self, horsepower: int) -> None:
        """Initialize an Engine instance.
        
        Args:
            horsepower: Engine horsepower
        """
        self.horsepower = horsepower
    
    def start(self) -> str:
        """Start the engine."""
        return f"Engine started ({self.horsepower} HP)"


class VehicleWithEngine(Vehicle):
    """Vehicle with engine - demonstrates composition (has a) vs inheritance (is a)."""
    
    def __init__(self, make: str, model: str, year: int, engine: Engine) -> None:
        """Initialize a VehicleWithEngine instance.
        
        Args:
            make: Manufacturer name
            model: Model name
            year: Manufacturing year
            engine: Engine instance (composition)
        """
        super().__init__(make, model, year)
        self.engine = engine  # Composition: "has a" relationship
    
    def start(self) -> str:
        """Start the vehicle's engine."""
        return self.engine.start()


# PCPP 1.1: Reflection functions
def demonstrate_reflection() -> None:
    """Demonstrate isinstance() and issubclass() functions."""
    car = Car("Toyota", "Camry", 2023)
    motorcycle = Motorcycle("Honda", "CBR", 2023, 600.0)
    flying_car = FlyingVehicle("Terrafugia", "Transition", 2023, 10000)
    
    # isinstance() - check if object is instance of class
    print("=== isinstance() Examples ===")
    print(f"car is Vehicle: {isinstance(car, Vehicle)}")
    print(f"car is Car: {isinstance(car, Car)}")
    print(f"car is Motorcycle: {isinstance(car, Motorcycle)}")
    print(f"car is (Car, Motorcycle): {isinstance(car, (Car, Motorcycle))}")
    
    # issubclass() - check if class is subclass of another
    print("\n=== issubclass() Examples ===")
    print(f"Car is subclass of Vehicle: {issubclass(Car, Vehicle)}")
    print(f"Car is subclass of Motorcycle: {issubclass(Car, Motorcycle)}")
    print(f"FlyingVehicle is subclass of (Vehicle, Flyable): {issubclass(FlyingVehicle, (Vehicle, Flyable))}")


# PCPP 1.3: Method Resolution Order (MRO)
def demonstrate_mro() -> None:
    """Demonstrate Method Resolution Order."""
    print("\n=== Method Resolution Order (MRO) ===")
    print(f"Vehicle MRO: {Vehicle.__mro__}")
    print(f"Car MRO: {Car.__mro__}")
    print(f"FlyingVehicle MRO: {FlyingVehicle.__mro__}")
    
    # Using mro() method
    print(f"\nCar.mro(): {Car.mro()}")


# PCPP 1.3: Polymorphism
def demonstrate_polymorphism(vehicles: list[Vehicle]) -> None:
    """Demonstrate polymorphism - function works with any Vehicle subclass.
    
    Args:
        vehicles: List of Vehicle instances (or subclasses)
    """
    print("\n=== Polymorphism Example ===")
    for vehicle in vehicles:
        print(f"{vehicle}: {type(vehicle).__name__}")
        # All vehicles have __str__ method (polymorphism)


if __name__ == "__main__":
    # Demonstrate class variables vs instance variables
    print("=== Class Variables vs Instance Variables ===")
    v1 = Vehicle("Ford", "F-150", 2022)
    v2 = Vehicle("Chevrolet", "Silverado", 2023)
    
    print(f"Vehicle.total_vehicles: {Vehicle.total_vehicles}")
    print(f"v1.total_vehicles: {v1.total_vehicles}")
    print(f"v2.total_vehicles: {v2.total_vehicles}")
    
    # Modify class variable
    Vehicle.total_vehicles = 100
    print(f"\nAfter Vehicle.total_vehicles = 100:")
    print(f"v1.total_vehicles: {v1.total_vehicles}")
    print(f"v2.total_vehicles: {v2.total_vehicles}")
    
    # Demonstrate reflection
    demonstrate_reflection()
    
    # Demonstrate MRO
    demonstrate_mro()
    
    # Demonstrate polymorphism
    vehicles = [
        Car("Toyota", "Camry", 2023),
        Motorcycle("Honda", "CBR", 2023, 600.0),
        FlyingVehicle("Terrafugia", "Transition", 2023, 10000)
    ]
    demonstrate_polymorphism(vehicles)
    
    # Demonstrate composition
    print("\n=== Composition Example ===")
    engine = Engine(300)
    vehicle_with_engine = VehicleWithEngine("BMW", "M3", 2023, engine)
    print(vehicle_with_engine.start())
