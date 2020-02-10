#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Paint Costs"""

import math

paints = int(input('How many colours? '))
supplies = int(40)

cost = supplies + (paints * 5)
tax = cost * 0.1
total = math.ceil(cost + tax)
# total math.ceil(cost * 1.1)
print(total)
