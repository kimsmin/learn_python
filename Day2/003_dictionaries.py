"""
Introduction to dictionaries in Python.
Demonstrates creating, accessing, and modifying dictionaries.
"""

# Create a simple dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing dictionary values
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Modifying dictionary values
person["age"] = 31
person["occupation"] = "Developer"  # Adding new key-value pair

# Dictionary methods
print("\nDictionary keys:", person.keys())
print("Dictionary values:", person.values())

# Checking if key exists
if "name" in person:
    print(f"\nFound name: {person['name']}") 