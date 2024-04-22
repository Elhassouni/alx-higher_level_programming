#!/usr/bin/python3

def best_score(a_dictionary):

    """Write a function that returns a key with the biggest integer value."""

    if a_dictionary is None or not a_dictionary:
        return None
    else:
        max_value = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == max_value:
                return key
