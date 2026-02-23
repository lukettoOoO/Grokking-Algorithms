# 4.1 Write out the code for the earlier sum function.
s = 0
def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])
    
print(sum([2, 4, 6]))

# 4.2 Write a recursive function to count the number of items in a list.
def count(arr):
    if arr == []:
        return 0
    else:
        return 1 + count(arr[1:])
    
print(count([2, 4, 6]))

# 4.3 Find the maximum number in a list.
def maxi(arr, m=-999999):
    if arr == []:
        return m
    else:
        if arr[0] > m:
            m = arr[0]
        return maxi(arr[1:], m)
    
print(maxi([2, 4, 6]))

# 4.4 Remember binary search from chapter 1? It’s a divide-and-conquer
# algorithm, too. Can you come up with the base case and recursive
# case for binary search?
def binary_search(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
    
nums = [2, 6, 88, 123, 456, 1128]
print(binary_search(nums, 0, len(nums), 456))