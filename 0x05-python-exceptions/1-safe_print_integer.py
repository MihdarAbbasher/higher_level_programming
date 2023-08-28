#!/usr/bin/python3

def safe_print_integer(value):
    try:
        i = int(value)
        print("{:d}".format(int(i)))
        return (True)
    except:
        return (False)
