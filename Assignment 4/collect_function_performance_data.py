"""
Name: Jordan Belinsky
Assignment: 4
Module: Collect Function Performance Data
"""

# Import modules
import random

def test_function(fn, max_n, num_tests):
    """
    This function tests each of the sorts to determine how many swaps occur.

    Parameters: fn (function name)
                max_n (integer)
                num_tests (integer)

    Returns: None
    """
    
    # Open file
    out = open(fn.__name__+".txt", "w+")

    # Set range for pre-defined number of tests
    for i in range(num_tests):
        
        # Generate a random list for testing
        rand_list = [random.random() for x in range(max_n)]
        row = []

        # Run random values through the sorting function
        for n in range(max_n):
            row.append(fn(rand_list[:n]))

        # Write values to a file
        out.write(str(row)+"\n")
    
    # Finish writing
    out.close()

if __name__ == "__main__":
    def insertion_sort_test(items):
        count = 0
        n = len(items)
        i = 1
        while i < n:
            count += 1
            j = i
            while j > 0 and items[j-1] > items[j]:
                count += 1
                items[j], items[j-1] = items[j-1], items[j]
                j -= 1
            i += 1
        return count

    MAX_N = 100
    NUM_TESTS = 100
    test_function(insertion_sort_test, MAX_N, NUM_TESTS)
