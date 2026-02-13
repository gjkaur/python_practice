# MP08 – GUI Calculator or Todo App

**PCPP Objectives**: 3.1, 3.2, 3.3  
**Week**: 9  
**Related Modules**: M09

## Goal

Build a functional GUI application using tkinter with event-driven programming.

## Requirements

Create a GUI application (choose one):

**Option A: Calculator**
- Basic operations (+, -, *, /) and clear/reset
- Display area for numbers and results
- Number buttons (0-9)
- Operation buttons
- Equals button

**Option B: Todo List App**
- Add todo items
- Delete todo items
- Mark items as complete
- List display of all todos

GUI must include:
- Main window with title and proper sizing
- At least 5 different widget types: `Label`, `Button`, `Entry`, `Listbox` or `Text`, and one of `Radiobutton`/`Checkbutton`
- Use `grid()` layout manager (primary) with proper spacing
- Event handlers for all interactive elements
- Observable variables: Use `StringVar` or `IntVar` for at least one widget
- Input validation and error handling: Validate user input, display user-friendly error messages in GUI

## Acceptance Criteria

- Application launches and displays correctly
- All buttons and interactions work as expected
- Input validation prevents invalid operations
- Error messages displayed in GUI (e.g., messagebox or label)
- Code is organized: separate GUI setup from event handlers
- Application closes cleanly

## File Structure

```
mp08_gui_app/
├── README.md
├── main.py            # Application entry point
├── gui.py             # GUI setup and widgets
├── handlers.py        # Event handlers
└── validators.py      # Input validation (optional)
```

## Suggested Extensions

- Add keyboard shortcuts (e.g., Enter to calculate/submit)
- Implement a menu bar with File/Edit menus
- Add a settings dialog using `Toplevel` window
- Use `Canvas` widget to draw something (e.g., graph for calculator history)

## Submission Checklist

- [ ] GUI application works correctly
- [ ] At least 5 widget types used
- [ ] Grid layout manager used
- [ ] Observable variables implemented
- [ ] Input validation and error handling
- [ ] Code organized and documented
