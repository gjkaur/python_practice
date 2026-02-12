# MP01 – Multi-Module CLI Using Standard Library

**PCAP**: 1.1–1.4 (modules, math, random, platform)

## Problem

Build a small CLI that uses the **math**, **random**, and **platform** modules. It should demonstrate import variants, `dir()`/discovery, and produce useful output (e.g. random tip, rounded value, OS info).

## User Stories

- As a user I get a one-shot report: OS, Python version tuple, a random number, and a math result (e.g. sqrt, ceil).
- As a learner I see clear separation: one module for “report” logic, main script for CLI.

## Suggested Structure

- `main.py` – entrypoint; imports from `report` and prints.
- `report.py` – functions that use math, random, platform; no raw input.

## Test Cases

1. Run `python main.py` → no crash; output includes platform and at least one math and one random result.
2. Run with fixed seed (if you add --seed) → reproducible random output.
3. Import report from REPL → dir(report) shows expected names.
