"""
PCPP 1.7, 1.8: Encapsulation & Built-in Subclassing Demo
"""


# PCPP 1.7: Attribute Encapsulation
class Temperature:
    """Temperature class demonstrating property decorator."""
    
    def __init__(self, celsius: float) -> None:
        """Initialize temperature.
        
        Args:
            celsius: Temperature in Celsius
        """
        self._celsius = celsius  # Private attribute (convention)
    
    @property
    def celsius(self) -> float:
        """PCPP 1.7: Getter for Celsius temperature."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float) -> None:
        """PCPP 1.7: Setter with validation."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @celsius.deleter
    def celsius(self) -> None:
        """PCPP 1.7: Deleter."""
        print("Deleting temperature")
        self._celsius = 0
    
    @property
    def fahrenheit(self) -> float:
        """Computed property - read-only."""
        return self._celsius * 9/5 + 32


# PCPP 1.8: Subclassing Built-in Classes
class UniqueList(list):
    """PCPP 1.8: List subclass that prevents duplicates."""
    
    def append(self, item: object) -> None:
        """Override append to prevent duplicates."""
        if item not in self:
            super().append(item)
    
    def extend(self, iterable: object) -> None:
        """Override extend to prevent duplicates."""
        for item in iterable:
            if item not in self:
                super().append(item)


class CaseInsensitiveDict(dict):
    """PCPP 1.8: Dict subclass with case-insensitive keys."""
    
    def __getitem__(self, key: str) -> object:
        """Override getitem for case-insensitive lookup."""
        key_lower = key.lower()
        for k, v in self.items():
            if k.lower() == key_lower:
                return v
        raise KeyError(key)
    
    def __setitem__(self, key: str, value: object) -> None:
        """Override setitem to store lowercase key."""
        # Remove any existing key with same lowercase
        keys_to_remove = [k for k in self.keys() if k.lower() == key.lower()]
        for k in keys_to_remove:
            del self[k]
        super().__setitem__(key.lower(), value)


if __name__ == "__main__":
    print("=== Encapsulation ===")
    temp = Temperature(25)
    print(f"Celsius: {temp.celsius}")
    print(f"Fahrenheit: {temp.fahrenheit}")
    
    temp.celsius = 30
    print(f"Updated Celsius: {temp.celsius}")
    
    print("\n=== Built-in Subclassing ===")
    unique_list = UniqueList([1, 2, 3])
    unique_list.append(2)  # Won't add duplicate
    unique_list.append(4)
    print(f"UniqueList: {unique_list}")
    
    case_dict = CaseInsensitiveDict()
    case_dict["Name"] = "Alice"
    case_dict["name"] = "Bob"  # Overwrites previous
    print(f"CaseInsensitiveDict: {case_dict}")
    print(f"case_dict['NAME']: {case_dict['NAME']}")
