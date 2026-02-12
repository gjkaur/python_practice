"""Demonstrate __name__ and simple package usage (PCAP 1.5)."""
# When run as script: __name__ == "__main__"
# When imported: __name__ == module name
print("This module's __name__ is:", __name__)

if __name__ == "__main__":
    print("Run as script: executing demo")
    # Simulate using a local "package": we are the module
    print("__name__ used for script vs import guard")
