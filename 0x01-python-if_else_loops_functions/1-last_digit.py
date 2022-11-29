#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(number)
i=number%10
if i>5:
    print("Last digit of",number,"is",number%10,"and is greater than 5\n")
elif i==0:
    print("Last digit of",number,"is",number%10,"and is 0\n")
else:
    print("Last digit of",number,"is",number%10,"and is less than 6 and not 0")
