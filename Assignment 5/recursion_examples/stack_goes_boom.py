"""
This program does nothing useful apart from demonstrating how the Python 3
stack blows up after a finite number of recursive calls.
"""

def main():
    print('Stuff')
    print('happens')
    print('here.')
    print()
    main() # Start over!
    print('That\'s all, folks!')

main()
