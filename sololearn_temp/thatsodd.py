#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > That's odd..."""

quantity = int(input('How many numbers? '))
sum = int(0)

for i in range(0, quantity):
    number = int(input('Please type a number: '))
    if number % 2 == 0:
        sum = sum + number

print(sum)
