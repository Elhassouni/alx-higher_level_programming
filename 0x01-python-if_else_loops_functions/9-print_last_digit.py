#!/usr/bin/python3
def print_last_digit(number):
    num_1 = abs(number) % 10
    print("{}".format(num_1), end='')
    return num_1
