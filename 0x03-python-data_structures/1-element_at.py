#!/usr/bin/python3
def element_at(my_list, idx):
    """get element at index"""
    l = len(my_list)
    if idx >= l or idx < 0:
        return None

    return my_list[idx]
