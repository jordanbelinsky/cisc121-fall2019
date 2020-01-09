def make_list(n, first_val, inc):
    """Returns a list of n values. Element 0 is first_val, and
    subsequent elements increase by inc.
    """
    if n == 0:
        return []
    else:
        return [first_val] + make_list(n-1,first_val + inc, inc)

def main():
    a_list = make_list(5, 0, 10) # [0, 10, 20, 30, 40]
    print(a_list)
##    list_1 = make_list(30, 0, 10) # [0, 10, 20, 30, ..., 290]
##    print('\n'.join(str(e) for e in list_1))
##    list_2 = make_list(10, -1, -2) # [-1, -3, -5, ..., -19]
##    print('\n'.join(str(e) for e in list_2))
##    list_3 = make_list(5, 'cat', 'dog')
##    print('\n'.join(str(e) for e in list_3))

main()
