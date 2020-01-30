#!/usr/bin/env python3

from datetime import datetime, timedelta
import time

# This is meant to be an overly-simplified alarm clock.
# Used as a proof-of-concept for a complex alarm system.


def get_dt_object(dt_string):
    alarm_H = int(dt_string.split(':')[0])
    alarm_M = int(dt_string.split(':')[1])
    now = datetime.now()
    later = now.replace(hour=alarm_H, minute=alarm_M, second=0, microsecond=0)
    if later < now:
        later = later + timedelta(days=1)
    return later


def get_dt_string(dt_object):
    return dt_object.strftime('%H:%M:%S')


default_alarm_time = get_dt_string(datetime.now() + timedelta(minutes=5))[:5]
# Convert user input (str) to a datetime object
alarm_time = get_dt_object(
    input('Please set an 24h time like HH:MM [{}] '.format(default_alarm_time))
    or default_alarm_time)
next_alarm = get_dt_string(alarm_time)

while True:
    current_time = get_dt_string(datetime.now())
    print(current_time)
    if current_time == next_alarm:
        print('beep, beep, beep!')
        exit()
    time.sleep(1)
