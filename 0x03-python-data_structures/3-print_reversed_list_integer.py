#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        my_list = []
    else:
        my_list.reverse()
    for item in my_list:
        print("{:d}".format(item))
