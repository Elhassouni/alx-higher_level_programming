#!/usr/bin/python3
for i in range(0, 89):
    flag = False 
    for j in range(10,90,10):
        if i == j:        
            flag = True
            break
        else:
            i + 1
            print("{:02d}".format(i),  end=', ')

