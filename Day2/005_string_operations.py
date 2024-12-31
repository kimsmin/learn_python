"""
Advanced string operations in Python.
Demonstrates various string manipulation techniques.
"""

# String methods
text = "  Hello, Python Programming!  "
print(f"Original text: '{text}'")
print(f"Uppercase: '{text.upper()}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Stripped: '{text.strip()}'")

# String splitting and joining
words = text.split()
print(f"\nWords list: {words}")
print(f"Joined back: {'_'.join(words)}")

# String searching
sentence = "Python is amazing and Python is fun"
print(f"\nCount of 'Python': {sentence.count('Python')}")
print(f"'amazing' starts at index: {sentence.find('amazing')}")

# String formatting
name = "Alice"
age = 25
print("\nDifferent ways to format strings:")
print("Using .format(): {} is {} years old".format(name, age))
print(f"Using f-strings: {name} is {age} years old")
print("Using %% operator: %s is %d years old" % (name, age)) 