#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Write a function that prints x elements of a list."""
    length = 0
    try:
        length = 0
        for value in range(x):
            print(f'{my_list[value]}', end='')
            length += 1
        print()
    except IndexError:
        print()
    finally:
        return length
my_list = [1, 2, 3, 4, 5]
