"""Data pipeline using comprehensions, lambdas, closure (PCAP 5.1-5.3)."""

def filter_positive(data):
    return [x for x in data if x > 0]

def transform_square(data):
    return list(map(lambda x: x * x, data))

def make_multiplier(n):
    def mul(x):
        return x * n
    return mul

def run_pipeline(data):
    step1 = filter_positive(data)
    step2 = transform_square(step1)
    return step2
