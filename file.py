with open("file.txt","w")as f:
    f.write("Abcd xyz")

with open("file.txt",'r') as f1:
    b = f1.read()
    a = b[::-1]
    with open("f1",'w')as f2:
        f2.write(a)

f = open("file1.txt",'w')
f.write("appium ")

with open("file1.txt","r")as f:
    a = f.read()
    b = a[::-1]
    with open("file2.txt","w")as f2:
        f2.write(b)

f = open("file1.txt","r")
a = f.read()
b = a[::-1]
f2 = open("filee2.txt",'w')
f2.write(b)
f = open("file1.txt","r")
print(f.read(5))


with open("abc.txt","w")as f1:
    f1.write("r-open an existing file for a read operations\n"
             " w: open an existing file for \n"
             "a write operation.\n "
             "If the file already contains some data, then \n"
             "it will be overridden but if the file is \n"
             "not present"
             )
# f1 = open("abc.txt","r")
# for x in f1:
#     print(x)
# #print(f1.read(5))
# print(f1.readlines())
f1 = open("abc.txt","r")
# print(f1.readlines()[-5:])
data = f1.readlines()[-5:]
# last_line = data[-5:]
for line in data:
    print(line)
f = open("file.txt","r")
a = f.read()
count=0
for x in a:
    count+=1
print(count)

word = a.split()
print(len(word))

str = 'hi hello'
count = 0
for i in str:
    count += 1
print(count)
def count_vowel():
    f = open("file.txt","r")
    a = f.read()
    count=0
    for x in a:
        if x in 'aeiouAEIOU':
            count+=1
    return count
print(count_vowel())

f = open("file.txt","r")
a = f.readlines()
print(max(a , key=len))

a=[1,3,86,98,4]
large = a[0]
for ele in a:
    if ele<large:
        large = ele
print(large)

a=[1,3,86,98,4]
count = 0
for i in a:
    count+=i
print(count)

a = "hi hello hi"
b = a.split()
print(len(b[-1]))
print(b[-1])

count = 0
for i in a:
    count+=1
print(count)

a = "hi hello hi"
word=a.split()
str = ''
for i in word:
    if i not in str:
        str=i+' '+str
print(str)

list1=[]
word=[1,5,3,4,6,3]
for i in word:
    if i not in list1:
        list1.append(i)
print(list1)

rev_str=''
a = "hi hello hi"
index = len(a)-1
while index>=0:
    rev_str+=a[index]
    index-=1
print(rev_str)

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

fruits = "apple"
a=[x for x in fruits if x in "aeiou"]
print(a)
