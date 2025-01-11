# Slices 
str = "Hello World"

# First Index is included, last not
# if want to be the first can be str[:4] or to end str[6:]
print(str[0:4])  # Output: Hell
# print(str[:4])  # Output: Hell
print(str[6:])


print(str[-5:])


print(str[0:4:2]) # takes every second character

# print


#To reverse a string can use
print("Reversed String ", str[::-1])
