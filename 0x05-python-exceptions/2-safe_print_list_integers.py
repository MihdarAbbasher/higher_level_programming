#!/usr/bin/python3
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

