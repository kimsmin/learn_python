"""
Combining previous concepts into a basic number guessing game.
Includes random numbers, input validation, and game logic.
"""

import random

def get_valid_number():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            print("Number must be between 1 and 100!")
        except ValueError:
            print("Please enter a valid number!")

def play_game():
    target = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = get_valid_number()
        attempts += 1
        
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"\nCongratulations! You got it in {attempts} attempts!")
            break

if __name__ == "__main__":
    play_game() 