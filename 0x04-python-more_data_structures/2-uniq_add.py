#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    li = []
    for x in my_list:
        if x not in li:
            li.append(x)
            sum += x
    return sum
