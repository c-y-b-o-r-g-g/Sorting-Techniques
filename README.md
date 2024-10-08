# Sorting-Techniques

This project contains implementations of various sorting algorithms in Python. Sorting algorithms are fundamental in computer science and are used to arrange data in a particular order. This README provides a brief description of each sorting technique and explains the graphs included in the `images` directory.

## Table of Contents

- Sorting Techniques
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Heap Sort
- Graphs Explanation
- Contributing

## Sorting Techniques

### Bubble Sort

Bubble Sort is a simple comparison-based algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

### Selection Sort

Selection Sort divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted. It repeatedly selects the smallest (or largest) element from the unsorted sublist, swaps it with the leftmost unsorted element, and moves the sublist boundaries one element to the right.

### Insertion Sort

Insertion Sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, it is efficient for small data sets or nearly sorted data.

### Merge Sort

Merge Sort is an efficient, stable, comparison-based, divide-and-conquer sorting algorithm. Most implementations produce a stable sort, meaning that the order of equal elements is the same in the input and output. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

### Quick Sort

Quick Sort is a highly efficient sorting algorithm and is based on the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.

### Heap Sort

Heap Sort is a comparison-based sorting technique based on a binary heap data structure. It is similar to selection sort where we first find the maximum element and place it at the end. We repeat the same process for the remaining elements.

## Graphs Explanation

The `images` directory contains graphs that illustrate the performance of each sorting algorithm. Here is a brief explanation of each graph:

- **Time Complexity Graphs**: These graphs show the time complexity of each sorting algorithm. The x-axis represents the size of the input array, and the y-axis represents the time taken to sort the array. The graphs help visualize how the performance of each algorithm scales with the size of the input.

- **Space Complexity Graphs**: These graphs show the space complexity of each sorting algorithm. The x-axis represents the size of the input array, and the y-axis represents the amount of memory used. These graphs help understand the memory efficiency of each algorithm.

- **Comparison Graphs**: These graphs compare the performance of different sorting algorithms on the same input data. They help identify which algorithm performs better under various conditions.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request
