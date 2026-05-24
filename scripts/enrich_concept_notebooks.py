"""Add supplementary example cells to M##_Concepts.ipynb notebooks."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "**Additional Example**"

ENRICHMENTS: dict[str, dict[int | str, list[tuple[str, str]]]] = {
    # ── Level 1 ──────────────────────────────────────────────────────────
    "python-level-1-course/modules/M01_Foundations_and_Tooling/M01_Concepts.ipynb": {
        1: [("**Additional Example**: Compare script vs interactive execution.", "print('Running in notebook — same as a .py script line by line')\nprint(2 + 2)")],
        2: [("**Additional Example**: Syntax vs semantics — valid syntax, runtime semantics.", "# Syntax OK; semantics: division by zero raises ZeroDivisionError\ntry:\n    result = 1 / 0\nexcept ZeroDivisionError as e:\n    print('Semantic error caught:', type(e).__name__)")],
        3: [("**Additional Example**: Valid identifiers and keyword check.", "import keyword\nnames = ['total_count', '_private', 'score2', '2bad']\nfor name in names:\n    valid = name.isidentifier() and not keyword.iskeyword(name)\n    print(f'{name!r}: valid={valid}')")],
        4: [("**Additional Example**: Indentation defines blocks.", "x = 10\nif x > 5:\n    print('Indented block runs')\n    print('Still inside if')\nprint('Back at top level')")],
        5: [("**Additional Example**: Single-line and block comments.", "# This is a comment\nvalue = 42  # inline comment\nprint(value)  # output: 42")],
        6: [("**Additional Example**: `__name__` guard pattern.", "def main():\n    print('App started')\n\nprint('__name__ is:', __name__)\nif __name__ == '__main__':\n    main()")],
        7: [("**Additional Example**: PEP 8 naming styles.", "MAX_ITEMS = 100      # CONSTANT\ndef calculate_total():  # function\n    user_name = 'Ada'    # variable\n    return user_name\nprint(calculate_total())")],
        8: [("**Additional Example**: Built-ins `len`, `type`, `print`.", "items = [10, 20, 30]\nprint('len:', len(items))\nprint('type:', type(items))\nprint('sum via built-in:', sum(items))")],
        9: [("**Additional Example**: Module introspection with `dir()`.", "import math\nprint('math.pi:', round(math.pi, 4))\nprint('Some math names:', [n for n in dir(math) if not n.startswith('_')][:6])")],
        10: [("**Additional Example**: Reading a traceback message.", "def divide(a, b):\n    return a / b\n\ntry:\n    divide(10, 0)\nexcept ZeroDivisionError as e:\n    print('Error type:', type(e).__name__)\n    print('Message:', e)")],
    },
    "python-level-1-course/modules/M02_Data_Types_and_Operators/M02_Concepts.ipynb": {
        1: [("**Additional Example**: Mixing types in expressions.", "count = 3\nlabel = 'items'\nprint(str(count) + ' ' + label)\nprint(isinstance(3.0, float), isinstance(3, int))")],
        2: [("**Additional Example**: Raw strings and escapes.", "path = r'C:\\Users\\data'\nprint('Raw:', path)\nprint('Tab:', 'a\\tb')\nprint('Newline:', 'line1\\nline2')")],
        3: [("**Additional Example**: Chained conversion.", "raw = '3.14'\nprint(float(raw), int(float(raw)))\nprint(bool('0'), bool(0))  # non-empty str is truthy")],
        4: [("**Additional Example**: String repetition and floor division.", "print('ha' * 3)\nprint('17 // 5 =', 17 // 5, '17 % 5 =', 17 % 5)")],
        5: [("**Additional Example**: Chained comparisons and short-circuit.", "n = 15\nprint(10 <= n <= 20)  # chained comparison\nprint('and short-circuit:', False and print('skipped'))")],
        6: [("**Additional Example**: Bit flags with AND/OR.", "READ, WRITE, EXEC = 1, 2, 4\nperms = READ | WRITE\nprint('has READ:', bool(perms & READ))\nprint('has EXEC:', bool(perms & EXEC))")],
        7: [("**Additional Example**: Parentheses clarify precedence.", "print('not True and False:', not True and False)\nprint('not (True and False):', not (True and False))")],
        8: [("**Additional Example**: Bulk pricing with min/max.", "prices = [9.99, 14.50, 7.25, 22.00]\nprint('cheapest:', min(prices), 'total:', round(sum(prices), 2))")],
        9: [("**Additional Example**: Formatted print output.", "name, score = 'Ada', 87\nprint(f'{name} scored {score}%')\nprint('{} scored {}%'.format(name, score))")],
    },
    "python-level-1-course/modules/M03_Control_Flow_and_Loops/M03_Concepts.ipynb": {
        1: [("**Additional Example**: if / elif / else chain.", "score = 85\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelse:\n    grade = 'C'\nprint(f'Score {score} -> {grade}')")],
        2: [("**Additional Example**: Nested conditionals.", "age, has_ticket = 16, True\nif age >= 18:\n    print('Adult entry')\nelif has_ticket and age >= 13:\n    print('Teen with ticket')\nelse:\n    print('No entry')")],
        3: [("**Additional Example**: while loop with counter.", "n = 3\nwhile n > 0:\n    print('countdown:', n)\n    n -= 1\nprint('liftoff!')")],
        4: [("**Additional Example**: for loop over a string.", "word = 'Python'\nfor ch in word:\n    print(ch, end=' ')\nprint()")],
        5: [("**Additional Example**: break exits early.", "for i in range(10):\n    if i == 5:\n        break\n    print(i, end=' ')\nprint('(stopped at 5)')")],
        6: [("**Additional Example**: continue skips iteration.", "for n in range(1, 6):\n    if n % 2 == 0:\n        continue\n    print(n, end=' ')\nprint('(odds only)')")],
        7: [("**Additional Example**: else on a for-loop (no break).", "for x in [2, 4, 6]:\n    if x % 2:\n        break\nelse:\n    print('All numbers were even')")],
        8: [("**Additional Example**: Simple menu loop pattern.", "choice = '2'  # simulate user picking option 2\nif choice == '1':\n    print('View items')\nelif choice == '2':\n    print('Add item')\nelse:\n    print('Invalid choice')")],
        9: [("**Additional Example**: Accumulator in a loop.", "total = 0\nfor price in [10, 20, 15]:\n    total += price\nprint('Cart total:', total)")],
    },
    "python-level-1-course/modules/M04_Collections_Lists_Tuples_Dicts/M04_Concepts.ipynb": {
        1: [("**Additional Example**: List creation and indexing.", "nums = [10, 20, 30, 40]\nprint('first:', nums[0], 'last:', nums[-1])\nprint('slice [1:3]:', nums[1:3])")],
        2: [("**Additional Example**: Tuple unpacking.", "point = (3, 4)\nx, y = point\nprint(f'x={x}, y={y}')\nprint('tuple is immutable — len:', len(point))")],
        3: [("**Additional Example**: Dict get with default.", "user = {'name': 'Ada', 'role': 'dev'}\nprint(user.get('name'))\nprint(user.get('email', 'none@example.com'))")],
        4: [("**Additional Example**: List methods append and pop.", "tasks = ['read', 'code']\ntasks.append('test')\nprint('after append:', tasks)\ndone = tasks.pop()\nprint('popped:', done, 'remaining:', tasks)")],
        5: [("**Additional Example**: Iterate dict items.", "scores = {'Ada': 90, 'Bob': 85}\nfor name, score in scores.items():\n    print(f'{name}: {score}')")],
        6: [("**Additional Example**: List comprehension basics.", "squares = [n * n for n in range(1, 6)]\nprint('squares:', squares)\nevens = [n for n in range(10) if n % 2 == 0]\nprint('evens:', evens)")],
        7: [("**Additional Example**: Copy vs alias.", "a = [1, 2, 3]\nb = a          # alias — same list\nb.append(4)\nprint('a after b.append(4):', a)\nc = list(a)    # shallow copy\nc.append(99)\nprint('a unchanged:', a, '| c:', c)")],
        8: [("**Additional Example**: Nested collection access.", "students = [{'name': 'Ada', 'grades': [90, 88]}, {'name': 'Bob', 'grades': [75, 80]}]\nprint(students[0]['grades'][1])")],
        9: [("**Additional Example**: Sort a list of numbers.", "data = [30, 10, 20]\ndata.sort()\nprint('sorted:', data)\nprint('sorted copy:', sorted([30, 10, 20]))")],
    },
    "python-level-1-course/modules/M05_Strings_and_Text_Processing/M05_Concepts.ipynb": {
        1: [("**Additional Example**: String indexing and slicing.", "s = 'Python'\nprint(s[0], s[-1], s[2:5])")],
        2: [("**Additional Example**: Case conversion methods.", "msg = 'Hello World'\nprint(msg.lower(), msg.upper(), msg.title())")],
        3: [("**Additional Example**: split and join.", "csv = 'apple,banana,cherry'\nfruits = csv.split(',')\nprint('split:', fruits)\nprint('join:', ' | '.join(fruits))")],
        4: [("**Additional Example**: strip whitespace.", "raw = '  hello  \\n'\nprint(repr(raw.strip()))\nprint(repr(raw.lstrip()))")],
        5: [("**Additional Example**: find and replace.", "text = 'one two one'\nprint('find one:', text.find('one'))\nprint('replace:', text.replace('one', '1'))")],
        6: [("**Additional Example**: f-string formatting.", "item, price = 'book', 19.99\nprint(f'{item}: ${price:.2f}')")],
        7: [("**Additional Example**: Character membership.", "word = 'code'\nprint('c' in word, 'z' in word)\nprint(''.join(reversed(word)))")],
        8: [("**Additional Example**: startswith / endswith.", "filename = 'report_2024.txt'\nprint(filename.startswith('report'), filename.endswith('.txt'))")],
        9: [("**Additional Example**: Parse a simple log line.", "line = '2024-01-15 ERROR: disk full'\nparts = line.split(' ', 2)\ndate, level_msg = parts[0], parts[1]\nprint(date, level_msg)")],
    },
    "python-level-1-course/modules/M06_Functions_and_Program_Design/M06_Concepts.ipynb": {
        1: [("**Additional Example**: Simple function with return.", "def area(width, height):\n    return width * height\n\nprint('area(4, 5):', area(4, 5))")],
        2: [("**Additional Example**: Implicit None return.", "def log(msg):\n    print('[LOG]', msg)\n\nresult = log('started')\nprint('Return value:', result)")],
        3: [("**Additional Example**: Positional vs keyword args.", "def connect(host, port=8080, ssl=False):\n    return f'{host}:{port} ssl={ssl}'\n\nprint(connect('localhost'))\nprint(connect(port=443, host='api.example.com', ssl=True))")],
        4: [("**Additional Example**: Local vs global (read-only).", "tax_rate = 0.2\n\ndef add_tax(amount):\n    return amount * (1 + tax_rate)  # reads global, no global keyword needed\n\nprint(add_tax(100))")],
        5: [("**Additional Example**: Docstring and help.", "def median(values):\n    \"\"\"Return middle value of a sorted list (simple odd-length case).\"\"\"\n    s = sorted(values)\n    return s[len(s) // 2]\n\nprint(median.__doc__)\nprint(median([3, 1, 2]))")],
    },
    "python-level-1-course/modules/M07_Exceptions_and_Defensive_Programming/M07_Concepts.ipynb": {
        1: [("**Additional Example**: try/except for ValueError.", "raw = 'abc'\ntry:\n    n = int(raw)\nexcept ValueError:\n    print(f'Cannot convert {raw!r} to int')")],
        2: [("**Additional Example**: except specific type first.", "try:\n    items = []\n    print(items[0])\nexcept IndexError:\n    print('List index out of range')\nexcept Exception:\n    print('Other error')")],
        3: [("**Additional Example**: else runs when no exception.", "try:\n    n = int('42')\nexcept ValueError:\n    print('bad input')\nelse:\n    print('Parsed successfully:', n)")],
        4: [("**Additional Example**: finally always runs.", "try:\n    f = open('nonexistent_file_xyz.txt')\nexcept FileNotFoundError:\n    print('File missing')\nfinally:\n    print('Cleanup block executed')")],
        5: [("**Additional Example**: raise with message.", "def set_age(age):\n    if age < 0:\n        raise ValueError('age must be non-negative')\n    return age\n\ntry:\n    set_age(-1)\nexcept ValueError as e:\n    print(e)")],
        6: [("**Additional Example**: Defensive input validation helper.", "def parse_positive_int(text):\n    try:\n        n = int(text)\n    except ValueError:\n        return None\n    return n if n > 0 else None\n\nprint(parse_positive_int('10'), parse_positive_int('-3'), parse_positive_int('x'))")],
        7: [("**Additional Example**: Exception as part of API contract.", "def divide(a, b):\n    if b == 0:\n        raise ZeroDivisionError('divisor is zero')\n    return a / b\n\nprint(divide(10, 2))\ntry:\n    divide(10, 0)\nexcept ZeroDivisionError as e:\n    print('Caught:', e)")],
    },
    "python-level-1-course/modules/M08_Intro_File_IO_and_Simple_CLI_Patterns/M08_Concepts.ipynb": {
        1: [("**Additional Example**: Write and read a text file with `with`.", "from pathlib import Path\np = Path('_demo_notebook.txt')\np.write_text('line1\\nline2\\n', encoding='utf-8')\nprint(p.read_text(encoding='utf-8'))\np.unlink(missing_ok=True)")],
        2: [("**Additional Example**: Read lines into a list.", "from pathlib import Path\np = Path('_lines_demo.txt')\np.write_text('alpha\\nbeta\\ngamma\\n', encoding='utf-8')\nlines = p.read_text(encoding='utf-8').splitlines()\nprint(lines)\np.unlink(missing_ok=True)")],
        3: [("**Additional Example**: JSON load and dump.", "import json\nfrom pathlib import Path\np = Path('_data_demo.json')\ndata = {'name': 'Ada', 'scores': [90, 88]}\np.write_text(json.dumps(data, indent=2), encoding='utf-8')\nloaded = json.loads(p.read_text(encoding='utf-8'))\nprint(loaded)\np.unlink(missing_ok=True)")],
        4: [("**Additional Example**: Handle missing file gracefully.", "from pathlib import Path\np = Path('_missing_demo.txt')\ntry:\n    text = p.read_text(encoding='utf-8')\nexcept FileNotFoundError:\n    print('File not found — using default')\n    text = ''\nprint(repr(text))")],
        5: [("**Additional Example**: Append to a log file.", "from pathlib import Path\np = Path('_app.log')\np.write_text('', encoding='utf-8')\nwith p.open('a', encoding='utf-8') as f:\n    f.write('event: started\\n')\n    f.write('event: finished\\n')\nprint(p.read_text(encoding='utf-8'))\np.unlink(missing_ok=True)")],
        6: [("**Additional Example**: Simple CLI argument simulation.", "import sys\n# Simulate: python app.py greet Ada\nargs = ['app.py', 'greet', 'Ada']\ncommand, name = args[1], args[2]\nif command == 'greet':\n    print(f'Hello, {name}!')")],
        7: [("**Additional Example**: Config dict from JSON file.", "import json\nfrom pathlib import Path\np = Path('_cfg.json')\np.write_text(json.dumps({'debug': True, 'port': 8080}), encoding='utf-8')\ncfg = json.loads(p.read_text(encoding='utf-8'))\nprint('debug mode:', cfg['debug'])\np.unlink(missing_ok=True)")],
        8: [("**Additional Example**: Count lines in a file.", "from pathlib import Path\np = Path('_count.txt')\np.write_text('one\\ntwo\\nthree\\n', encoding='utf-8')\ncount = len(p.read_text(encoding='utf-8').splitlines())\nprint('Line count:', count)\np.unlink(missing_ok=True)")],
    },
    # ── Level 2 ──────────────────────────────────────────────────────────
    "python-level-2-course/modules/M01_Modules_and_Standard_Library/M01_Concepts.ipynb": {
        1: [("**Additional Example**: Import a standard module.", "import math\nprint('hypot(3,4):', math.hypot(3, 4))\nprint('ceil(2.3):', math.ceil(2.3))")],
        2: [("**Additional Example**: `from module import name`.", "from datetime import date\ntoday = date.today()\nprint('Today:', today.isoformat())")],
        3: [("**Additional Example**: Module alias with `as`.", "import json as js\ndata = js.dumps({'ok': True})\nprint(data)")],
        4: [("**Additional Example**: `random` from standard library.", "import random\nnums = [10, 20, 30, 40]\nprint('choice:', random.choice(nums))\nprint('sample:', random.sample(nums, 2))")],
        5: [("**Additional Example**: `os.path` / pathlib for paths.", "from pathlib import Path\np = Path('.') / 'README.md'\nprint('exists:', p.exists(), '| name:', p.name)")],
        6: [("**Additional Example**: `sys.argv` and platform.", "import sys\nprint('Python version:', sys.version_info[:3])\nprint('Platform:', sys.platform)")],
        7: [("**Additional Example**: `collections.Counter`.", "from collections import Counter\nwords = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']\nprint(Counter(words))")],
    },
    "python-level-2-course/modules/M02_User_Defined_Modules_and_Packages/M02_Concepts.ipynb": {
        1: [("**Additional Example**: Module is a `.py` file with names.", "# Simulating mymath.py in this cell\nPI = 3.14159\n\ndef area(r):\n    return PI * r * r\n\nprint('area(2):', round(area(2), 2))")],
        2: [("**Additional Example**: Package = folder with `__init__.py`.", "# Package layout: mypkg/__init__.py exposes greet()\nclass _PkgDemo:\n    @staticmethod\n    def greet(name):\n        return f'Hello from package, {name}!'\n\nprint(_PkgDemo.greet('Dev'))")],
        3: [("**Additional Example**: Relative vs absolute import concept.", "# Absolute: from mypkg.utils import helper\n# Relative (inside package): from .utils import helper\nprint('Prefer absolute imports for clarity (PEP 8)')")],
        4: [("**Additional Example**: `__all__` controls `from mod import *`.", "ALL = ['public_fn']\n\ndef public_fn():\n    return 'exported'\n\ndef _private_fn():\n    return 'hidden'\n\nprint(public_fn(), 'defined in __all__:', 'public_fn' in ALL)")],
        5: [("**Additional Example**: Running module as script: `python -m pkg`.", "print('python -m mypkg runs __main__.py or __init__ entry point')")],
        6: [("**Additional Example**: Namespace packages (PEP 420) note.", "print('Folders without __init__.py can be namespace packages on Python 3.3+')")],
    },
    "python-level-2-course/modules/M03_Exceptions/M03_Concepts.ipynb": {
        1: [("**Additional Example**: Hierarchy — catch subclass.", "try:\n    int('x')\nexcept ValueError as e:\n    print('ValueError:', e)")],
        2: [("**Additional Example**: Custom exception class.", "class AppError(Exception):\n    pass\n\nraise AppError('something went wrong in the app layer')")],
        3: [("**Additional Example**: Re-raise after logging.", "def load_config():\n    try:\n        raise FileNotFoundError('config.json')\n    except FileNotFoundError:\n        print('LOG: config missing, using defaults')\n        return {}\n\nprint(load_config())")],
        4: [("**Additional Example**: Exception args tuple.", "try:\n    raise RuntimeError('timeout', 30)\nexcept RuntimeError as e:\n    print('args:', e.args)")],
    },
    "python-level-2-course/modules/M04_Strings/M04_Concepts.ipynb": {
        1: [("**Additional Example**: ord and chr.", "print('ord A:', ord('A'), 'chr 65:', chr(65))")],
        2: [("**Additional Example**: String immutability.", "s = 'hello'\n# s[0] = 'H'  # TypeError\nupper = s.upper()\nprint('original:', s, '| upper copy:', upper)")],
        3: [("**Additional Example**: encode/decode UTF-8.", "text = 'café'\nb = text.encode('utf-8')\nprint('bytes:', b)\nprint('decoded:', b.decode('utf-8'))")],
        4: [("**Additional Example**: str.format with placeholders.", "template = 'User: {0}, Role: {1}'\nprint(template.format('Ada', 'admin'))")],
        5: [("**Additional Example**: isalpha / isdigit checks.", "tokens = ['abc', '123', 'a1']\nfor t in tokens:\n    print(t, 'alpha:', t.isalpha(), 'digit:', t.isdigit())")],
    },
    "python-level-2-course/modules/M05_OOP_Foundations/M05_Concepts.ipynb": {
        1: [("**Additional Example**: Multiple instances, independent state.", "class Counter:\n    def __init__(self):\n        self.value = 0\n    def inc(self):\n        self.value += 1\n        return self.value\n\nc1, c2 = Counter(), Counter()\nc1.inc()\nc1.inc()\nc2.inc()\nprint(c1.value, c2.value)")],
        2: [("**Additional Example**: Class variable default vs instance override.", "class Settings:\n    theme = 'light'\n\na, b = Settings(), Settings()\nb.theme = 'dark'\nprint('a.theme:', a.theme, '| b.theme:', b.theme, '| class:', Settings.theme)")],
        3: [("**Additional Example**: Method chaining via return self.", "class Builder:\n    def __init__(self):\n        self.parts = []\n    def add(self, part):\n        self.parts.append(part)\n        return self\n\nb = Builder().add('A').add('B')\nprint(b.parts)")],
        4: [("**Additional Example**: vars() introspection.", "class Item:\n    def __init__(self, sku, qty):\n        self.sku = sku\n        self.qty = qty\n\nit = Item('X1', 5)\nprint(vars(it))")],
        5: [("**Additional Example**: Validate in __init__.", "class EmailUser:\n    def __init__(self, email):\n        if '@' not in email:\n            raise ValueError('invalid email')\n        self.email = email\n\nu = EmailUser('ada@example.com')\nprint(u.email)")],
        6: [("**Additional Example**: delattr and hasattr.", "class Box:\n    def __init__(self):\n        self.temp = True\n\nb = Box()\nprint('before:', hasattr(b, 'temp'))\ndelattr(b, 'temp')\nprint('after:', hasattr(b, 'temp'))")],
    },
    "python-level-2-course/modules/M06_Inheritance_and_Polymorphism/M06_Concepts.ipynb": {
        1: [("**Additional Example**: Extend superclass method.", "class Animal:\n    def speak(self):\n        return '...'\n\nclass Cat(Animal):\n    def speak(self):\n        return super().speak() + ' meow'\n\nprint(Cat().speak())")],
        2: [("**Additional Example**: Polymorphic list.", "class Dog(Animal):\n    def speak(self):\n        return 'woof'\n\nfor pet in [Dog(), Cat()]:\n    print(type(pet).__name__, 'says', pet.speak())")],
        3: [("**Additional Example**: super() in multi-level chain.", "class Vehicle:\n    def start(self):\n        return 'engine on'\n\nclass Car(Vehicle):\n    def start(self):\n        return super().start() + ', seatbelt check'\n\nprint(Car().start())")],
        4: [("**Additional Example**: Diamond MRO inspection.", "class Base:\n    def ping(self):\n        return 'Base'\nclass Left(Base):\n    def ping(self):\n        return 'Left'\nclass Right(Base):\n    def ping(self):\n        return 'Right'\nclass Bottom(Left, Right):\n    pass\n\nprint(Bottom().ping())\nprint([c.__name__ for c in Bottom.__mro__])")],
    },
    "python-level-2-course/modules/M07_Comprehensions_Lambdas_Closures/M07_Concepts.ipynb": {
        1: [("**Additional Example**: Filtered comprehension.", "words = ['apple', 'kiwi', 'banana', 'fig']\nlong_words = [w for w in words if len(w) >= 5]\nprint(long_words)")],
        2: [("**Additional Example**: sorted with key=lambda.", "people = [('Ada', 30), ('Bob', 25), ('Cy', 35)]\nby_age = sorted(people, key=lambda p: p[1])\nprint(by_age)")],
        3: [("**Additional Example**: Closure factory for validators.", "def min_length(n):\n    def check(text):\n        return len(text) >= n\n    return check\n\nvalidate = min_length(3)\nprint(validate('hi'), validate('hey'))")],
    },
    "python-level-2-course/modules/M08_File_IO/M08_Concepts.ipynb": {
        1: [("**Additional Example**: Read/write with Path (alternative to open).", "from pathlib import Path\np = Path('_nb_demo.txt')\np.write_text('hello file\\n', encoding='utf-8')\nprint(p.read_text(encoding='utf-8'))\np.unlink(missing_ok=True)")],
        2: [("**Additional Example**: Process file line-by-line without read().", "from pathlib import Path\np = Path('_lineproc.txt')\np.write_text('a\\nb\\nc\\n', encoding='utf-8')\nwith p.open(encoding='utf-8') as f:\n    for line in f:\n        print('got:', line.strip())\np.unlink(missing_ok=True)")],
    },
    # ── Level 3 ──────────────────────────────────────────────────────────
    "python-level-3-course/modules/M01_Advanced_OOP_Foundations/M01_Concepts.ipynb": {
        1: [("**Additional Example**: issubclass with built-in types.", "class Employee: pass\nprint(issubclass(Employee, object))\nprint(isinstance(Employee(), Employee))")],
        2: [("**Additional Example**: Mutating class variable affects all instances.", "class Tag:\n    prefix = 'ID-'\n\na, b = Tag(), Tag()\nTag.prefix = 'REF-'\nprint(a.prefix, b.prefix)")],
        3: [("**Additional Example**: super() in multiple inheritance.", "class A:\n    def __init__(self):\n        print('A init')\nclass B(A):\n    def __init__(self):\n        super().__init__()\n        print('B init')\n\nB()")],
        4: [("**Additional Example**: Duck typing — no inheritance required.", "class Robot:\n    def speak(self):\n        return 'beep'\n\ndef announce(entity):\n    print(entity.speak())\n\nannounce(Robot())")],
    },
    "python-level-3-course/modules/M02_Magic_Methods/M02_Concepts.ipynb": {
        1: [("**Additional Example**: Sort Points with @total_ordering.", "from functools import total_ordering\n\n@total_ordering\nclass Score:\n    def __init__(self, value):\n        self.value = value\n    def __eq__(self, other):\n        return self.value == other.value\n    def __lt__(self, other):\n        return self.value < other.value\n\nprint(sorted([Score(30), Score(10), Score(20)], key=lambda s: s.value))")],
        2: [("**Additional Example**: __sub__ for vector subtraction.", "class V:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __sub__(self, other):\n        return V(self.x - other.x, self.y - other.y)\n    def __str__(self):\n        return f'V({self.x},{self.y})'\n\nprint(V(5, 7) - V(1, 2))")],
        3: [("**Additional Example**: __repr__ for debugging.", "class SKU:\n    def __init__(self, code):\n        self.code = code\n    def __repr__(self):\n        return f\"SKU({self.code!r})\"\n\nprint([SKU('A1'), SKU('B2')])")],
        4: [("**Additional Example**: __setattr__ validation.", "class Positive:\n    def __setattr__(self, name, value):\n        if name == 'x' and value < 0:\n            raise ValueError('x must be >= 0')\n        super().__setattr__(name, value)\n\np = Positive()\np.x = 10\nprint(p.x)")],
        5: [("**Additional Example**: __contains__ for membership.", "class Bag:\n    def __init__(self, items):\n        self._items = list(items)\n    def __contains__(self, item):\n        return item in self._items\n\nb = Bag(['pen', 'pad'])\nprint('pen' in b, 'phone' in b)")],
        6: [("**Additional Example**: __str__ vs __repr__ side by side.", "class Product:\n    def __init__(self, name, price):\n        self.name, self.price = name, price\n    def __str__(self):\n        return f'{self.name} (${self.price})'\n    def __repr__(self):\n        return f\"Product({self.name!r}, {self.price})\"\n\np = Product('Widget', 9.99)\nprint(str(p), '|', repr(p))")],
    },
    "python-level-3-course/modules/M03_Decorators/M03_Concepts.ipynb": {
        1: [("**Additional Example**: Combining *args and **kwargs.", "def log_call(*args, **kwargs):\n    print('args:', args)\n    print('kwargs:', kwargs)\n\nlog_call(1, 2, mode='fast', debug=True)")],
        2: [("**Additional Example**: Closure counter.", "def make_counter():\n    count = 0\n    def inc():\n        nonlocal count\n        count += 1\n        return count\n    return inc\n\nc = make_counter()\nprint(c(), c(), c())")],
        3: [("**Additional Example**: Simple @decorator without functools.", "def bold(fn):\n    def wrapper(*a, **k):\n        return f'**{fn(*a, **k)}**'\n    return wrapper\n\n@bold\ndef title():\n    return 'Report'\n\nprint(title())")],
        4: [("**Additional Example**: Parameterized @repeat(n).", "import functools\n\ndef repeat(times):\n    def deco(fn):\n        @functools.wraps(fn)\n        def wrapper(*a, **k):\n            for _ in range(times):\n                fn(*a, **k)\n        return wrapper\n    return deco\n\n@repeat(2)\ndef ping():\n    print('ping')\n\nping()")],
        5: [("**Additional Example**: Class decorator with state.", "class CountCalls:\n    def __init__(self, fn):\n        self.fn = fn\n        self.calls = 0\n    def __call__(self, *a, **k):\n        self.calls += 1\n        return self.fn(*a, **k)\n\n@CountCalls\ndef work():\n    return 'done'\n\nwork()\nwork()\nprint('calls:', work.calls)")],
        6: [("**Additional Example**: Stacking order demo.", "def tag(name):\n    def deco(fn):\n        def wrapper(*a, **k):\n            print(f'[{name}] enter')\n            return fn(*a, **k)\n        return wrapper\n    return deco\n\n@tag('outer')\n@tag('inner')\ndef task():\n    print('running')\n\ntask()")],
    },
    "python-level-3-course/modules/M04_Static_Class_Methods/M04_Concepts.ipynb": {
        1: [("**Additional Example**: Static method as validator.", "class UserForm:\n    @staticmethod\n    def is_valid_email(email: str) -> bool:\n        return '@' in email and '.' in email.split('@')[-1]\n\nprint(UserForm.is_valid_email('a@b.com'), UserForm.is_valid_email('bad'))")],
        2: [("**Additional Example**: Class method alternate constructor.", "class Temperature:\n    def __init__(self, celsius: float):\n        self.celsius = celsius\n    @classmethod\n    def from_fahrenheit(cls, f: float):\n        return cls((f - 32) * 5 / 9)\n\nprint(Temperature.from_fahrenheit(32).celsius)")],
        3: [("**Additional Example**: Cannot instantiate ABC.", "import abc\nclass Port(abc.ABC):\n    @abc.abstractmethod\n    def send(self, data: bytes) -> None: ...\n\nclass MemoryPort(Port):\n    def send(self, data: bytes) -> None:\n        print('sent', len(data), 'bytes')\n\nMemoryPort().send(b'hi')")],
        4: [("**Additional Example**: Multiple ABC mixins.", "import abc\nclass Serializable(abc.ABC):\n    @abc.abstractmethod\n    def to_dict(self) -> dict: ...\n\nclass User(Serializable):\n    def __init__(self, name):\n        self.name = name\n    def to_dict(self):\n        return {'name': self.name}\n\nprint(User('Ada').to_dict())")],
    },
    "python-level-3-course/modules/M05_Encapsulation/M05_Concepts.ipynb": {
        1: [("**Additional Example**: Property deleter.", "class Account:\n    def __init__(self, owner):\n        self.owner = owner\n        self._notes = None\n    @property\n    def notes(self):\n        return self._notes\n    @notes.setter\n    def notes(self, value):\n        self._notes = value.strip() if value else None\n    @notes.deleter\n    def notes(self):\n        self._notes = None\n\na = Account('Ada')\na.notes = '  hello  '\nprint(repr(a.notes))\ndel a.notes\nprint(a.notes)")],
        2: [("**Additional Example**: Subclass list with custom insert.", "class Stack(list):\n    def push(self, item):\n        self.append(item)\n    def pop_item(self):\n        return super().pop()\n\ns = Stack()\ns.push(1)\ns.push(2)\nprint(s.pop_item(), s)")],
    },
    "python-level-3-course/modules/M06_Advanced_Exceptions/M06_Concepts.ipynb": {
        1: [("**Additional Example**: Implicit vs explicit chaining.", "def low():\n    raise ValueError('low level')\n\ndef high():\n    try:\n        low()\n    except ValueError as e:\n        raise RuntimeError('high level') from e\n\ntry:\n    high()\nexcept RuntimeError as e:\n    print('cause type:', type(e.__cause__).__name__)")],
        2: [("**Additional Example**: traceback.format_exc in except block.", "import traceback\n\ndef risky():\n    return 1 / 0\n\ntry:\n    risky()\nexcept ZeroDivisionError:\n    print(traceback.format_exc().splitlines()[-1])")],
        3: [("**Additional Example**: deepcopy nested dict.", "import copy\noriginal = {'a': [1, 2], 'b': {'x': 1}}\nshallow = copy.copy(original)\ndeep = copy.deepcopy(original)\nshallow['a'].append(99)\ndeep['b']['x'] = 42\nprint('original:', original)\nprint('deep b:', deep['b'])")],
    },
    "python-level-3-course/modules/M07_Serialization/M07_Concepts.ipynb": {
        1: [("**Additional Example**: Pickle list of objects.", "import pickle\nitems = [{'id': 1}, {'id': 2}]\nraw = pickle.dumps(items)\nprint('restored:', pickle.loads(raw))")],
        2: [("**Additional Example**: Shelve update existing key.", "import shelve\nfrom pathlib import Path\npath = 'demo_shelf.db'\nwith shelve.open(path, flag='c') as db:\n    db['counter'] = db.get('counter', 0) + 1\n    print('counter:', db['counter'])\nfor ext in ('.db', '.bak', '.dat', '.dir'):\n    p = Path(path + ext)\n    if p.exists():\n        p.unlink()")],
        3: [("**Additional Example**: Metaclass auto __repr__.", "class AutoReprMeta(type):\n    def __new__(mcs, name, bases, ns):\n        cls = super().__new__(mcs, name, bases, ns)\n        if name != 'Base':\n            def __repr__(self):\n                fields = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())\n                return f'{name}({fields})'\n            cls.__repr__ = __repr__\n        return cls\n\nclass Base(metaclass=AutoReprMeta):\n    pass\n\nclass Point(Base):\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n\nprint(Point(1, 2))")],
        4: [("**Additional Example**: type() with methods.", "def greet(self):\n    return f'Hi, {self.name}'\n\nPerson = type('Person', (), {'name': 'Guest', 'greet': greet})\nprint(Person().greet())")],
        5: [("**Additional Example**: __qualname__ for nested classes.", "class Outer:\n    class Inner:\n        pass\n\nprint(Outer.Inner.__qualname__)")],
    },
    "python-level-3-course/modules/M08_PEP_Standards/M08_Concepts.ipynb": {
        1: [("**Additional Example**: PEP 8 line length and naming.", "def calculate_total(items):\n    return sum(items)\n\nprint(calculate_total([1, 2, 3]))")],
        2: [("**Additional Example**: PEP 257 one-line docstring.", "def add(a, b):\n    \"\"\"Return sum of a and b.\"\"\"\n    return a + b\n\nprint(add.__doc__)")],
        3: [("**Additional Example**: PEP 484 type hints.", "def discount(price: float, rate: float = 0.1) -> float:\n    return price * (1 - rate)\n\nprint(discount(100.0))")],
        4: [("**Additional Example**: `if __name__ == '__main__'` guard.", "def main():\n    print('PEP 8: keep imports at top, use 4 spaces')\n\nif __name__ == '__main__':\n    main()")],
    },
    "python-level-3-course/modules/M09_GUI_Programming/M09_Concepts.ipynb": {
        1: [("**Additional Example**: Frame widget grouping.", "import tkinter as tk\nroot = tk.Tk()\nframe = tk.Frame(root, padx=10, pady=10)\nframe.pack()\ntk.Label(frame, text='Inside frame').pack()\n# root.mainloop()")],
        2: [("**Additional Example**: grid column weights.", "import tkinter as tk\nroot = tk.Tk()\nroot.columnconfigure(0, weight=1)\ntk.Label(root, text='Left').grid(row=0, column=0, sticky='w')\ntk.Label(root, text='Right').grid(row=0, column=1, sticky='e')\n# root.mainloop()")],
        3: [("**Additional Example**: bind mouse click event.", "import tkinter as tk\n\ndef on_click(event):\n    print(f'clicked at {event.x}, {event.y}')\n\nroot = tk.Tk()\nlbl = tk.Label(root, text='Click me', width=20, height=2)\nlbl.pack()\nlbl.bind('<Button-1>', on_click)\n# root.mainloop()")],
        4: [("**Additional Example**: IntVar with Checkbutton.", "import tkinter as tk\nroot = tk.Tk()\naccepted = tk.BooleanVar(value=False)\ntk.Checkbutton(root, text='Accept terms', variable=accepted).pack()\nprint('initial:', accepted.get())\n# root.mainloop()")],
    },
    "python-level-3-course/modules/M10_Network_Programming/M10_Concepts.ipynb": {
        1: [("**Additional Example**: JSON pretty print.", "import json\ndata = {'users': [{'name': 'Ada'}, {'name': 'Bob'}]}\nprint(json.dumps(data, indent=2))")],
        2: [("**Additional Example**: Build XML with attributes.", "import xml.etree.ElementTree as ET\nroot = ET.Element('catalog')\nitem = ET.SubElement(root, 'item', id='1')\nET.SubElement(item, 'name').text = 'Widget'\nprint(ET.tostring(root, encoding='unicode'))")],
        3: [("**Additional Example**: Handle HTTP errors.", "import requests\nfrom requests.exceptions import HTTPError\n\ntry:\n    r = requests.get('https://httpbin.org/status/404')\n    r.raise_for_status()\nexcept HTTPError as e:\n    print('HTTP error:', e.response.status_code)")],
    },
    "python-level-3-course/modules/M11_Database_File_Processing/M11_Concepts.ipynb": {
        1: [("**Additional Example**: SQLite CREATE and INSERT.", "import sqlite3\nconn = sqlite3.connect(':memory:')\nconn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')\nconn.execute('INSERT INTO users (name) VALUES (?)', ('Ada',))\nrow = conn.execute('SELECT name FROM users').fetchone()\nprint(row)\nconn.close()")],
        2: [("**Additional Example**: Parameterized query prevents SQL injection.", "import sqlite3\nconn = sqlite3.connect(':memory:')\nconn.execute('CREATE TABLE items (name TEXT)')\nconn.execute('INSERT INTO items VALUES (?)', ('safe',))\nuser_input = \"'; DROP TABLE items; --\"\nrows = conn.execute('SELECT name FROM items WHERE name = ?', (user_input,)).fetchall()\nprint('rows:', rows)\nconn.close()")],
        3: [("**Additional Example**: CSV read with csv module.", "import csv\nfrom io import StringIO\ntext = 'name,score\\nAda,90\\nBob,85\\n'\nreader = csv.DictReader(StringIO(text))\nprint(list(reader))")],
        4: [("**Additional Example**: Context manager for DB connection.", "import sqlite3\nfrom contextlib import closing\n\nwith closing(sqlite3.connect(':memory:')) as conn:\n    conn.execute('SELECT 1')\n    print('connection active inside with block')")],
    },
    "python-level-3-course/modules/M12_Integration/M12_Concepts.ipynb": {
        "Architecture Pattern": [
            ("**Additional Example**: Controller coordinates model and view.", "class Model:\n    def fetch(self):\n        return ['task-1', 'task-2']\n\nclass Controller:\n    def __init__(self, model, view):\n        self.model, self.view = model, view\n    def refresh(self):\n        self.view.display(self.model.fetch())\n\nclass View:\n    def display(self, items):\n        print('UI shows:', items)\n\nController(Model(), View()).refresh()")
        ],
        "Integration Checklist": [
            ("**Additional Example**: Layered config loading pattern.", "import json\n\nDEFAULTS = {'debug': False, 'port': 8080}\n\ndef load_config(overrides=None):\n    cfg = DEFAULTS.copy()\n    if overrides:\n        cfg.update(overrides)\n    return cfg\n\nprint(load_config({'debug': True}))")
        ],
    },
}


def make_md(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.split("\n")[:-1]] + ([text.split("\n")[-1] + "\n"] if text else []),
    }


def make_code(text: str) -> dict:
    lines = text.split("\n")
    source = [line + "\n" for line in lines[:-1]]
    if lines:
        source.append(lines[-1] + ("\n" if not lines[-1].endswith("\n") else ""))
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source,
    }


def cell_text(cell: dict) -> str:
    return "".join(cell.get("source", []))


def already_enriched(cells: list[dict]) -> bool:
    return any(MARKER in cell_text(c) for c in cells)


def find_sections(cells: list[dict]) -> list[dict]:
    sections = []
    skip_headers = {"Learning Outcomes", "Table of Contents", "Practice Exercises", "Practice"}
    for i, cell in enumerate(cells):
        if cell["cell_type"] != "markdown":
            continue
        src = cell_text(cell)
        if any(h in src for h in ("## Learning Outcomes", "## Table of Contents")):
            continue
        m = re.search(r"^##\s+(?:(\d+)\.\s+(.+)|(.+))", src, re.MULTILINE)
        if not m:
            continue
        if m.group(1):
            num = int(m.group(1))
            title = m.group(2).strip()
        else:
            num = m.group(3).strip()
            title = num
        if any(title.startswith(s) for s in skip_headers):
            continue
        if title.startswith("Practice"):
            continue
        sections.append({"idx": i, "num": num, "title": title})
    return sections


def section_key(section: dict) -> int | str:
    title = section["title"]
    if isinstance(section["num"], int):
        return section["num"]
    if "MVC" in title or "Architecture" in title:
        return "Architecture Pattern"
    if "Integration Checklist" in title or "Checklist" in title:
        return "Integration Checklist"
    return title


def enrich_notebook(path: Path, examples: dict) -> int:
    with path.open(encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb["cells"]
    if already_enriched(cells):
        print(f"  skip (already enriched): {path.name}")
        return 0

    sections = find_sections(cells)
    inserted = 0

    for sec_i in range(len(sections) - 1, -1, -1):
        sec = sections[sec_i]
        end_idx = sections[sec_i + 1]["idx"] if sec_i + 1 < len(sections) else len(cells)

        # Stop before practice-only tail
        while end_idx > sec["idx"] + 1:
            prev = cell_text(cells[end_idx - 1])
            if re.search(r"^##\s+.*Practice", prev, re.MULTILINE):
                end_idx -= 1
                break
            break

        key = section_key(sec)
        pairs = examples.get(key) or examples.get(sec["num"])
        if not pairs:
            continue

        new_cells = []
        for md, code in pairs:
            new_cells.append(make_md(md))
            new_cells.append(make_code(code))

        cells[end_idx:end_idx] = new_cells
        inserted += len(new_cells)

    nb["cells"] = cells
    with path.open("w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)
        f.write("\n")

    return inserted


def main() -> None:
    total = 0
    for rel, examples in ENRICHMENTS.items():
        path = ROOT / rel.replace("/", "\\") if "\\" in str(ROOT) else ROOT / rel
        path = ROOT / Path(rel)
        if not path.exists():
            print(f"MISSING: {rel}")
            continue
        n = enrich_notebook(path, examples)
        print(f"  +{n} cells: {rel}")
        total += n
    print(f"Done. Inserted {total} new cells across {len(ENRICHMENTS)} notebooks.")


if __name__ == "__main__":
    main()
