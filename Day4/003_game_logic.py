"""
Implementing the core game logic for Rock Paper Scissors.
Shows how to determine the winner of a round.
"""

def determine_winner(player_choice, computer_choice):
    """
    Determine the winner of the game.
    Returns: 1 for player win, -1 for computer win, 0 for tie
    """
    if player_choice == computer_choice:
        return 0
    
    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_moves[player_choice] == computer_choice:
        return 1
    return -1

def get_result_message(result, player_choice, computer_choice):
    """Get a formatted message for the game result."""
    if result == 0:
        return f"Tie! Both chose {player_choice}"
    elif result == 1:
        return f"You win! {player_choice} beats {computer_choice}"
    else:
        return f"Computer wins! {computer_choice} beats {player_choice}"

# Test the game logic
test_cases = [
    ("rock", "scissors"),
    ("paper", "rock"),
    ("scissors", "paper"),
    ("rock", "rock"),
]

print("Testing game logic:")
for player, computer in test_cases:
    result = determine_winner(player, computer)
    message = get_result_message(result, player, computer)
    print(f"\nPlayer: {player}")
    print(f"Computer: {computer}")
    print(f"Result: {message}") 