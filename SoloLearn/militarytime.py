#!/usr/bin/env python3
"""SoloLearn > Code Coach > Military Time"""

from datetime import datetime

def convert_time(civ_time):
    hhmm, ampm = civ_time.split(' ')
    pm = True if ampm[0].lower() == 'p' else False
    hh, mm = hhmm.split(':')
    # The time is 'PM', but not 12:xx PM
    if pm and int(hh) != 12:
        hh = int(hh) + 12
    # The time is '12:xx' AM
    if not pm and int(hh) == 12:
        hh = '00'
    # The time is between '1:00 AM' and '9:59 AM'
    if int(hh) < 10 and len(hh) < 2:
        hh = '0' + str(hh)
    mil_time = '{}:{}'.format(hh, mm)
    return mil_time

now = datetime.now().strftime('%I:%M %p')
my_prompt = 'Enter a civilian time like "hh:mm AM/PM" [{}] '.format(now)
print(convert_time(input(my_prompt) or now))
