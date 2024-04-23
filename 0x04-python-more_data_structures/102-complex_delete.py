#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for key, values in list(new_dict.items()):
        if values == value:
            del new_dict[key]
