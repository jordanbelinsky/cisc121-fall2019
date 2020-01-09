"""
Towers of Hanoi. Based on a program by James Rodger, Margaret Lamb, and
Wendy Powley.

This is a recursive solution to an old puzzle.
"""
def move_disks(h, source, dest, spare, count=0):
    if (h > 0):
        ##print('Making recursive call.')
        count = move_disks(h - 1, source, spare, dest, count+1)
        ##print("move disk", h, "from" , source , "to", dest)
        ##print('Making recursive call.')
        count = move_disks(h - 1, spare, dest, source, count+1)
        return count
    return count
    
def main():
    disk_count = 6
    # This loop runs the Towers of Hanoi recursive algorithm on disk heights
    # from 0 to disk_count.
    for height in range(disk_count + 1):
        # Print the number of recursive calls
        print(move_disks(height, 'A', 'C', 'B'))
    print()

    # This loop calculates and displays the result of 2**(n+1)-2 for values of
    # n from 0 to disk_count. You'll note the values displayed are the same as
    # those printed in the first loop.
    for n in range(disk_count + 1):
        print(2**(n+1)-2)

main()
