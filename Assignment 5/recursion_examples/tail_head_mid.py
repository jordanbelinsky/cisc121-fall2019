"""
This program demonstrates tail, head, and middle recursion with simple output.
"""

def tail_rec(n):
    if n > 0: # base case is n <= 0
        print(n)
        tail_rec(n-1)

def head_rec(n):
    if n > 0:
        head_rec(n-1)
        print(n)

def mid_rec(n):
    if n > 0:
        print(n)
        mid_rec(n-1)
        print(n)

def main():
    print('Tail recursion:')
    tail_rec(4)
    print('\nHead recursion:')
    head_rec(4)
    print('\nMiddle recursion:')
    mid_rec(4)

main()
