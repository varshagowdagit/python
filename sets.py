# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating a set using set() constructor
another_set = set([3, 4, 5, 6, 7])
print(another_set)  # Output: {3, 4, 5, 6, 7}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {4, 5}

# Difference of sets
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2, 3}

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

my_set = {1, 2, 3}
my_set.add(4)  # Adding a single element
print(my_set)  # Output: {1, 2, 3, 4}

my_set.update([5, 6, 7])  # Adding multiple elements
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

my_set.remove(3)  # Removing an element
print(my_set)  # Output: {1, 2, 4, 5, 6, 7}

