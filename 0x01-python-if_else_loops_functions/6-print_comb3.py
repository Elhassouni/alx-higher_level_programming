#!/usr/bin/python3
for i in range(0, 10):
    for x in range(i + 1, 10):
        print("{}".format(i), end='')
        if i == 8 and x == 9:
            print("{:d}".format(x))
        else:
            print("{:d}".format(x), end=', ')
