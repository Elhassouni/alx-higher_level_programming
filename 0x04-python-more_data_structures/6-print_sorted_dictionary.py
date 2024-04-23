#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Write a function that prints a dictionary by ordered keys."""
    if a_dictionary is None:
        return None
    for key, value in sorted(a_dictionary.items()):
        print(str(key) + ":", value)
