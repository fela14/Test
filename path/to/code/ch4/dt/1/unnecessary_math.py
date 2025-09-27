def multiply(a, b):
    """
    Returns a multiplied by b.

    Usage example as an external user would do:

    >>> import unnecessary_math as um
    >>> um.multiply(4, 3)
    12
    >>> um.multiply('a', 3)
    'aaa'
    
    # doctest: +SKIP  <- prevents doctest from running this inside the module
    """
    return a * b


def divide(a, b):
    """
    Returns a divided by b.

    Usage example as an external user would do:

    >>> import unnecessary_math as um
    >>> um.divide(10, 5)
    2.0

    # doctest: +SKIP
    """
    return a / b
