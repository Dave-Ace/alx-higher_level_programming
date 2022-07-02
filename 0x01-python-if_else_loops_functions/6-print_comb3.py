#!/usr/bin/python3
for i in range(0, 9):
    for x in range(i+1, 10):
        if i == 9:
            print("\n")
        else:
            print("{}".format(i))
            print("{}".format(x), end=', ')
