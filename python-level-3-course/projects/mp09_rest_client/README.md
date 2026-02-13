# MP09 – REST API Client

**PCPP Objectives**: 4.1, 4.2, 4.3, 4.4  
**Week**: 10  
**Related Modules**: M10

## Goal

Build a REST client that communicates with a web API using `requests` and handles JSON/XML.

## Requirements

- Create a REST client class that implements CRUD operations:
  - `get(resource, id=None)`: GET request to fetch data
  - `create(resource, data)`: POST request to create new resource
  - `update(resource, id, data)`: PUT request to update resource
  - `delete(resource, id)`: DELETE request to delete resource
- Handle JSON data:
  - Serialize Python objects to JSON for requests
  - Deserialize JSON responses to Python objects
  - Handle JSON errors gracefully
- Implement error handling:
  - Check HTTP status codes (2xx success, 4xx client error, 5xx server error)
  - Raise custom exceptions for different error types
  - Retry logic for transient failures (optional but encouraged)
- Use a real API or mock server:
  - JSONPlaceholder (https://jsonplaceholder.typicode.com) or similar
  - Or create a simple Flask/FastAPI mock server (extension)

## Acceptance Criteria

- All CRUD operations work correctly with the API
- JSON serialization/deserialization handles Python types correctly
- Error handling provides meaningful messages for different failure scenarios
- Code uses `requests` library appropriately (not raw sockets)
- Client class is reusable and well-documented

## File Structure

```
mp09_rest_client/
├── README.md
├── client.py          # REST client class
├── exceptions.py     # Custom exceptions
├── demo.py            # Demonstration script
└── tests.py           # Unit tests
```

## Suggested Extensions

- Add pagination support for list endpoints
- Implement authentication (API keys or OAuth tokens)
- Add request/response logging
- Parse XML responses (if API supports XML)
- Create a simple CLI interface to interact with the REST client

## Submission Checklist

- [ ] REST client class implemented
- [ ] CRUD operations work
- [ ] JSON handling correct
- [ ] Error handling comprehensive
- [ ] Code tested with real API
