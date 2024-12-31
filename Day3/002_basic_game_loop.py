"""
Introduction to game loops and user input validation.
Basic structure for a guessing game.
"""

def get_valid_number():
    """Get a valid number from the user between 1 and 100."""
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Number must be between 1 and 100!")
        except ValueError:
            print("Please enter a valid number!")

# Simple game loop
print("Welcome to the Number Guessing Game!")
user_input = get_valid_number()
print(f"You entered: {user_input}") 