"""
Complete number guessing game with all features.
Includes score tracking, multiple rounds, and play again functionality.
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

def play_round():
    target = random.randint(1, 100)
    attempts = 0
    
    print("\nI'm thinking of a number between 1 and 100.")
    
    while True:
        guess = get_valid_number()
        attempts += 1
        
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"\nCongratulations! You got it in {attempts} attempts!")
            return attempts

def play_game():
    print("Welcome to the Number Guessing Game!")
    player_name = input("Enter your name: ")
    best_score = float('inf')
    games_played = 0
    
    while True:
        score = play_round()
        games_played += 1
        best_score = min(best_score, score)
        
        print(f"\nGames played: {games_played}")
        print(f"Best score: {best_score} attempts")
        
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\nThanks for playing, {player_name}!")
            print(f"Your best score was {best_score} attempts.")
            break

if __name__ == "__main__":
    play_game() 