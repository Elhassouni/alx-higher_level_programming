#!/usr/bin/python3

def element_at(my_list, idx):

    length = len(my_list)
    if idx < 0 or (idx == 1 and length == 1):
        return None
    if idx >= length:
        return None
    result = my_list[idx]
    return result
