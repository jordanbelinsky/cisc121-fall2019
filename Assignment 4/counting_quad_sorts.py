"""
Name: Jordan Belinsky
Assignment: 4
Module: Counting Quadratic Sorts
"""

def bubble_sort(items):
    """
    Implementation of bubble sort for testing purposes.

    Parameters: items (list)

    Returns: a count of the number of passes for inner and outer loops
    """

    # Define variables
    count = 0
    n = len(items)
    swapped = True
    while swapped:
        # Increase swap count for outer loop
        count += 1
        swapped = False
        for i in range(1,n):
            # Increase swap count for inner loop
            count += 1
            # If last item is greater than current item, swap them
            if items[i-1] > items[i]:
                items[i-1], items[i] = items[i], items[i-1]
                swapped = True
    return count

def insertion_sort(items):
    """
    Implementation of insertion sort for testing purposes.

    Parameters: items (list)

    Returns: a count of the number of passes for inner and outer loops
    """

    # Define variables
    count = 0
    n = len(items)
    i = 1
    while i < n:
        # Increase swap count for outer loop
        count += 1
        j = i
        while j > 0 and items[j-1] > items[j]:
            # Increase swap count for inner loop
            count += 1
            # If last item is greater than current item, swap them
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
        i += 1
    return count

def optimized_bubble_sort(items):
    """
    Implementation of optimized bubble sort for testing purposes.

    Parameters: items (list)

    Returns: a count of the number of passes for inner and outer loops
    """

    # Define variables
    count = 0
    n = len(items)
    swapped = True
    while swapped:
        # Increase swap count for outer loop
        count += 1
        swapped = False
        for i in range(1,n):
            # Increase swap count for inner loop
            count += 1
            # If last item is greater than current item, swap them
            if items[i-1] > items[i]:
                items[i-1], items[i] = items[i], items[i-1]
                swapped = True
        n -= 1
    return count

def selection_sort(items):
    """
    Implementation of selection sort for testing purposes.

    Parameters: items (list)

    Returns: a count of the number of passes for inner and outer loops
    """

    # Define variables
    count = 0
    n = len(items)
    for i in range(n-1):
        # Increase swap count for outer loop
        min = i
        count += 1
        for j in range(i+1,n):
            # Increase swap count for inner loop
            count += 1
            if (items[j] < items[min]):
                min = j
        if (min != i):
            # If minimum does not equal the current item, swap them
            items[i], items[min] = items[min], items[i]
    return count