"""
Complete Rock Paper Scissors game with all features.
Includes score tracking, multiple rounds, and statistics.
"""

import random
from time import sleep

CHOICES = ["rock", "paper", "scissors"]

def get_player_choice():
    while True:
        print("\nChoices:", ", ".join(CHOICES))
        choice = input("Enter your choice: ").lower().strip()
        
        if choice in CHOICES:
            return choice
        
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(CHOICES):
                return CHOICES[choice_index]
        except ValueError:
            pass
            
        print("Invalid choice! Please try again.")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 0
    
    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    return 1 if winning_moves[player_choice] == computer_choice else -1

def display_score(player_score, computer_score, ties):
    print("\nCurrent Score:")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {ties}")

def play_round(player_score, computer_score, ties):
    print("\n" + "="*30)
    player_choice = get_player_choice()
    
    print("\nRock...")
    sleep(0.5)
    print("Paper...")
    sleep(0.5)
    print("Scissors...")
    sleep(0.5)
    
    computer_choice = random.choice(CHOICES)
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    
    if result == 1:
        print("You win this round!")
        player_score += 1
    elif result == -1:
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")
        ties += 1
    
    return player_score, computer_score, ties

def play_game():
    print("Welcome to Rock Paper Scissors!")
    player_name = input("Enter your name: ")
    rounds_to_win = 3
    
    player_score = 0
    computer_score = 0
    ties = 0
    
    while True:
        player_score, computer_score, ties = play_round(
            player_score, computer_score, ties
        )
        
        display_score(player_score, computer_score, ties)
        
        # Check for overall winner
        if player_score >= rounds_to_win:
            print(f"\nCongratulations {player_name}! You've won the game!")
            break
        elif computer_score >= rounds_to_win:
            print(f"\nGame Over! The computer has won!")
            break
        
        # Ask to play again
        if input("\nPlay another round? (yes/no): ").lower() != "yes":
            print("\nFinal Score:")
            display_score(player_score, computer_score, ties)
            print(f"\nThanks for playing, {player_name}!")
            break

if __name__ == "__main__":
    play_game() 