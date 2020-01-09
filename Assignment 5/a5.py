"""
Name: Jordan Belinsky
Assignment: 5
Module: Main Program
"""

def split_int_pairs(ints):
    """
    Returns a copy of ints, a list of integers, with the value None
    inserted between any two identical values. For example:
        split_int_pairs([])
            returns []
        split_int_pairs([-5])
            returns [-5]
        split_int_pairs([-5, 1])
            returns [-5, 1]
        split_int_pairs([-5, -5])
            returns [-5, None, -5]
        split_int_pairs([0, 1, 0, 1, 1, 0, 0])
            returns [0, 1, 0, 1, None, 1, 0, None, 0]
    """
    if len(ints) < 2:
        return ints
    else:
        if ints[0] == ints[1]:
            copied = ints.copy()
            ints = []
            ints.append(copied[0])
            ints.append(None)
            ints.extend(split_int_pairs(copied[1:]))
            return ints
        else:
            copied = [ints[0]]
            copied.extend(split_int_pairs(ints[1:]))
            return copied

def count_split_char_pairs(s):
    """
    Returns an integer representing the number of occurrences of two
    identical characters being separated by one other (i.e., non-identical)
    character in string s. For example:
        count_split_char_pairs('')
            returns 0
	    count_split_char_pairs('aA')
            returns 0
        count_split_char_pairs('aAa')
            returns 1
        count_split_char_pairs('bAbA')
            returns 2
        count_split_char_pairs('BcBcBc')
            returns 4 (from overlapping split pairs BcB, cBc, BcB, and cBc)
    """
    if len(s) <= 2:
        return 0
    if s[0] == s[2]:
        return 1 + count_split_char_pairs(s[1:])
    else:
        return 0 + count_split_char_pairs(s[1:])

def check_nesting(s):
    """
    s is a str containing only square brackets, '[' and ']'. Returns True
    if s is a nesting of zero or more pairs of square brackets, and False
    otherwise. For example:
        check_nesting('')
            returns True (i.e., 0 pairs of square brackets)
        check_nesting('[')
            returns False
        check_nesting('[]')
            returns True
        check_nesting('[]]')
            returns False
        check_nesting('[[]]')
            returns True
        check_nesting('[[[[[[[[[]]]]]]]]]')
            returns True
    """
    if s == "" or s == "[]":
        return True
    if len(s)%2 != 0:
        return False
    if len(s) > 1 and s[0] == "[" and s[-1] == "]":
        return check_nesting(s[1:-1])
    else: 
        return False

def find_double(ints, index=0):
    """
    Returns True if integer list ints contains two adjacent elements where the
    second element is twice the value of the first. 
        find_double([])
            returns False
        find_double([3])
            returns False
        find_double([3, 5])
            returns False
        find_double([3, 5, 6])
            returns False (since although 3 * 2 is 6, the 6 does not immediately follow the 3)
        find_double([3, 6])
            returns True (since 3 * 2 is 6, and 3 comes before 6 in ints)
        find_double([7, 8, 16, 15, 3, 22])
            returns True (since 8 * 2 is 16, and 8 comes before 16 in ints)
        find_double([7, 8, 16, 14, 28, 22])
            returns True (since 8 * 2 is 16, and 8 comes before 16 in ints)
    Note from that last example, that there are two pairs of values where one
    is the double of the other (8, 16, and 14, 28), but only one such pair is
    required for the function to return True.

    Parameters: ints is a list of 0 or more integers.
                index is an in indicating an index position.  This parameter is optional.  The default is 0.
    """
    if len(ints) < 2:
        return False
    if 2*(ints[0]) == ints[1]:
        return True
    else:
        return find_double(ints[1:])

def climbing_patterns_count(n):
    """
    Returns an integer representing the number of possible patterns of climbing
    a ladder with that numberor rungs.
        climbing_patterns_count(1)
            returns 1
        climbing_patterns_count(2)
            returns 2 (because Ashwany can take two single steps or one double step up a two-rung ladder)
        climbing_patterns_count(3)
            returns 4 (three single steps, a double and a single, a single and a double, or all three at once)
        climbing_patterns_count(4)
            returns 7 (and you get to confirm that for yourself!)
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return climbing_patterns_count((n-1)) + climbing_patterns_count(n-2) + climbing_patterns_count(n-3)
    

if __name__ == "__main__":
    # Function 1
    pair1 = []
    pair2 = [-5]
    pair3 = [-5,-1]
    pair4 = [-5,-5]
    pair5 = [0,1,0,1,1,0,0]
    print("\nFunction 1:")
    print("Pair 1: ", split_int_pairs(pair1))
    print("Pair 2: ", split_int_pairs(pair2))
    print("Pair 3: ", split_int_pairs(pair3))
    print("Pair 4: ", split_int_pairs(pair4))
    print("Pair 5: ", split_int_pairs(pair5))

    # Function 2
    string1 = ""
    string2 = "aA"
    string3 = "aAa"
    string4 = "bAbA"
    string5 = "BcBcBc"
    print("\nFunction 2:")
    print("String 1: ", count_split_char_pairs(string1))
    print("String 2: ", count_split_char_pairs(string2))
    print("String 3: ", count_split_char_pairs(string3))
    print("String 4: ", count_split_char_pairs(string4))
    print("String 5: ", count_split_char_pairs(string5))

    # Function 3
    square1 = ""
    square2 = "["
    square3 = "[]"
    square4 = "[]]"
    square5 = "[[]]"
    square6 = "[[[[[[[[[]]]]]]]]]"
    print("\nFunction 3:")
    print("String 1: ", check_nesting(square1))
    print("String 2: ", check_nesting(square2))
    print("String 3: ", check_nesting(square3))
    print("String 4: ", check_nesting(square4))
    print("String 5: ", check_nesting(square5))
    print("String 6: ", check_nesting(square6))

    # Function 4
    list1 = []
    list2 = [3]
    list3 = [3, 5]
    list4 = [3, 5, 6]
    list5 = [3, 6]
    list6 = [7, 8, 16, 15, 3, 22]
    list7 = [7, 8, 16, 14, 28, 22]
    print("\nFunction 4:")
    print("List 1: ", find_double(list1))
    print("List 2: ", find_double(list2))
    print("List 3: ", find_double(list3))
    print("List 4: ", find_double(list4))
    print("List 5: ", find_double(list5))
    print("List 6: ", find_double(list6))
    print("List 7: ", find_double(list7))

    # Function 5
    pattern1 = 1
    pattern2 = 2
    pattern3 = 3
    pattern4 = 4
    print("\nFunction 5:")
    print("Pattern 1: ", climbing_patterns_count(pattern1))
    print("Pattern 2: ", climbing_patterns_count(pattern2))
    print("Pattern 3: ", climbing_patterns_count(pattern3))
    print("Pattern 4: ", climbing_patterns_count(pattern4))