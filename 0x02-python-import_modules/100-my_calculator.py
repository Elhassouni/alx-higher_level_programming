#!/usr/bin/python3
from calculator_1 import add, div, mul, sub
import sys

result = 0

arg_num = len(sys.argv)
if arg_num != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if arg_num == 4:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    signs = sys.argv[2]
elif (sys.argv[2] != '+' or sys.argv[2] != '-' or
      sys.argv[2] != '/' or sys.argv[2] != '*'):
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)


def sign(num_1, num_2, signs):

    if signs == '+':
        result = add(num_1, num_2)
        print(f"{num_1} + {num_2} = {result}")
    elif signs == '-':
        result = sub(num_1, num_2)
        print(f"{num_1} - {num_2} = {result}")
    elif signs == '*':
        result = mul(num_1, num_2)
        print(f"{num_1} * {num_2} = {result}")
    elif signs == '/':
        result = div(num_1, num_2)
        print(f"{num_1} / {num_2} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    sign(a, b, signs)
