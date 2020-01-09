"""
Towers of Hanoi. Based on a program by James Rodger, Margaret Lamb, and
Wendy Powley.

This is a recursive solution to an old puzzle.
"""
def move_disks(h, source, dest, spare):
    if (h > 0):
        move_disks(h - 1, source, spare, dest)
        print("move disk", h, "from" , source , "to", dest)
        move_disks(h - 1, spare, dest, source)
    
def main():
    print('Demonstration of Moves to Solve Towers of Hanoi Puzzle')
    height = int(input('Enter the number of disks: '))
    print('Towers of Hanoi of height', height)
    move_disks(height, 'A', 'C', 'B')
    print('Done!')

main()
