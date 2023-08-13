#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace list item at index"""
    l = len(my_list)
    if idx >= l or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list
