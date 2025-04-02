def find_closest_name_by_length(names: list) -> str or None:
    """
    Find the name whose length is closest to the average length of all names.

    Args:
        names (list): List of name strings. Can be empty.

    Returns:
        str or None: Name closest to average length, or None if list is empty.
    """
    if not names:
        return None

    lengths = [len(name) for name in names]
    avg_length = sum(lengths) / len(lengths)
    return min(names, key=lambda name: abs(len(name) - avg_length))
