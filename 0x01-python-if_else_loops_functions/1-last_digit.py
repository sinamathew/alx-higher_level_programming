#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) % 10

if (number < 0):
    last_num == -last_num

msg = "Last digit of {} is {} and is ".format(number, last_num)

if last_num > 5:
    print("{}greater than 5".format(msg))
elif last_num == 0:
    print("{}0".format(msg))
else:
    print("{}less than 6 and not 0".format(msg))
