# nlogn  -  n^2
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr    # the stop condition is when only 1 element
    else:
        pivot = random.choice(arr)     #pick a random pivot
        smaller = [x for x in arr if x < pivot]     #array for smaller ones
        equal = [x for x in arr if x == pivot]    #array for equal
        larger = [x for x in arr if x > pivot]    #array for bigger
        print(pivot)
        print(smaller)
        print(equal)
        print(larger)
        
        return quick_sort(smaller) + equal + quick_sort(larger)     #recursively sort the smaller , bigger and place everything in order

# Example usage
arr = [4, 2, 7, 1, 9, 5]
sorted_arr = quick_sort(arr)
print(sorted_arr)

