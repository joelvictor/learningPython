# Creating and using a dictionary
student = {
    'name': 'John',
    'age': 20,
    'grades': [85, 90, 78]
}

# Accessing dictionary values
print(student['name'])  # Access using key
print(student.get('age'))  # Access using get() method

# Adding/updating items
student['course'] = 'Python'  # Add new key-value pair
student['age'] = 21  # Update existing value

# Dictionary methods
print(student.keys())  # Get all keys
print(student.values())  # Get all values
print(student.items())  # Get all key-value pairs

# Check if key exists
if 'name' in student:
    print("Name exists in dictionary")

# Remove items
removed_value = student.pop('grades')  # Remove and return value
del student['course']  # Delete key-value pair

# Different ways to create dictionaries
empty_dict = {}  # Empty dictionary
dict_constructor = dict()  # Using dict() constructor
dict_with_items = dict(name='Alice', age=25)  # Using dict() with keywords
dict_from_tuples = dict([('name', 'Bob'), ('age', 30)])  # From list of tuples
dict_comprehension = {x: x*x for x in range(3)}  # Dictionary comprehension

# Dictionary update methods
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Using update() method
dict1.update(dict2)

# Using | operator (Python 3.9+)
combined_dict = dict1 | dict2

# Using dictionary unpacking
merged_dict = {**dict1, **dict2}

# Update multiple values at once
dict1.update({'x': 10, 'y': 20, 'z': 30})

