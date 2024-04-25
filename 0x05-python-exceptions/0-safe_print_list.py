#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Write a function that prints x elements of a list."""
    result = 0
    try:
        for v in my_list:
            result += 1
        if x >= result:
            for key in my_list:
                print(f'{key}', end='')
            print()
            return result
        elif x < result or x == 0:
            _sum = 0
            for value in range(x):
                print(f'{my_list[value]}', end='')
                _sum += 1
            print()
            return _sum
        print()
    except (ValueError, IndexError, TypeError):
        print("x is zero Enter bigger number and list is empty")
