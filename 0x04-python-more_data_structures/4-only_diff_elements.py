#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    li = []
    for x in set_1:
        if x not in set_2:
            li.append(x)
    for x in set_2:
        if x not in set_1:
            li.append(x)
    return set(li)
