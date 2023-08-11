#!/usr/bin/python3
if __name__ == "__main__":
    """Print the args"""

    import sys

    args_no = len(sys.argv) - 1
    if (args_no == 0):
        print("0 arguments.")
    elif (args_no == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(args_no))
    for i in range(1, args_no + 1):
        print("{}: {}".format(i, sys.argv[i]))
