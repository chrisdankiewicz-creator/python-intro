def add(a, b):
    return a + b


def clamp(x, low, high):

    if low > high:
        raise ValueError("low cannot be greater than high")
    if x < low:
        return low
    if x > high:
        return high
    return x


def mean(values):
    values = list(values)
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
