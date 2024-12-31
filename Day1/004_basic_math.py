"""
A program that demonstrates basic arithmetic operations in Python.
It takes two numbers from the user and shows different mathematical operations.
"""

# Get input from user and convert it to integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform and display basic arithmetic operations
print(f"\nMath operations with {num1} and {num2}:")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Integer Division: {num1} // {num2} = {num1 // num2}")
print(f"Remainder (modulo): {num1} % {num2} = {num1 % num2}")
print(f"Power: {num1} ** {num2} = {num1 ** num2}") 