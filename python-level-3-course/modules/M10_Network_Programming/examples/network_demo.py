"""
PCPP 4.1, 4.2, 4.3, 4.4: Network Programming & REST Demo

Demonstrates:
- Socket programming
- JSON serialization
- XML processing
- REST API clients with requests
"""

import json
import socket
import xml.etree.ElementTree as ET
from typing import Any, Dict
from urllib.parse import urlparse

import requests


# PCPP 4.2: Socket Programming
def socket_example() -> None:
    """PCPP 4.2: Basic socket example (HTTP request)."""
    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to HTTP server
        s.connect(("httpbin.org", 80))
        
        # Send HTTP GET request
        request = "GET /get HTTP/1.1\r\nHost: httpbin.org\r\n\r\n"
        s.send(request.encode())
        
        # Receive response
        response = s.recv(4096).decode()
        print("Socket response (first 200 chars):")
        print(response[:200])
    finally:
        s.close()


# PCPP 4.3: JSON Serialization
def json_example() -> None:
    """PCPP 4.3: JSON serialization and deserialization."""
    # Python dict to JSON string
    data = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "active": True
    }
    
    json_string = json.dumps(data, indent=2)
    print("JSON string:")
    print(json_string)
    
    # JSON string to Python dict
    parsed = json.loads(json_string)
    print(f"\nParsed data: {parsed}")
    
    # Custom object serialization
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
        
        def to_dict(self) -> Dict[str, Any]:
            return {"name": self.name, "age": self.age}
    
    person = Person("Bob", 25)
    person_json = json.dumps(person.to_dict())
    print(f"\nPerson JSON: {person_json}")


# PCPP 4.3: XML Processing
def xml_example() -> None:
    """PCPP 4.3: XML parsing and creation."""
    # Parse XML
    xml_string = """
    <users>
        <user id="1">
            <name>Alice</name>
            <email>alice@example.com</email>
        </user>
        <user id="2">
            <name>Bob</name>
            <email>bob@example.com</email>
        </user>
    </users>
    """
    
    root = ET.fromstring(xml_string)
    
    # Find elements
    users = root.findall('user')
    print("XML Users:")
    for user in users:
        name = user.find('name').text
        email = user.find('email').text
        print(f"  {name}: {email}")
    
    # Create XML
    new_root = ET.Element("products")
    product1 = ET.SubElement(new_root, "product")
    product1.set("id", "1")
    ET.SubElement(product1, "name").text = "Widget"
    ET.SubElement(product1, "price").text = "19.99"
    
    print("\nCreated XML:")
    ET.dump(new_root)


# PCPP 4.4: REST Client with requests
class RESTClient:
    """PCPP 4.4: Simple REST API client."""
    
    def __init__(self, base_url: str) -> None:
        """Initialize REST client.
        
        Args:
            base_url: Base URL for API
        """
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
    
    def get(self, endpoint: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
        """PCPP 4.4: GET request.
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            
        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()
    
    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """PCPP 4.4: POST request.
        
        Args:
            endpoint: API endpoint
            data: Request body data
            
        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """PCPP 4.4: PUT request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.put(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint: str) -> None:
        """PCPP 4.4: DELETE request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.delete(url)
        response.raise_for_status()


if __name__ == "__main__":
    print("=== JSON Example ===")
    json_example()
    
    print("\n=== XML Example ===")
    xml_example()
    
    print("\n=== REST Client Example ===")
    # Using httpbin.org for testing
    client = RESTClient("https://httpbin.org")
    
    try:
        # GET request
        response = client.get("/get", params={"test": "value"})
        print(f"GET response: {response.get('args', {})}")
        
        # POST request
        post_data = {"name": "Alice", "age": 30}
        post_response = client.post("/post", data=post_data)
        print(f"POST response data: {post_response.get('json', {})}")
    except requests.RequestException as e:
        print(f"Request error: {e}")
    
    print("\n=== Socket Example (commented - requires network) ===")
    # socket_example()  # Uncomment to test
