# Capstone 2 – REST Client with GUI Frontend

**PCPP Objectives**: All sections (1.1–5.2)  
**Duration**: 2-3 weeks  
**Weight**: 30% of final grade

## Goal

Build a REST API client with a GUI frontend that integrates networking, data persistence, and user interface.

## Project Description

Create a desktop application that acts as a client for a REST API (real or mock). The application should fetch data from an API, display it in a GUI, allow users to interact with the data, and persist data locally.

## Requirements

### Core Functionality

1. **REST Client** (PCPP 4.1–4.4):
   - Complete REST client class with CRUD operations
   - Handle JSON serialization/deserialization
   - Implement error handling for HTTP errors
   - Retry logic for transient failures
   - Custom exceptions for different error types

2. **GUI Frontend** (PCPP 3.1–3.3):
   - Main window displaying API data
   - Forms for creating/editing resources
   - List view or table displaying multiple resources
   - Buttons for CRUD operations
   - Status indicators (loading, success, error)
   - Use observable variables for data binding

3. **Data Persistence** (PCPP 5.1):
   - SQLite database for caching API data
   - Sync between local database and API
   - Handle offline mode (use cached data)
   - Implement data refresh functionality

4. **OOP Design** (PCPP 1.1–1.12):
   - Proper class hierarchy
   - Use decorators for cross-cutting concerns (logging, caching)
   - Abstract base classes if appropriate
   - Magic methods for data classes
   - Properties for encapsulation

5. **Error Handling** (PCPP 1.9):
   - Exception chaining for API errors
   - User-friendly error messages in GUI
   - Logging of errors with tracebacks

6. **Logging** (PCPP 5.2):
   - Log all API requests/responses
   - Log errors and exceptions
   - Log user actions
   - File and console handlers

7. **Configuration** (PCPP 5.2):
   - API base URL in config file
   - API keys/tokens in config (or environment variables)
   - Application settings

### Optional Advanced Features

- XML support (if API supports XML)
- Request/response caching with TTL
- Pagination support for list endpoints
- Search/filter functionality
- Export data to CSV/JSON
- Authentication (API keys, OAuth)

## Architecture

Suggested structure:

- **Client Layer**: REST API client
- **Model Layer**: Data models matching API resources
- **Service Layer**: Business logic, sync between API and database
- **View Layer**: GUI components
- **Storage Layer**: Local database for caching

## File Structure

```
capstone2_rest_gui/
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── config.ini            # Configuration file
├── main.py              # Application entry point
├── api/                 # REST client
│   ├── __init__.py
│   ├── client.py        # REST client class
│   └── exceptions.py    # API exceptions
├── models/              # Data models
│   ├── __init__.py
│   └── resource.py      # Resource classes
├── services/            # Business logic
│   ├── __init__.py
│   └── sync_service.py  # Sync API and database
├── database/            # Local storage
│   ├── __init__.py
│   └── cache.py         # Database cache
├── gui/                 # GUI layer
│   ├── __init__.py
│   ├── main_window.py   # Main window
│   ├── resource_form.py # Create/edit form
│   └── resource_list.py # List view
├── utils/               # Utilities
│   ├── __init__.py
│   ├── logging_config.py
│   └── config.py
└── tests/               # Unit tests
```

## API Suggestions

- **JSONPlaceholder**: https://jsonplaceholder.typicode.com (posts, users, todos)
- **ReqRes**: https://reqres.in (users)
- **GitHub API**: https://api.github.com (repositories, users)
- **OpenWeatherMap**: https://openweathermap.org/api (weather data)
- **Mock Server**: Create your own with Flask/FastAPI

## Acceptance Criteria

- [ ] REST client successfully communicates with API
- [ ] GUI displays data from API
- [ ] CRUD operations work through GUI
- [ ] Data is cached locally in database
- [ ] Error handling provides user-friendly messages
- [ ] Logging captures all important events
- [ ] Configuration file is used correctly
- [ ] Code follows PEP standards
- [ ] Application handles network failures gracefully
- [ ] README includes setup and usage instructions

## Submission Requirements

1. **Source Code**: Complete, working application
2. **README.md**: 
   - Project description
   - API used and endpoints
   - Installation instructions
   - Usage guide
   - Architecture overview
3. **Documentation**: Docstrings for all public APIs
4. **Tests**: Unit tests for REST client and models
5. **Git History**: Meaningful commit history

## Evaluation Rubric

See `assessments/final_practical.md` for detailed rubric.

**Key Areas**:
- Functionality (25%)
- REST Client Implementation (20%)
- GUI Integration (15%)
- Error Handling (15%)
- Code Quality (10%)
- Testing (10%)
- Documentation (5%)

## Suggested Timeline

- **Week 1**: REST client, API integration, data models
- **Week 2**: GUI implementation, database caching
- **Week 3**: Integration, error handling, testing, documentation

## Tips

- Start with a simple API (JSONPlaceholder is great for learning)
- Test REST client independently before integrating with GUI
- Implement caching early to handle API rate limits
- Use logging to debug API communication issues
- Handle network errors gracefully (timeouts, connection errors)
- Consider API rate limits in your design

Good luck!
