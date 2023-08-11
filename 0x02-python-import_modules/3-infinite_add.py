#!/usr/bin/python3
if __name__ == "__main__":
    """Print the args"""

    import sys

    res = 0

    args_no = len(sys.argv)
    for i in range(1, args_no):
        res += int(sys.argv[i])
    print("{}".format(res))
