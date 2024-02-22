def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if target is not found in the array

# Example usage:
arr = [4, 2, 6, 8, 1, 5, 3]
target = 5
index = linear_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index} using Linear Search")
else:
    print(f"Target {target} not found in the array")


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target if found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Return -1 if target is not found in the array

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 8]
target = 5
index = binary_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index} using Binary Search")
else:
    print(f"Target {target} not found in the array")
