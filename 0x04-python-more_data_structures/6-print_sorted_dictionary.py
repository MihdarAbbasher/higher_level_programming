#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    def smallest(li):
        res = li[0]
        for x in li:
            if x < res:
                res = x
        return res
    for i in range(len(a_dictionary)):
        curr = smallest(list(a_dictionary))
        print("{}: {}".format(curr, a_dictionary.get(curr)))
        a_dictionary.pop(curr)
        
