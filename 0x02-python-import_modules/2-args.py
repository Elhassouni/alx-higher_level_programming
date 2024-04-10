#!/usr/bin/python3
import sys

counter = 0
result = len(sys.argv)
if result == 1:
    print(f"{0} argument.")
elif result == 2:
    print(f"{result - 1} argument:")
else:
    print(f"{result - 1} arguments:")
if __name__ == "__main__":
    for i in sys.argv[1:]:
        counter += 1
        print("{}: {}".format(counter, i))
