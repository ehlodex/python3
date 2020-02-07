#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > New Driver's License"""

import math

your_name = input('Your Name: ')
agents = int(input('Agents: '))
other_names = input('Others: ').replace(',', ' ')
wait_time = 20

names = other_names.split()
names.append(your_name)
names.sort()

position = names.index(your_name) + 1
group = math.ceil(position/agents)

print(group * wait_time)
