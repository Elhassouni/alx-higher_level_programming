#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = abs(number) % 10
if last_digit != 0 and number < 0:
    to_negative_num = -last_digit
    print("Last digit of {} is {} and is less than 6 and not 0".format
          (number, to_negative_num))
elif last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,
          last_digit))

elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))

elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, last_digit))
