#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Deja Vu"""

string = input()
unique = True

for letter in string:
    count = string.count(letter)
    if count > 1:
        unique = False
        
if unique:
    print('Unique')
else:
    print('Deja Vu')
