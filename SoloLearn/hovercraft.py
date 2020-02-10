#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Hovercraft"""

sales = int(input('How many did you sell? ')) * 3
expense = 21

if sales > expense:
    print('Profit')
elif sales < expense:
    print('Loss')
else:
    print('Broke Even')
