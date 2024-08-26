def hybrid_sort(arr, threshold):
    if len(arr) <= threshold:
        insertion_sort(arr)
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        hybrid_sort(left, threshold)
        hybrid_sort(right, threshold)

        merge(arr, left, right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage
arr = [5, 2, 8, 1, 9]
threshold = 5
hybrid_sort(arr, threshold)
print(arr)

