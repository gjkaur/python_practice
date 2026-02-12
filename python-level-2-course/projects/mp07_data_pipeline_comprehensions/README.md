# MP07 – Data Pipeline with Comprehensions and Lambdas

**PCAP**: 5.1–5.3 (list comprehensions, lambdas, map/filter, closures)

## Problem

Build a small **data pipeline** or transformer: take a list of data, use **list comprehensions** (with if, optionally nested), **map()**/ **filter()**, and a **closure** (e.g. configurable multiplier or filter threshold).

## User Stories

- As a user I get transformed/filtered output from a list of numbers or records.
- As a learner I use comprehensions, lambdas, and one closure.

## Suggested Structure

- `pipeline.py` – filter_positive, transform_square, make_multiplier(n) closure, pipeline(steps).
- `main.py` – build sample list, run pipeline, print.

## Test Cases

1. [x for x in data if x > 0] and list(map(lambda x: x*2, data)).
2. make_multiplier(3)(4) == 12.
3. Pipeline of filter then map produces expected list.
