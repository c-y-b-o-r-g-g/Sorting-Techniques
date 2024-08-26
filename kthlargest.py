import random
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# def partition(arr,low,high):
#     if len(arr) <= 1:
#         return arr  # the stop condition is when only 1 element
#     else:
#         pivot = random.choice(arr)  # pick a random pivot
#         smaller = [x for x in arr if x < pivot]  # array for smaller ones
#         equal = [x for x in arr if x == pivot]  # array for equal
#         larger = [x for x in arr if x > pivot]  # array for bigger
#         # print(pivot)
#         # print(smaller)
#         # print(equal)
#         # print(larger)
#
#         # return partition(smaller,low,high) + equal + partition(larger,low,high)  # recursively sort the smaller , bigger and place everything in order
#

def find_kth_largest(arr, k):
    low = 0
    high = len(arr) - 1
    while True:
        pivot_index = partition(arr, low, high)
        if pivot_index == len(arr) - k:
            return arr[pivot_index]
        elif pivot_index < len(arr) - k:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

# Example usage
arr = [3, 41, 16, 25, 63, 52, 40]
k = 3
kth_largest = find_kth_largest(arr, k)
print(f"{k}th largest Element is {kth_largest}")


