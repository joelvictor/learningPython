# Creating a list
my_list = [1, 2, 3, 4, 5]

# append() - Adds an element at the end of the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# insert() - Adds an element at the specified position
my_list.insert(2, 'a')
print(my_list)  # Output: [1, 2, 'a', 3, 4, 5, 6]

# remove() - Removes the first item with the specified value
my_list.remove('a')
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# pop() - Removes the element at the specified position
my_list.pop(3)
print(my_list)  # Output: [1, 2, 3, 5, 6]

# clear() - Removes all the elements from the list
my_list.clear()
print(my_list)  # Output: []

# extend() - Adds the elements of a list (or any iterable) to the end of the current list
my_list.extend([7, 8, 9])
print(my_list)  # Output: [7, 8, 9]

# index() - Returns the index of the first element with the specified value
index = my_list.index(8)
print(index)  # Output: 1

# count() - Returns the number of elements with the specified value
count = my_list.count(8)
print(count)  # Output: 1

# sort() - Sorts the list in ascending order
my_list.sort()
print(my_list)  # Output: [7, 8, 9]

# reverse() - Reverses the order of the list
my_list.reverse()
print(my_list)  # Output: [9, 8, 7]

# copy() - Returns a copy of the list
new_list = my_list.copy()
print(new_list)  # Output: [9, 8, 7]

# Initial list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# del - Remove an element at a specific index
del my_list[0]
print(my_list)  # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# del - Remove a slice of elements
del my_list[2:5]
print(my_list)  # Output: [2, 3, 7, 8, 9]

# del - Remove the entire list
del my_list
# print(my_list)  # This will raise an error because my_list no longer exists
