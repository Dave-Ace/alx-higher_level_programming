#!/usr/bin/python3
for i in range(65, 123):
    if chr(i) != 'p'and chr(i) != 'e':
        print("{:c}".format(chr(i)), end='')
