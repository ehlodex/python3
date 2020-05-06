#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Cheer Creator"""

yards = int(input('How many yards? '))
cheer = ''

if yards < 1:
    cheer = 'shh'
elif yards >= 1 and yards <= 10:
    for yard in range(0,yards):
        cheer = cheer + 'Ra!'
else:
    cheer = 'High Five!'

print(cheer)
