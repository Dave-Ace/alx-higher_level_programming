#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
print("Last digit of %s is %s and is " % (number, last_digit))
if last_digit > 5:
    print("greater than 5" % (number, last_digit))
elif last_digit == 0:
    print("0" % (number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("less than 6 and not 0" % (number, last_digit))
