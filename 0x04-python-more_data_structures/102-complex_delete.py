#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Write a function that prints a dictionary by ordered keys."""

    new_key_dict = []
    for key, values in a_dictionary.items():
        if values == value:
            new_key_dict.append(key)

    for keys in new_key_dict:
        del a_dictionary[keys]
    return a_dictionary
