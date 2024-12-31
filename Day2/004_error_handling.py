"""
Introduction to error handling in Python.
Shows how to use try-except blocks to handle potential errors.
"""

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numbers only!"

# Test the function with different inputs
print(divide_numbers(10, 2))  # Normal division
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, "hello"))  # Type error

# Using try-except with user input
try:
    age = int(input("Enter your age: "))
    print(f"Next year you will be {age + 1}")
except ValueError:
    print("Please enter a valid number!") 