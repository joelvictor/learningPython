# Example of a for loop in Python

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through a range of numbers
for i in range(5):
    print(i)

# Loop through a string
for letter in "hello":
    print(letter)

# Loop while a condition is true
count = 0
while count < 5:
    print(count)
    count += 1

# Loop with an else clause
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Count reached 5")

# Infinite loop (use with caution)
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break  # Exit the loop

# Loop with continue statement
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of the loop when count is 3
    print(count)