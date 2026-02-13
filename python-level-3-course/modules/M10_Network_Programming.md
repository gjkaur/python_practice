# Module 10 – Network Programming & REST

**PCPP Objectives**: 4.1, 4.2, 4.3, 4.4

## Learning Objectives

- Understand network programming concepts (REST, sockets, protocols)
- Work with sockets using the `socket` module
- Serialize/deserialize JSON and XML data
- Build REST API clients using `requests`
- Handle HTTP methods (GET, POST, PUT, DELETE)
- Implement error handling for network operations

## Topics Covered

### Lesson 10.1 – Network Programming Fundamentals
- REST architecture
- Network sockets
- Domains, addresses, ports, protocols
- Connection-oriented vs connectionless

### Lesson 10.2 – Socket Programming
- `socket` module
- Creating sockets
- Connecting to servers
- Sending and receiving data

### Lesson 10.3 – Exception Handling in Network Programming
- Network exceptions
- Timeouts
- Retry logic

### Lesson 10.4 – JSON Serialization
- JSON syntax and structure
- `json` module: `dumps()`, `loads()`
- Serializing custom objects

### Lesson 10.5 – XML Processing
- XML syntax and structure; XML as a tree; DTD (Document Type Definition) as optional schema
- `xml.etree.ElementTree`
- Parsing and creating XML; building with `Element` and `SubElement`

### Lesson 10.6 – requests Module
- Basic HTTP methods
- Response objects
- Parameters and headers

### Lesson 10.7 – Building REST Clients
- CRUD operations
- Error handling
- Response parsing

## Key Concepts

- **REST**: Representational State Transfer, HTTP-based API architecture
- **Sockets**: Low-level network communication
- **JSON/XML**: Data exchange formats
- **requests**: High-level HTTP library

## Practice Exercises

See `practice/practice_10_networking.py`

## Examples

See `examples/network_demo.py`

## Related Mini Project

**MP09 – REST API Client** (Week 10)

## Next Module

**M11 – Database & File Processing** (PCPP 5.1, 5.2)
