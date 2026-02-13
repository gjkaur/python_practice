# Module 9 – GUI Programming with tkinter

**PCPP Objectives**: 3.1, 3.2, 3.3

## Learning Objectives

- Understand GUI concepts and event-driven programming
- Create windows and widgets using tkinter
- Use layout managers (pack, grid, place)
- Handle events and callbacks
- Use observable variables (StringVar, IntVar)
- Build interactive GUI applications

## Topics Covered

### Lesson 9.1 – GUI Concepts and Event-Driven Programming
- GUI terminology and concepts
- Event-driven vs classical programming
- Widget toolkits

### Lesson 9.2 – tkinter Basics
- Creating windows: `Tk()`, `mainloop()`, `title()`
- Basic widgets: `Label`, `Button`, `Entry`, `Frame` (container for grouping widgets)
- Adding widgets to windows; closing windows: `destroy()` method
- Dialog boxes: `messagebox` for alerts, confirmations, and input dialogs

### Lesson 9.3 – Layout Managers
- `pack()`: simple automatic layout
- `grid()`: table-like layout
- `place()`: absolute positioning

### Lesson 9.4 – Event Handlers and Callbacks
- Command parameter for buttons
- Event binding: `bind()`
- Common events: `<Button-1>`, `<Key>`, `<Return>`

### Lesson 9.5 – Advanced Widgets
- `Canvas`: drawing area; coloring widgets using color modes: RGB (e.g. `#RRGGBB`), HEX (e.g. `'#ff0000'` for red)
- `Entry`, `Radiobutton`, `Checkbutton`, `Text`, `Listbox`

### Lesson 9.6 – Observable Variables
- `StringVar`, `IntVar`, `BooleanVar`
- Variable tracing
- Widget `textvariable` parameter

## Key Concepts

- **Event-Driven**: Program responds to user events, not sequential execution
- **Widgets**: GUI components (buttons, labels, entry fields)
- **Layout Managers**: Organize widgets in windows
- **Observable Variables**: Link widgets to data

## Practice Exercises

See `practice/practice_09_gui.py`

## Examples

See `examples/gui_demo.py`

## Related Mini Project

**MP08 – GUI Calculator or Todo App** (Week 9)

## Next Module

**M10 – Network Programming & REST** (PCPP 4.1, 4.2, 4.3, 4.4)
