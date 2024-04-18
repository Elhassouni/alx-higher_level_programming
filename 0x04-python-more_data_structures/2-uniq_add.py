#!/usr/bin/python3

def uniq_add(my_list=[]):

    """Write a function that adds all unique integers in a list
    (only once for each integer)."""

    # res = [my_list[i] for i in range(len(my_list)) if i ==
    # my_list.index(my_list[i])] This alternative of for loop removes
    # diplucates

    new_list = []
    for item in range(len(my_list)):
        if item == my_list.index(my_list[item]):
            new_list.append(my_list[item])
    result = sum(new_list)

    return result
