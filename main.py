# This is a legacy application with NO test suite.
# Our agent will have to generate its own test.

def multiply(a, b):
    """A function that works correctly."""
    return a * b

def buggy_divide(a, b):
    """A function with a deliberate bug."""
    # The bug is here! It should be a / b.
    return a * b