#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Write a function that prints a dictionary by ordered keys."""

    for key in sorted(a_dictionary):
        print(key + ":", a_dictionary[key])
