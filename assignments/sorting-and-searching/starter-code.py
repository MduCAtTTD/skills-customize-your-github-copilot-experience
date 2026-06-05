import time
import random


def bubble_sort(numbers):
    """Sort a list of numbers in ascending order using bubble sort.
    
    Do NOT use Python's built-in sort() or sorted().
    """
    # TODO: Implement bubble sort
    pass


def binary_search(sorted_list, target):
    """Search for target in a sorted list using binary search.
    
    Return the index of target if found, or -1 if not found.
    """
    # TODO: Implement binary search
    pass


def compare_performance():
    """Compare bubble sort vs built-in sorted() on different list sizes."""
    sizes = [100, 1000, 10000]

    print(f"{'Size':<10} {'Bubble Sort (s)':<20} {'Built-in sorted (s)':<20}")
    print("-" * 50)

    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]

        # TODO: Time bubble_sort on a copy of data and store result in bubble_time

        # TODO: Time sorted() on data and store result in builtin_time

        # TODO: Print a row of the comparison table
        pass

    # TODO: Add a comment below explaining which method is faster and why
    # 


if __name__ == "__main__":
    # Test bubble_sort
    print(bubble_sort([5, 3, 8, 1, 2]))       # Expected: [1, 2, 3, 5, 8]

    # Test binary_search
    print(binary_search([1, 2, 3, 5, 8], 3))  # Expected: 2
    print(binary_search([1, 2, 3, 5, 8], 7))  # Expected: -1

    # Run performance comparison
    compare_performance()
