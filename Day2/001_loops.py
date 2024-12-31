"""
Introduction to loops in Python.
This program demonstrates both for and while loops with practical examples.
"""

# For loop with a list
print("Counting from 1 to 5:")
for number in [1, 2, 3, 4, 5]:
    print(f"Current number: {number}")

# For loop with range
print("\nUsing range to count from 0 to 4:")
for i in range(5):
    print(f"Index: {i}")

# While loop with a condition
print("\nWhile loop countdown:")
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blast off!") 