import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr    # the stop condition is when only 1 element
    else:
        pivot = random.choice(arr)     #pick a random pivot
        smaller = [x for x in arr if x < pivot]     #array for smaller ones
        equal = [x for x in arr if x == pivot]    #array for equal
        larger = [x for x in arr if x > pivot]    #array for bigger
        # print(pivot)
        # print(smaller)
        # print(equal)
        # print(larger)
        
        return quick_sort(smaller) + equal + quick_sort(larger)     #recursively sort the smaller , bigger and place everything in order

def merge_sort(arr):    #divide
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):     #compare
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged


def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    # print(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # print(arr)

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            # print(arr)
        
        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr







def generate_random_array(size):
   """Generates a random array of integers with the given size."""
   return [random.randint(0, 1000) for _ in range(size)]

sizes = [1000, 25000, 50000, 100000]  # Add more sizes as needed

for size in sizes:
   arr = generate_random_array(size)

   # Quick Sort
   start_time = time.time()
   quick_sort(arr)  # Assuming you have quick_sort implemented
   end_time = time.time()
   print(f"Running time for Quick Sort with size {size} is {end_time - start_time:.4f} ms")

   # Merge Sort
   start_time = time.time()
   merge_sort(arr)  # Assuming you have merge_sort implemented
   end_time = time.time()
   print(f"Running time for Merge Sort with size {size} is {end_time - start_time:.4f} ms")

   # Heap Sort
   start_time = time.time()
   heap_sort(arr)  # Assuming you have heap_sort implemented
   end_time = time.time()
   print(f"Running time for Heap Sort with size {size} is {end_time - start_time:.4f} ms")

   # Insertion Sort
   start_time = time.time()
   insertion_sort(arr)  # Assuming you have insertion_sort implemented
   end_time = time.time()
   print(f"Running time for Insertion Sort with size {size} is {end_time - start_time:.4f} ms")

   # Selection Sort
   start_time = time.time()
   selection_sort(arr)  # Assuming you have selection_sort implemented
   end_time = time.time()
   print(f"Running time for Selection Sort with size {size} is {end_time - start_time:.4f} ms")


