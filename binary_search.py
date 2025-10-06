def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

#   1.1 Suppose you have a sorted list of 128 names, and you’re searching
#   through it using binary search. What’s the maximum number of
#   steps it would take?

#   log(128) = 7

#   1.2 Suppose you double the size of the list. What’s the maximum
#   number of steps now?

#   log(256) = 8