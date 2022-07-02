#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c_str = ord(i)
        if (ord(i) < 97) or (ord(i) > 122):
            u_str = chr(ord(i))
        else:
            u_str = chr(ord(i) - 32)
        print("{:s}".format(u_str), end='')
    print("\n")
