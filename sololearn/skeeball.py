#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Skee-ball"""

my_points = int(input('How many points do you have? '))
need_tickets = int(input('How many tickets do you need? '))

# 1 ticket = 12 points
my_tickets = int(my_points // 12)

if my_tickets >= need_ticekts:
    print('Buy it!')
else:
    print('Try again')
    
# print('Buy it!' if my_tickets >= need_tickets else 'Try again')
