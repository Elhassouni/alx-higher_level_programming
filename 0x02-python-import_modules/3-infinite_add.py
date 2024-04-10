#!/usr/bin/python3
import sys
result = 0
for i in sys.argv[1:]:
    num_arguments = len(sys.argv)
    if num_arguments == 1:
        print(f"{0}")
    else:
        result += int(i)
if result != 0:
    print("{}".format(result))
