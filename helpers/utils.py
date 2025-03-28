def find_closest_name_by_length(names: list) -> str or None:
    if not names:
        return None

    lengths = [len(name) for name in names]
    avg_length = sum(lengths) / len(lengths)
    return min(names, key=lambda name: abs(len(name) - avg_length))