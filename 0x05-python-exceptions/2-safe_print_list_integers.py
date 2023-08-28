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
    while(i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        except(IndexError):
            pass
    print()
    return (i)
