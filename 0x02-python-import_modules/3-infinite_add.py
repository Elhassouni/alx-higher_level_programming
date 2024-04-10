#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    num_arg = len(sys.argv)
    if num_arg == 1:
        print(f"{0}")
    for i in sys.argv[1:]:
        result += int(i)
    if result != 0:
        print("{}".format(result))
