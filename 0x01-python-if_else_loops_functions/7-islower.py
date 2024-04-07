#!/usr/bin/python3
def islower(c):
    str_1 = ord(c)
    if str_1 >= ord('a') and str_1 <= ord('z'):
        return True
    else:
        return False
