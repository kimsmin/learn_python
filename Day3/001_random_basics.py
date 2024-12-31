"""
Introduction to random numbers in Python.
Shows how to generate and work with random numbers.
"""

import random  # Import the random module

# Generate a random integer between 1 and 10
number = random.randint(1, 10)
print(f"Random number: {number}")

# Generate multiple random numbers
print("\nFive random numbers between 1 and 10:")
for _ in range(5):
    print(random.randint(1, 10))

# Using random.choice with a list
choices = ["rock", "paper", "scissors"]
print(f"\nRandom choice: {random.choice(choices)}")

# Random floating point number between 0 and 1
print(f"\nRandom float: {random.random()}") 