#!/usr/bin/python3

def safe_print_integer(value):
    try:
        i = int(value)
        print("{}".format(i))
        return (True)
    except:
        return (False)

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        while(i < x):
            print("{:d}".format(int(my_list[i])), end="")
            i += 1
        print()
    except:
        print()
    finally:
        return (i)

