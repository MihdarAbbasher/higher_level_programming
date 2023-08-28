#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    print list of int.

    Args:
    list
    x count

    Return:
    count
    """

    i = 0
    count = 0
    while(i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except(IndexError, ValueError):
            pass
        i += 1
    print()
    return (count)
