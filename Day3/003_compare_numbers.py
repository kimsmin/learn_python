"""
Adding comparison logic to the game.
Demonstrates how to compare numbers and provide feedback.
"""

import random

def check_guess(guess, target):
    """Compare guess with target and return appropriate message."""
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"

# Test the comparison logic
target_number = random.randint(1, 100)
print("Testing comparison logic:")

test_guesses = [50, 75, 25, target_number]
for guess in test_guesses:
    print(f"\nGuess: {guess}")
    print(f"Result: {check_guess(guess, target_number)}") 