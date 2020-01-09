"""
This program demonstrates four ways of finding the longest row in a table
(i.e., a list of lists) with rows of different lengths. The first "longest row"
function is iterative, the second recursive, and wasteful of memory since it
creates multiple slices of the table, the third recursive but less wasteful of
space because it uses an optional index parameter to avoid slicing, and the
fourth uses Python 3's map() function with len() to generate an iterator (kind
of like a list) of the lengths of all the table's rows, then simply returns the
max of those.
"""

import random

def longest_row_iterative(table):
    """Returns the length of the longest row or rows in table, which is
    either a multidimensional list or a list of objects (like strings)
    which have measurable lengths.
    """
    if len(table) > 0:
        longest = len(table[0])
        for i in range(1, len(table)):
            longest = max(longest, len(table[i]))
        return longest
    return 0

def longest_row_recursive_slice(table):
    """Returns the length of the longest row or rows in table, which is
    either a multidimensional list or a list of objects (like strings)
    which have measurable lengths.
    """
    if len(table) > 0:
        return max(len(table[0]), longest_row_recursive_slice(table[1:]))
    return 0

def longest_row_recursive_index(table, i=0):
    """Returns the length of the longest row or rows in table, which is
    either a multidimensional list or a list of objects (like strings)
    which have measurable lengths.
    """
    if i < len(table):
        return max(len(table[i]), longest_row_recursive_index(table,i+1))
    return 0

def longest_row_map(table):
    """Returns the length of the longest row or rows in table, which is
    either a multidimensional list or a list of objects (like strings)
    which have measurable lengths.
    """
    if len(table) > 0:
        return max(map(len, table))
    return 0

def yes_no(prompt):
    """Returns the length of the longest row or rows in table, which is
    either a multidimensional list or a list of objects (like strings)
    which have measurable lengths.
    """
    while True:
        response = input(prompt)
        if response in ['y', 'Y', 'n', 'N']:
            break
        print('Your response must be "y" for "yes", or "n" for "no".')
    return response in ['y', 'Y']

def main():
    n = 10
    max_row_len = 20
    min_val = 10
    max_val = 99

    while True:
        a_table = []
        print('The table:')
        for i in range(n):
            a_table.append([])
            for j in range(random.randint(0, max_row_len)):
                a_table[i].append(random.randint(min_val,max_val))
            print(' '.join(str(e) for e in a_table[i]))
        print('Length of longest row:')
        print(longest_row_iterative(a_table))
        print(longest_row_recursive_slice(a_table))
        print(longest_row_recursive_index(a_table))
        print(longest_row_map(a_table))
        if not yes_no('Do again (y, n): '):
            break

    print('Tests with empty table:')
    a_table = []
    print(longest_row_iterative(a_table))
    print(longest_row_recursive_slice(a_table))
    print(longest_row_recursive_index(a_table))
    print(longest_row_map(a_table))
            
main()
