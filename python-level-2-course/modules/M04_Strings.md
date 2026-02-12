## M04 – Strings

**PCAP Alignment**: Section 3 (3.1–3.3) – Machine representation, operations, built-in methods.  
**Professional Focus**: Encoding-aware text handling, string methods in production.

---

### 1. Outcomes

By the end of this module you will:

- Understand **encoding standards**: ASCII, Unicode, UTF-8, code points, escape sequences.
- Use **ord()** and **chr()** for code point conversion.
- Apply **indexing**, **slicing**, and **immutability**.
- **Iterate** through strings; **concatenate**, **multiply**, **compare** (strings and with numbers where applicable).
- Use operators **in**, **not in**.
- Use built-in string methods: **.isxxx()**, **.join()**, **.split()**, **.sort()**/ **sorted()**, **.index()**, **.find()**, **.rfind()**.

---

### 2. Core Concepts (PCAP 3.1–3.3)

#### 2.1 Machine representation (PCAP 3.1)

- **ASCII**: 7-bit; covers basic Latin and control characters.
- **Unicode**: code points (e.g. U+0041 for 'A'); covers all scripts.
- **UTF-8**: variable-length encoding of Unicode; backward compatible with ASCII for code points < 128.
- **Escape sequences**: `\n` newline, `\t` tab, `\uXXXX` 16-bit hex, `\UXXXXXXXX` 32-bit, `\N{name}` by name.

Example:

```python
print(ord("A"), chr(65))
print(ord("é"), chr(233))
print("Hello\nWorld")
```

#### 2.2 Operate on strings (PCAP 3.2)

- `ord("A")`, `chr(65)`; indexing `s[0]`, slicing `s[1:4]`; immutability (no in-place change).
- Iteration: `for c in s`; concatenation `+`; repetition `*`; comparison `==`, `<`, `>`; `in`, `not in`.
- Comparing strings to numbers: type-dependent (e.g. `"3" > 2` in Python 3 raises TypeError in strict comparison).

#### 2.3 Built-in string methods (PCAP 3.3)

- `.isalpha()`, `.isdigit()`, `.isalnum()`, etc. (`.isxxx()` family).
- `.join(iterable)`, `.split(sep=None, maxsplit=-1)`.
- `.sort()` is list method; `sorted(s)` returns sorted list of characters.
- `.index(sub)` raises if not found; `.find(sub)` returns -1; `.rfind(sub)` from right.

---

### 2.4 Edge Cases and Pitfalls

- **Empty string**: Most methods behave sensibly; `"".find("x")` → -1. `ord("")` raises TypeError.
- **Encoding**: When reading/writing files, always pass `encoding="utf-8"` (or the correct encoding) to avoid platform-dependent defaults.
- **str vs bytes**: `ord`/`chr` work on characters (str of length 1). For bytes, use index directly (e.g. b[0]).
- **.index()** raises ValueError when substring not found; use .find() if you need -1 instead.

---

### 2.5 Built-in and Related Functions

- **ord(c)**: Code point of a single character (str length 1).
- **chr(i)**: Character for code point i (0 ≤ i ≤ 0x10FFFF).
- **str(x)**: String representation of any object.
- **repr(x)**: Developer-friendly representation (often with quotes).
- **len(s)**: Length of string (number of characters).
- **sorted(s)**: Returns a list of characters in sorted order.

---

### 2.6 Production Notes

- For building long strings from many parts, use a list of fragments and **''.join(list)** instead of repeated `+=` (which creates many intermediate strings).
- Use **.find()** when you want -1 for "not found"; use **.index()** only when you want an exception.
- Specify **encoding** explicitly in open() for text files to avoid surprises across platforms.

---

### 3. Practice Set (10–15 Exercises)

1. Print **ord** and **chr** for "A", "0", and one non-ASCII character (e.g. "é" in UTF-8). Verify chr(ord(c)) == c.
2. Slice a string to get the first three and last three characters. Use any string of length at least 6.
3. Use **in** and **not in** to check if a substring exists in a sentence; print boolean results.
4. Concatenate two strings with **+** and multiply a string by 3; print both results.
5. Use **.split()** and **.join()** to reverse the word order in "a b c" so the result is "c b a".
6. Use **.isdigit()** and **.isalpha()** on the strings "123", "abc", and "12ab"; print the results for each.
7. Use **.find()** for a substring that exists and one that does not; then use **.index()** and catch **ValueError** when the substring is not found.
8. Use **.rfind()** to find the last occurrence of a character in "hello world"; print the index.
9. Iterate over a string and build a list of code points using **ord()**; try with "Hi".
10. Encode a string to bytes with **s.encode("utf-8")** and decode back with **.decode("utf-8")**; print and explain.
11. Use **sorted(s)** on a short string and explain what the result is (list of what?).
12. Build a long string from a list of 10 fragments using **"".join(list)** instead of repeated **+=**; time or reason about performance.

---

### 4. Mini-Project – Text Normalizer / Simple Parser

#### 4.1 Problem Statement

Build a small CLI or script that reads text input (from user or a file), normalizes it (e.g. strip, lower, replace), and uses **split**, **join**, **find** or **index** to produce a structured output. Handle encoding explicitly (e.g. **encoding="utf-8"**) when reading or writing files.

#### 4.2 Requirements

- Read a line or file; normalize with **.strip()**, **.lower()**, and optionally **.replace()**.
- Use **.split()** and **" ".join()** (or another separator) to reorganize or filter words.
- Use **.find()** or **.index()** (with try/except for index) for at least one lookup.
- When opening files, pass **encoding="utf-8"** (or document the encoding used).
- Implement a **main()** entrypoint and clear function names; follow PEP 8.

#### 4.3 Suggested Folder Structure

```text
mp04_text_normalizer/
  main.py       # entrypoint: read input, call normalizer, print result
  normalizer.py # e.g. normalize_line(s), extract_words(s)
  README.md     # short project description and usage
```

#### 4.4 Acceptance Tests (High-Level)

- Running the script on a sample line produces normalized output (e.g. lowercase, trimmed, words reordered or filtered).
- Code uses **.find()** or **.index()** with appropriate error handling.
- Any file I/O uses an explicit **encoding** argument.
- Code passes a quick review for "no repeated += in a loop for building a long string" (prefer **join**).

---

### 5. Code Review Checklist (Module-Specific)

- **Encoding**: [ ] Encoding specified when reading/writing text (e.g. **encoding="utf-8"**).
- **String methods**: [ ] Correct use of **.find()** vs **.index()** (and error handling for **.index()**). [ ] No unnecessary string concatenation in loops (prefer list + **"".join()**).
- **Correctness**: [ ] **ord()** not called on empty string.

---

### 6. Interview-Style Questions (8–12)

1. What is the difference between **ASCII**, **Unicode**, and **UTF-8**?
2. What does **ord()** return? **chr()**? What happens if you call **ord("")**?
3. Why are strings immutable? What happens if you “change” one?
4. What is the difference between **.find()** and **.index()**? When would you use each?
5. How do you combine a list of strings into one? On which object do you call **join**?
6. What does **.split()** return? How do you limit the number of splits?
7. Name three **.isxxx()** methods and their purpose.
8. What does **.rfind()** do? How does it differ from **.find()**?
9. How do you reverse word order in "a b c" using **split** and **join**?
10. Why is **"".join(parts)** preferred over repeated **+=** when building a long string in a loop?
