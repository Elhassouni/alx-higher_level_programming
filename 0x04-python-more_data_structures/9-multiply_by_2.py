#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Write a function that returns a new dictionary with
        all values multiplied by 2"""
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict
