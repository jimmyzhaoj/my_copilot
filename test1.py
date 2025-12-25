"""Simple math functions."""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b, with error handling for division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b