#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """delete key in a dictionary if exist"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
