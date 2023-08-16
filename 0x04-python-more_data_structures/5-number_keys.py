#!/usr/bin/python3
def number_keys(a_dictionary):
    res = 0
    li = []
    for k in a_dictionary:
        if k not in li:
            li.append(k)
            res += 1
    return res
