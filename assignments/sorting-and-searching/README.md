# 📘 Assignment: Sorting and Searching Algorithms

## 🎯 Objective

Implement classic sorting and searching algorithms from scratch in Python to understand how computers organize and find data efficiently — without using built-in sort or search functions.

## 📝 Tasks

### 🛠️ Implement Bubble Sort

#### Description
Write a function called `bubble_sort()` that sorts a list of numbers in ascending order using the bubble sort algorithm.

#### Requirements
Completed program should:

- Accept a list of integers as input
- Sort the list in ascending order by repeatedly swapping adjacent elements that are out of order
- Return the sorted list without using Python's built-in `sort()` or `sorted()`
- Example usage:
  ```python
  print(bubble_sort([5, 3, 8, 1, 2]))  # [1, 2, 3, 5, 8]
  ```

### 🛠️ Implement Binary Search

#### Description
Write a function called `binary_search()` that searches for a target value in a **sorted** list and returns its index.

#### Requirements
Completed program should:

- Accept a sorted list and a target value as arguments
- Use the binary search algorithm to find the target by repeatedly halving the search range
- Return the index of the target if found, or `-1` if it is not in the list
- Example usage:
  ```python
  print(binary_search([1, 2, 3, 5, 8], 3))   # 2
  print(binary_search([1, 2, 3, 5, 8], 7))   # -1
  ```

### 🛠️ Compare Performance

#### Description
Measure and compare how long bubble sort takes versus Python's built-in `sorted()` on lists of different sizes.

#### Requirements
Completed program should:

- Use the `time` module to measure the execution time of each approach
- Test on lists of at least three different sizes (e.g., 100, 1000, 10000 elements)
- Print a comparison table showing the time taken by each method for each list size
- Write a short comment in the code explaining which method is faster and why
