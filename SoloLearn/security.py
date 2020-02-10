#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Security"""

floor = input('Floor plan? Use "x" for empty space. ')
floor = floor.replace('x', '')

if '$T' in floor or 'T$' in floor:
    print('ALARM')
else:
    print('quiet')
