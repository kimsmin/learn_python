"""
Introduction to functions in Python.
Shows how to define and use functions with different parameter types.
"""

def greet(name):
    """Simple function that returns a greeting."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Function that adds two numbers together."""
    return a + b

def calculate_rectangle_area(length, width=10):
    """Function with a default parameter."""
    return length * width

# Using the functions
print(greet("Alice"))
print(f"Sum of 5 and 3 is: {add_numbers(5, 3)}")
print(f"Rectangle area: {calculate_rectangle_area(5)}")  # Uses default width
print(f"Rectangle area: {calculate_rectangle_area(5, 20)}")  # Specifies width 