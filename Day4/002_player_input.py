"""
Adding player input validation for Rock Paper Scissors.
Shows how to get and validate player choices.
"""

CHOICES = ["rock", "paper", "scissors"]

def get_player_choice():
    """Get and validate the player's choice."""
    while True:
        print("\nChoices:", ", ".join(CHOICES))
        choice = input("Enter your choice: ").lower().strip()
        
        if choice in CHOICES:
            return choice
        
        # Allow number inputs (1 for rock, 2 for paper, 3 for scissors)
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(CHOICES):
                return CHOICES[choice_index]
        except ValueError:
            pass
            
        print("Invalid choice! Please try again.")

# Test the player input
print("Testing player input:")
player_choice = get_player_choice()
print(f"You chose: {player_choice}") 