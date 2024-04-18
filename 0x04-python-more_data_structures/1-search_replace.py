#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Write a function that replaces all occurrences of an element by another
        in a new list."""

    new_list = [replace if search == x else x for x in my_list]

    return new_list
