# Using a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

### Using `for` Loop with `range()`

# Using a for loop with range()
for i in range(len(fruits)):
    print(fruits[i])

### Using `while` Loop

# Using a while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

### Using List Comprehension

# Using list comprehension
[print(fruit) for fruit in fruits]

### Using `enumerate()`
# Using enumerate() to get index and value
for index, fruit in enumerate(fruits):
    print(index, fruit)

# These examples demonstrate different ways to iterate over a list in Python, allowing you to choose the method that best fits your needs.