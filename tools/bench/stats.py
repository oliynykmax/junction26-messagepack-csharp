def mean(values: list[int]) -> float:
    return sum(values) / len(values)

def report(values: list[int]) -> str:
    return "mean: " + mean(values)
