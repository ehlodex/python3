#!/usr/bin/env python3
"""SoloLearn > Code Coach > Halloween Candy"""

import math

houses = int(input('houses: '))
chance = lambda x : math.ceil((2 / x) * 100)

print((chance(houses)))
