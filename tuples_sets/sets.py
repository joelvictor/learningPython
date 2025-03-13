# Creating sets
set1 = {1, 2, 3, 4, 5}
# Using set() constructor with a list
set2 = set([4, 5, 6, 7, 8])

# Using set() constructor with tuple
# set2 = set((4, 5, 6, 7, 8))
# Using set comprehension
# set2 = {x for x in range(4, 9)}

# 1. Union (|): Combines unique elements from both sets
union_result = set1 | set2  # or set1.union(set2)
print("Union:", union_result)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 2. Intersection (&): Returns common elements
intersection_result = set1 & set2  # or set1.intersection(set2)
print("Intersection:", intersection_result)  # {4, 5}

# 3. Difference (-): Returns elements in first set but not in second
difference_result = set1 - set2  # or set1.difference(set2)
print("Difference:", difference_result)  # {1, 2, 3}

# 4. Symmetric Difference (^): Returns elements in either set, but not both
symmetric_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_diff)  # {1, 2, 3, 6, 7, 8}

# 5. Add and Remove operations
test_set = {1, 2, 3}
test_set.add(4)  # Adds single element
test_set.update([5, 6])  # Adds multiple elements
test_set.remove(6)  # Removes element (raises error if not found)
test_set.discard(7)  # Removes element (no error if not found)
print("Modified set:", test_set)  # {1, 2, 3, 4, 5}

# 6. Membership test
print("Is 4 in set1?", 4 in set1)  # True

# 7. Set comparisons
set3 = {1, 2}
set4 = {1, 2, 3, 4}
print("Is set3 subset of set4?", set3 <= set4)  # True
print("Is set4 superset of set3?", set4 >= set3)  # True