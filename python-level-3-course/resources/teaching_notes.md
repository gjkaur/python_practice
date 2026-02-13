# Level 3 Teaching Notes

## Course Delivery Guidelines

### Pacing

- **Weeks 1–5**: Focus on OOP mastery (foundational for rest of course)
- **Weeks 6–7**: Advanced topics (exceptions, serialization, metaprogramming)
- **Week 8**: Code quality standards (important before capstones)
- **Weeks 9–11**: Applied topics (GUI, networking, databases)
- **Week 12**: Integration and capstone completion

### Key Teaching Moments

#### Module 1 (OOP Foundations)
- **Critical**: Ensure students understand MRO before moving to magic methods
- **Common confusion**: Class variables vs instance variables (use visual diagrams)
- **Practice**: Have students trace MRO for complex inheritance hierarchies

#### Module 2 (Magic Methods)
- **Critical**: Emphasize when to use magic methods (not always necessary)
- **Common mistake**: Forgetting to return `NotImplemented` for unsupported types
- **Practice**: Convert existing classes to use magic methods

#### Module 3 (Decorators)
- **Critical**: Three-level function pattern for decorators with arguments
- **Common confusion**: Execution time (definition) vs call time
- **Practice**: Build decorators incrementally (simple → with args → class-based)

#### Module 9 (GUI)
- **Critical**: Event-driven programming model (different from sequential)
- **Common issue**: Blocking operations freezing GUI (use `after()` or threading)
- **Practice**: Convert CLI apps to GUI step-by-step

#### Module 10 (Networking)
- **Critical**: Error handling for network operations (many failure modes)
- **Common mistake**: Not checking status codes
- **Practice**: Build REST client incrementally (basic → error handling → features)

### Common Misconceptions

1. **Magic Methods**: Students think they're always needed – teach when they add value
2. **Inheritance**: Overused – emphasize composition when appropriate
3. **Decorators**: Confusion about execution time – use live coding to demonstrate
4. **GUI**: Blocking operations – must emphasize async patterns
5. **Databases**: Forgetting transactions – emphasize data integrity

### Assessment Tips

- **Midterm (Week 6)**: Focus on OOP concepts – ensure students can design hierarchies
- **Code Reviews**: Use rubrics consistently – provide specific, actionable feedback
- **Capstones**: Check progress early (Week 9) – don't wait until Week 12

### Resources for Students

- Python documentation (official)
- PEP 8, PEP 257, PEP 484 (code standards)
- tkinter tutorial (official Python docs)
- requests library documentation
- SQLite Python tutorial

### Troubleshooting

**Issue**: Students struggling with MRO  
**Solution**: Use `ClassName.__mro__` visualization, step through method calls

**Issue**: GUI freezing  
**Solution**: Demonstrate `root.after()` for periodic tasks, threading for blocking I/O

**Issue**: Decorator confusion  
**Solution**: Build from scratch, show equivalent non-decorator code

**Issue**: Database connection errors  
**Solution**: Emphasize proper connection management, use context managers

### Capstone Guidance

- **Week 8**: Review proposals – ensure scope is appropriate
- **Week 9**: Check architecture – ensure proper separation of concerns
- **Week 10**: Review progress – identify blockers early
- **Week 11**: Final review – provide last-minute feedback
- **Week 12**: Presentations – celebrate achievements

### Professional Practices Emphasis

Throughout the course, reinforce:

- **PEP 8**: Code style consistency
- **PEP 257**: Documentation standards
- **PEP 484**: Type hints for maintainability
- **Error Handling**: User-friendly messages, proper logging
- **Testing**: Unit tests for core logic
- **Git**: Meaningful commits, clean history

These practices are not optional – they're professional requirements.
