#!/usr/bin/python3

def add_integer(a, b=98):
    """add two integers.
    Args:
        a (int), b (int): The integers to be added together.
    Returns:
        The addition of a and b (int).
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("{} must be an integer".format(a))
    elif isinstance(a, float) and isinstance(b, float):
        return int(a) + int(b)
    else:
        return a + b
