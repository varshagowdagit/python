import time

n=5
if n>1:
    for i in range(2,int(n/2)+1):
        if (n%i)==0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")

#fib
n=5
n1,n2=0,1
print("Fib",n1,n2,end=" ")
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()

#max
l=[1,4,7,8]
large=l[0]
for i in range(len(l)):
    if l[i]>=large:
        large=l[i]
print(large)

str='apple'
print(str[::-1])

print(''.join(reversed(str)))

str2=''
for i in str:
    str2=i+str2
print(str2)


l=[1,4,7,8]
l2=[]
for i in l:
    l2=[i]+l2
print(l2)

str="malayalam"
if(str==str[::-1]):
    print("palindrome")
else:
    print("not palindrome")

count=0
for i in l:
    count+=i
print(count)

# #fact
# fact=1
# n=int(input("Enter the number"))
# if n<0:
#     print("no -ve number")
# elif n==0:
#     print("fact of 0 is 1")
# else:
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
#
# fact=1
# if n<0:
#     print("na")
# elif n==0:
#     print("fact of 0 is 1")
# elif n>0:
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
#
# n=int(input("enter number"))
# rev=0
# temp=n
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("pal")
# else:
#     print("no")
#
# n=int(input("enter number"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("Pal")
# else:
#     print("not")

a =input("enter text")
b=[x for x in a if x in "aeiou"]
print(b)
print(len(b))

import subprocess
p=subprocess.run(['dir'],shell=True)
print(p)
p=subprocess.run(['ipconfig/all'],shell=True)
print(p)

import math
print(math.sqrt(25))

import random
print(random.randint(1,8))

import sys
print(sys.path_hooks)
print(sys.path)
print(time.time())
