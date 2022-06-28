#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
string = f"Last digit of {number} is {last_digit} and is {}"
if last_digit > 5:
    print(string.format("greater than 5"))
elif last_digit == 0:
    print(string.format("0"))
elif last_digit < 6 and last_digit != 0:
    print(string.format("less than 6 and not 0"))
