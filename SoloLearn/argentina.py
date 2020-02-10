#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Argentina"""

pesos = int(input('List price in pesos: '))
cents = int(input('List price in dollars: ')) * 100

# 2 cents / 1 peso
pesos = pesos * 2

if pesos > cents:
    print('Dollars')
else:
    print('Pesos')
