#!/usr/bin/python3

def best_score(a_dictionary):
    """Write a function that returns a key with the biggest integer value."""

    if a_dictionary is None:
        return None
    else:
        max_value = max(a_dictionary, key=lambda value: a_dictionary[value])
        return max_value
