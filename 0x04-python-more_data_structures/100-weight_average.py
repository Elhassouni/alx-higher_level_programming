#!/usr/bin/python3
def weight_average(my_list=[]):
    """Write a function that returns the weighted average
        of all integers tuple (<score>, <weight>)"""

    score = 0
    weight = 0
    if not my_list:
        return 0
    else:
        for s, w in my_list:
            score += s * w
            weight += w
        average = score / weight
        return average
