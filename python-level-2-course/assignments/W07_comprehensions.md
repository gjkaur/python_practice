# Week 7 – Comprehensions, Lambdas, Closures (PCAP 5.1–5.3)

**Module**: M07  
**Mini Project**: [mp07 Data Pipeline](../projects/mp07_data_pipeline_comprehensions/)

## Learning focus

- List comprehensions with if and nested; lambdas; map(), filter(); closures (define and use).

## Reading

- [M07 – Comprehensions, Lambdas, Closures](../modules/M07_Comprehensions_Lambdas_Closures.md)
- M07_Concepts.ipynb.

## Practice

1. Write [x*2 for x in range(10) if x % 2 == 0].
2. Use map(lambda x: x+1, list) and filter(lambda x: x>0, list).
3. Define make_adder(n) returning lambda x: x+n; call make_adder(2)(3).

## Mini project

1. Read mp07 README. Implement pipeline using comprehensions, map/filter, and one closure.
2. Run with sample data; verify output.

## Checklist

- [ ] List comprehension with if used
- [ ] map or filter used with lambda
- [ ] At least one closure (factory function)
- [ ] Pipeline produces correct result
