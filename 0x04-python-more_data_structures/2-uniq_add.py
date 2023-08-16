#!/usr/bin/python3
def uniq_add(my_list=[]):
    li = []
    for x in my_list:
        if x not in li:
            li.append(x)
    return li
