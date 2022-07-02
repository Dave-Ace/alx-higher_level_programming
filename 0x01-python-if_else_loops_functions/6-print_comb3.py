#!/usr/bin/python3
for i in range(0, 9):
    for x in range(i+1, 10):
        print("{}".format(i), end='')
        if i+1 == 9:
            print("{}".format(x), end='\n')
        else:
            print("{}".format(x), end=', ')
