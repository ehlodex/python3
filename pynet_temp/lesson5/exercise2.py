#!/usr/bin/env python3
""" PyNet Lesson 5, Exercise 2
Create a function that randomly generates an IP address for a network.
The default base network should be '10.10.10.0/24'.

You should be able to pass a different base network into your function as an
argument.

Randomly pick a number between 1 and 254 for the last octet and return the
full IP address.

You can use the following to randomly generate the last octet:

Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.

For each function call print the returned IP address to the screen.
"""

import random


def netgen(net_prefix='10.10.10'):
    octet4 = random.randint(1, 254)
    print('{}.{}'.format(net_prefix, octet4))
    print('-' * 20)


netgen()
netgen('172.16.32')
netgen(net_prefix='192.168.144')
