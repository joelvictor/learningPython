# Truthiness and Falseyness
# In Python, values can be evaluated in a boolean context

# Examples of values that are considered False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool(None))  # False

# Examples of values that are considered True
print(bool(1))  # True
print(bool(0.1))  # True
print(bool("Hello"))  # True
print(bool([1, 2, 3]))  # True
print(bool({"key": "value"}))  # True