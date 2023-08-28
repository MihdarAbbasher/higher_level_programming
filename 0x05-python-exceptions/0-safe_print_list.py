#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ safe_print_list.

    Args:
    list

    Return:
    count
    """
    try:
        i = 0
        while(i < x):
            print(my_list[i], end="")
            i += 1
        print()
    except(IndexError):
        print()
    return(i)
