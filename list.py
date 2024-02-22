my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
print(my_list[-1]) # Output: 5 (last element)

my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

my_list.extend([7, 8])
print(my_list)  # Output: [10, 2, 3, 4, 5, 6, 7, 8]
#Append function in Python adds a single element to the end of the list,
# whereas the extend function adds multiple elements (from an iterable) to the list

my_list.remove(3)
print(my_list)  # Output: [10, 2, 4, 5, 6, 7, 8]

popped_value = my_list.pop(2)  # Remove element at index 2
print(popped_value)            # Output: 4
print(my_list)                 # Output: [10, 2, 5, 6, 7, 8]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

print(len(my_list))  # Output: 6

count=0
for i in my_list:
    count+=1
print(count)

count=0
for i in my_list:
    count+=i
print(count)

my_list.sort()
print(my_list)  # Output: [2, 5, 6, 7, 8, 10]

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = list(set(numbers))
print(unique_numbers)  # Output: [1, 2, 3, 4]


  #list comprehension
fruits=["apple", "banana", "cherry"]
newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in range(10) if x < 5]

squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]

string = "hello"
up = [x.upper() for x in string]
print(up)  # Output: ['H', 'E', 'L', 'L', 'O']

sentence = "The quick brown fox jumps Over the lazy dog"
vowels = [x for x in sentence if x in 'AEIOUaeiou']
print(vowels)  # Output: ['e', 'u', 'i', 'o', 'o', 'u', 'o', 'e', 'e', 'a', 'o']

#Creating a List of Tuples:

numbers = [1, 2, 3]
tuples = [(x, x**2) for x in numbers]
print(tuples)  # Output: [(1, 1), (2, 4), (3, 9)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64, 100]

#Extracting Initials from a List of Names:
names = ["John Doe", "Alice Smith", "Bob Johnson"]
initials = [name.split()[0][0] + name.split()[1][0] for name in names]
print(initials)  # Output: ['JD', 'AS', 'BJ']

#Mapping Values to Their Types
values = [1, 'two', 3.0, [4, 5], (6, 7)]
types = [type(item) for item in values]
print(types)  # Output: [<class 'int'>, <class 'str'>, <class 'float'>, <class 'list'>, <class 'tuple'>]


# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)
