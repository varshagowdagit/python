# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

another_dict = dict(name='Alice', age=25, city='London')
print(another_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'London'}

# Modifying a value
my_dict['age'] = 35
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York'}

# Adding a new key-value pair
my_dict['gender'] = 'Male'
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York', 'gender': 'Male'}

# Removing a key-value pair
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'gender': 'Male'}

# Iterating over keys
for key in my_dict:
    print(key)  # Output: name, age, gender

# Iterating over values
for value in my_dict.values():
    print(value)  # Output: John, 35, Male

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)  # Output: name John, age 35, gender Male

#dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)

sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)
#Output :{'O': 'ooo', 'N': 'nnn', 'I': 'iii', 'C': 'ccc', 'D': 'ddd', 'G': 'ggg'}

dic=dict.fromkeys(range(5), True)
print(dic)
#output: {0: True, 1: True, 2: True, 3: True, 4: True}

#nested dict
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people)

#accessing nested dictionary
print(people[2]['age'])

#sort dictionary using key
my_dict = {'b': 2, 'a': 1, 'c': 4}
my_dict1={1:1,4:4,3:3}
sorted_dict = {k: my_dict[k] for k in sorted(my_dict)}
sorted_dict1 = {k: my_dict1[k] for k in sorted(my_dict1)}
print(sorted_dict)
print(sorted_dict1)
