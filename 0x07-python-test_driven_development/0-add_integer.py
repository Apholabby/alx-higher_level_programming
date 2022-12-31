#!/usr/bin/python3
def add_integer(a, b=98):
    """add two integers.
    Args:
        a (int), b (int): The integers to be added together.
    Returns:
        The addition of a and b (int).
    """
    if type(a) is not int and type(b) is not int:
        raise TypeError("{} must be an integer".format(a, b))
    elif a == float and b == float:
        return int(a) and int(b)
    else:
        return a + b

    print("{}".format(add_integer(1, b)))
