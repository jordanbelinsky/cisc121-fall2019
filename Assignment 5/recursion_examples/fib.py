"""
Demonstration of naiive, recursive Fibonacci number generator. Complexity is
exponential (O(2**n)).
"""

def fib(n):
    """Returns the nth Fibonacci number, where n should be a non-negative
    integer. Returns None if n is not a non-negative integer.
    """
    try:
        if n != int(n): # reject non-integers (but accept integer floats)
            return None # n is a non-integer float
    except:
        return None # n is not a number
    if n == 0:      # base case
        return 0    # no recursion
    elif n == 1:    # other base case
        return 1    # still no recursion
    elif n > 1:     # process positive values for n greater than 1
        return fib(n-1) + fib(n-2) # two recursive calls!
    else:
        return None # n is negative

def main():
    print(fib('Fred')) # should be None
    for i in range(-2, 8):
        print(fib(i)) # first two should be None

main()
