"""
A program that demonstrates conditional statements in Python.
It asks for a name and provides different greetings based on whether
the name entered is 'Joe' or not.
"""

name = input("Enter your name: ")  # Get user input and store it in 'name' variable
if name == "Joe":  # Check if the entered name is "Joe"
    print("Hello, Joe!")  # Special greeting for Joe
else:
    print("Hello, stranger!")  # Generic greeting for everyone else