# n^2
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)

# Example usage:
arr = [5, 2, 8, 12, 1, 6]
insertion_sort(arr)
print(arr)