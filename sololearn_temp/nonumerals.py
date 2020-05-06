#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > No Numerals"""

sentence = input()

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
           'eight', 'nine', 'ten')

for number in range(10, 0, -1):
    sentence = sentence.replace(str(number), numbers[number])

print(sentence)
