def chunk(items, size):

    if size <= 0:
        raise ValueError("size must be > 0")

    result = []
    for i in range(0, len(items), size):
        result.append(items[i : i + size])
    return result


def safe_get(d, key, default=None):

    if not isinstance(d, dict):
        raise TypeError("d must be a dict")
    return d.get(key, default)
