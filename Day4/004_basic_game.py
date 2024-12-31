"""
Combining previous concepts into a basic Rock Paper Scissors game.
Includes player input, computer choice, and game logic.
"""

import random

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

def play_game():
    print("Welcome to Rock Paper Scissors!")
    
    # Get choices
    player_choice = get_player_choice()
    computer_choice = random.choice(CHOICES)
    
    # Show choices
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine and show winner
    result = determine_winner(player_choice, computer_choice)
    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play_game() 