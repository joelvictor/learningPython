# Using parentheses
my_tuple = (1, 2, 3)

# Without parentheses (tuple packing)
my_tuple = 1, 2, 3

# From a list
my_tuple = tuple([1, 2, 3])

# Empty tuple
my_tuple = ()

# Single element tuple
my_tuple = (1,)

# Tuple unpacking
a, b, c = my_tuple

# Iterating through a tuple
for item in my_tuple:
    print(item)

# Tuple methods
count = my_tuple.count(1)  # Count occurrences of 1
index = my_tuple.index(2)  # Find the index of 2

# Tuple immutability
# my_tuple[0] = 4  # This will raise an error

# Tuple concatenation
new_tuple = my_tuple + (4, 5, 6)

# Tuple slicing
slice_tuple = my_tuple[1:3]