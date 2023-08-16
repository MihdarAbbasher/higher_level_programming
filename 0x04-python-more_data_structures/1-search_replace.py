#!/usr/bin/python3
def search_replace(my_list, search, replace):
    li = []
    for x in range(len(my_list)):
        if search == my_list[x]:
            li.append(replace)
        else:
            li.append(my_list[x])
    return li
