tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

another_tuple = 1, 2, 3
print(another_tuple)  # Output: (1, 2, 3)

print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Attempting to modify a tuple (will raise an error)
my_tuple[0] = 10  # This will raise a TypeError

# However, you can concatenate or multiply tuples to create new tuples:

# Concatenating tuples
concatenated_tuple = my_tuple + another_tuple
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3)

# Multiplying tuples
multiplied_tuple = another_tuple * 3
print(multiplied_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
