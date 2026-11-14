"""Summary statistics for benchmark runs."""

def mean(values: list[int]) -> float:
    if not values:
        raise ValueError("mean() of an empty list")
    return sum(values) / len(values)

def report(values: list[int]) -> str:
    return f"mean: {mean(values)}"
