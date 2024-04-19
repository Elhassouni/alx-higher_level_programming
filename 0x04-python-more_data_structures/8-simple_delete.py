#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):

    """Write a function that deletes a key in a dictionary."""

    if key in a_dictionary:
        a_dictionary.pop(key, None)
    return a_dictionary
