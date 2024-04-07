#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for alpha in str:
        unicode = ord(alpha)
        if unicode >= ord('a') and unicode <= ord('z'):
            unicode -= 32
            upper_str += chr(unicode)
        else:
            upper_str += chr(unicode)
    print(upper_str)
