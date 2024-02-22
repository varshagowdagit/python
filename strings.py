string1="apple"

print(string1[2]) #index

#loop
for x in "apple":
    print(x)

print(len(string1)) #len

text = "hi friends this is python"  #present in txt or not
print("is" in text)
print("is" not in text)

#slicing
print(string1[::-1])  #reverse
print(string1[1:])
print(string1[:4])
print(string1[1:3])
print(string1[-1:-3])


text = "  hi friends this is python"
print(text.upper())
print(text.isupper())
print(text.lower())
print(text.islower())
print(text.replace("h","H"))
print(text.strip())   #removes whitespace in begining or end
print(text.split())

a ="hi"
b="hello"
c=a +" " +b
print(c) #concatenate

age=23
print("my age is {}".format(age))

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

def swap_case(string):
    swapped = ""
    for char in string:
        if 'A' <= char <= 'Z':  # Check if the character is uppercase
            swapped += chr(ord(char) + 32)  # Convert uppercase to lowercase
        elif 'a' <= char <= 'z':  # Check if the character is lowercase
            swapped += chr(ord(char) - 32)  # Convert lowercase to uppercase
        else:
            swapped += char  # If it's not a letter, keep it unchanged
    return swapped

# Example usage:
original_string = "Hello World"
converted_string = swap_case(original_string)
print("Original string:", original_string)
print("Converted string:", converted_string)

#count no.of character in a string
count = 0
for letter in original_string:
    count+=1
print(count)

#str reverse -3types
s=""
for i in original_string:
    s=i+s
print(s)

print(original_string[::-1])

print(''.join(reversed(original_string)))

a="hello"
upper = ""
for i in a:
    if "a"<= i <="z":
        upper+=chr(ord(i)-32)
print(upper)

a = "HELLO"
lower = ""
for i in a:
    if "A" <= i <= "Z":
        lower += chr(ord(i) + 32)
print(lower)

