#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Security"""

floor = input()
floor = floor.replace('x', '')

if '$T' in floor or 'T$' in floor:
    print('ALARM')
else:
    print('quiet')
