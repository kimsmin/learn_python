"""
A program that demonstrates basic list operations in Python.
Shows how to create, access, and modify lists, which are fundamental
data structures in Python.
"""

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")

# Adding elements to the list
numbers.append(6)  # Add to the end
print(f"After append(6): {numbers}")

# Accessing elements
print(f"\nFirst element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")

# Modifying elements
numbers[0] = 10  # Change the first element
print(f"\nAfter changing first element: {numbers}")

# List slicing
print(f"First three elements: {numbers[:3]}")
print(f"Last three elements: {numbers[-3:]}")

# List operations
more_numbers = [7, 8, 9]
combined = numbers + more_numbers  # Concatenating lists
print(f"\nCombined list: {combined}")

# Some useful list methods
combined.sort()  # Sort the list
print(f"Sorted list: {combined}")
print(f"List length: {len(combined)}")

# Check if element exists in list
print(f"\nIs 5 in the list? {5 in combined}")
print(f"Is 20 in the list? {20 in combined}") 