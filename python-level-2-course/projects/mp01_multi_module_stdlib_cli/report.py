"""Report helpers using math, random, platform (PCAP 1.2-1.4)."""
import math
import random
import platform


def get_platform_info():
    return {
        "system": platform.system(),
        "version_tuple": platform.python_version_tuple(),
    }


def get_math_sample(value=10.7):
    return {
        "sqrt": math.sqrt(value),
        "ceil": math.ceil(value),
        "floor": math.floor(value),
    }


def get_random_sample(seed=None):
    if seed is not None:
        random.seed(seed)
    return {
        "random": random.random(),
        "choice": random.choice(["heads", "tails"]),
    }


def build_report(seed=None):
    info = get_platform_info()
    math_vals = get_math_sample()
    rnd = get_random_sample(seed=seed)
    return {"platform": info, "math": math_vals, "random": rnd}
