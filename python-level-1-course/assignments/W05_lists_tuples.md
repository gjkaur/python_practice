# Week 5 – Lists and Tuples

**Module**: M04 (lists, tuples)  
**Mini Project**: [mp05 Student Score Manager v1](../projects/mp05_student_score_manager_v1/)

---

## Learning focus

- Building lists; indexing, slicing, negative indices; list methods.
- Shallow vs deep copy; cloning patterns.
- Tuples: creation, immutability, use as fixed-shape records or keys.

---

## Reading and notebooks

- [M04 – Collections](../modules/M04_Collections_Lists_Tuples_Dictionaries.md) (lists and tuples)
- [M04 Concepts notebook](../modules/M04_Collections_Lists_Tuples_Dictionaries/M04_Concepts.ipynb)
- Run M04 `examples/` and `practice/practice_04_*.py`.

---

## Concepts & practice

1. Build a list of 5 numbers; compute sum and average; print the list reversed (new list, don’t mutate in place if you want to keep original).
2. Given a list of names, print the first, last, and middle (if any); handle empty/single-element lists.
3. Create a tuple of (name, score) for 3 students; loop and print each; explain why tuple might be preferred over list for one record.
4. From the module: complete at least 5 list/tuple exercises from the M04 practice set.

---

## Mini project tasks

1. Read [mp05 README](../projects/mp05_student_score_manager_v1/README.md).
2. Implement Student Score Manager v1: add scores, compute statistics (min, max, mean, count), list scores.
3. Use lists (and optionally tuples for one score record); validate numeric input.
4. Run README test cases; document one edge case (e.g. no scores yet).

---

## Optional

- Add "remove last score" or "clear all."
- Use a tuple for (student_id, score) and a list of such tuples.

---

## Checklist

- [ ] Scores stored and retrieved correctly
- [ ] Statistics correct for 0, 1, and N scores
- [ ] Input validation
- [ ] Clear structure (e.g. separate functions for add/stats/list)
