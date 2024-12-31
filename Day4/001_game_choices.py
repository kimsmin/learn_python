"""
Introduction to game choices and basic game setup for Rock Paper Scissors.
Shows how to work with game choices and random selection.
"""

import random

# Define the possible choices
CHOICES = ["rock", "paper", "scissors"]

def get_computer_choice():
    """Get a random choice for the computer."""
    return random.choice(CHOICES)

# Test the random choice generation
print("Testing computer choices:")
for _ in range(5):
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

# Show all possible choices
print("\nAvailable choices:")
for i, choice in enumerate(CHOICES, 1):
    print(f"{i}. {choice}") 