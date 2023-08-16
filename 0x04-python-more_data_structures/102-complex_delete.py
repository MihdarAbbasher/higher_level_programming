#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for curr_key in list_keys:
        if value == a_dictionary[curr_key]:
            del a_dictionary[curr_key]

    return (a_dictionary)
