#!/usr/bin/python3
def safe_print_division(a, b):
    """Write a function that divides 2 integers and prints the result."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
