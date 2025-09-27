"""
A small module demonstrating multiply and divide with user-friendly doctests.

Users can import the module as:

>>> import unnecessary_math as um
>>> um.multiply(4, 3)
12
>>> um.divide(10, 5)
2.0
"""

def multiply(a, b):
    """
    Multiply two values.

    Usage example as an external user would do:

    >>> um.multiply(4, 3)
    12
    >>> um.multiply('a', 3)
    'aaa'
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers.

    Usage example as an external user would do:

    >>> um.divide(10, 5)
    2.0
    """
    return a / b
