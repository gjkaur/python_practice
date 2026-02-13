# Code Review Rubric – Level 3

Use this rubric for peer and instructor code reviews of mini projects and capstones.

## Review Categories

Each category can be rated as **Pass** / **Needs Work** / **Excellent**, with 1–2 sentences of feedback.

### 1. Readability & Style

- Uses PEP 8 naming, consistent indentation, appropriate comments/docstrings (PEP 257), type hints (PEP 484)
- Code is understandable without running it

**Pass**: Code follows PEP 8 and has basic docstrings.  
**Needs Work**: Violations of PEP 8, missing docstrings, or unclear code.  
**Excellent**: Exemplary adherence to PEP 8/257/484, self-documenting code.

### 2. Correctness & Edge Cases

- Implements specified behavior; considers typical edge cases
- No obvious logic flaws in core flows

**Pass**: Core functionality works; handles common edge cases.  
**Needs Work**: Logic errors or missing edge case handling.  
**Excellent**: Robust handling of edge cases, defensive programming.

### 3. OOP Design & Architecture

- Proper use of classes, inheritance, composition, encapsulation
- Magic methods used appropriately
- Design patterns applied where beneficial

**Pass**: Basic OOP structure; classes and methods used correctly.  
**Needs Work**: Poor OOP design, misuse of inheritance, missing encapsulation.  
**Excellent**: Sophisticated OOP design with appropriate patterns and abstractions.

### 4. Error Handling & Logging

- Uses specific exceptions instead of bare `except`
- Exception chaining where appropriate
- Logging for important events and errors

**Pass**: Basic exception handling; some logging.  
**Needs Work**: Bare `except`, no logging, or poor error messages.  
**Excellent**: Comprehensive exception handling with chaining, structured logging.

### 5. Testability & Tests

- Presence of pure functions and testable classes
- Tests are meaningful and cover important paths

**Pass**: Some tests present; core logic is testable.  
**Needs Work**: No tests or untestable code structure.  
**Excellent**: High test coverage with well-designed test cases.

### 6. PCPP Objective Coverage

- Explicit use of PCPP concepts (magic methods, decorators, abstract classes, etc.)

**Pass**: Uses required PCPP concepts correctly.  
**Needs Work**: Missing required concepts or incorrect usage.  
**Excellent**: Demonstrates mastery of PCPP concepts with advanced applications.

## Review Feedback Template

```
## Code Review for [Project Name]

### Strengths
- [Positive feedback]

### Areas for Improvement
- [Specific suggestions]

### PCPP Objective Coverage
- [List objectives covered and any missing]

### Overall Rating
[Pass / Needs Work / Excellent]

### Next Steps
- [Action items]
```

## Review Guidelines

- Be constructive and specific
- Reference PCPP objectives when relevant
- Provide code examples for suggestions when possible
- Focus on learning and improvement, not just criticism
