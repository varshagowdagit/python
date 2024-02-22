#general sort
l1=[76, 23, 45, 12, 54, 9]
print("Original List:", l1)

# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]

# sorted list
print("Sorted List", l1)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array using Bubble Sort:", arr)



def insertion_sort(arr):
    n=len(arr)
    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array using Insertion Sort:", arr)



def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array using Selection Sort:", arr)

def b_s(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
a=[5,4,7,1,2,1]
b_s(a)
print(a)

def ins_sort(a):
    n=len(a)
    for i in range(n):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
a=[5,4,7,1,2,1]
ins_sort(a)
print(a)

def se_s(a):
    n =len(a)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
a=[5,4,7,1,2,1]
se_s(a)
print(a)

a=[5,4,7,1,2,1]
# print(a.sort()) or
print(sorted(a))
