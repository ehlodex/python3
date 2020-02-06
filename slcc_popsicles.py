#!/usr/bin/env python3
""""SoloLearn > Code Coach > Popsicles"""

siblings = int(input('siblings: '))
popsicles = int(input('popsicles: '))

leftovers = popsicles % siblings

if leftovers:
    print('eat them yourself')
else:
    print('give away')
