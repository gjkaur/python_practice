"""Demo: pipeline with comprehensions and lambdas."""
from pipeline import filter_positive, transform_square, make_multiplier, run_pipeline

def main():
    data = [-1, 2, -3, 4, 5]
    print("filter_positive:", filter_positive(data))
    print("transform_square:", transform_square([2, 3, 4]))
    print("make_multiplier(3)(4) =", make_multiplier(3)(4))
    print("run_pipeline:", run_pipeline(data))

if __name__ == "__main__":
    main()
