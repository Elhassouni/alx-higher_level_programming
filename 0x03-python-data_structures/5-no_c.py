#!/usr/bin/python3

def no_c(my_string):
    new_string_list = []
    if my_string == '':
        return ''
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            new_string_list.append(i)
            new_string = ''.join(new_string_list)
    return new_string
