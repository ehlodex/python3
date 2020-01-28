#!/usr/bin/env python3

import os
import threading
import time
from datetime import datetime
from playsound import playsound

# IMPORTANT: alarm_repeat is currently unused!

# This will execute each time the script is run or imported. This is not
# necessarily the best option, as it prevents the alarms from being saved. The
# alarms could (optionally) be saved into a separate file on the local disk for
# preservation, or stored in a database (overkill). For now, starting with an
# empty list, or a default list, is good enough for a rudimentary system.
alarm_path = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(alarm_path, 'Sounds')
sound_exts = ('.mp3', '.wav')
default_alarm_time = '06:00'
default_alarm_snooze = int(9)
default_alarm_sound = os.path.join(sound_path, 'default.mp3')
default_alarm_name = 'Alarm'
default_alarm_repeat = '0 0 * * *'
alarm_list = []


def main():
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        for alarm in alarm_list:
            how_soon = alarm['alarm_time'] + ":00"
            # calculate time delta
            # If the delta is smaller, change the delta
            if how_soon == now:
                # TODO: Thread the alarm sound
                print(r'The alarm "{}" is active!'.format(alarm['alarm_name']))
                alarm_sound = get_alarm_sound(alarm['alarm_sound'])
                print('Playing the sound file at {}'.format(alarm_sound))
                try:
                    playsound(alarm_sound)
                except:
                    print('Cannot play any sounds! *beep* *beep* *beep*')
                finally:
                    # TODO: write the name and time of the next alarm
                    pass
                # TODO: Configure snooze function
                # If snooze != '', then prompt the user to snooze or cancel the
                # current alarm. Presume that the user wants to snooze after 45
                # seconds of inactivity. This will prevent collision of alarms
                # that are 1 minute apart.
        time.sleep(1)


def set_alarm(alarm_time, alarm_snooze, alarm_sound, alarm_name, alarm_repeat):
    # TODO: Check for time collision; we only want one alarm per time
    # TODO: Move error-correction and default values here from ui_
    alarm_list.append({'alarm_time': alarm_time, 'alarm_snooze': alarm_snooze,
                       'alarm_sound': alarm_sound, 'alarm_name': alarm_name,
                       'alarm_repeat': alarm_repeat, 'alarm_enabled': True})


def ui_set_alarm():
    # TODO: Move error-correction and default values out of the ui_
    # A curse upon you, PEP 8, for an absurdly short 'maximum' line length!
    alarm_time = \
        input('What time shall the alarm be sounded? [{}] '
              .format(default_alarm_time)) or default_alarm_time
    alarm_snooze = \
        input('How long (in minutes) should the alarm snooze? [{}] '
              .format(default_alarm_snooze)) or default_alarm_snooze
    alarm_sound = \
        input('Path or name for the alarm sound [{}] '
              .format(default_alarm_sound)) or default_alarm_sound
    alarm_name = \
        input('What is the name of this alarm? [{}] '
              .format(default_alarm_name)) or default_alarm_name
    alarm_repeat = \
        input('How often, if ever, should the alarm be repeated? [{}] '
              .format(default_alarm_repeat)) or default_alarm_repeat
    set_alarm(alarm_time, alarm_snooze, alarm_sound, alarm_name, alarm_repeat)


def delete_alarm(alarm_id):
    alarm_dict = None
    for i, alarm in enumerate(alarm_list):
        if alarm_id == alarm['alarm_name'] or alarm_id == str(i):
            print('matched alarm {}'.format(i))
            alarm_dict = alarm
    try:
        alarm_list.remove(alarm_dict)
        print(r'Deleted alarm "{}"'.format(alarm_dict['alarm_name']))
        print(alarm_dict)
    except ValueError:
        print('no match for {}'.format(alarm_id))



def ui_delete_alarm():
    print(' ID  Time   Name')
    for i, alarm in enumerate(alarm_list):
        print('{:>3}  {:>5}  {}'
              .format(i, alarm['alarm_time'], alarm['alarm_name']))
    alarm_id = str(input('\nWhich alarm would you like to delete? '))
    delete_alarm(alarm_id)


def get_alarm_sound(alarm_sound):
    # assert os.path.isfile(globals()['default_alarm_sound'])
    if os.path.isfile(alarm_sound): return alarm_sound
    this_alarm = os.path.join(globals()['sound_path'], alarm_sound)
    if os.path.isfile(this_alarm): return this_alarm
    for ext in globals()['sound_exts']:
        this_alarm_with_ext = this_alarm + '.' + ext
        if os.path.isfile(this_alarm_with_ext): return this_alarm_with_ext
    return globals()['default_alarm_sound']


if __name__ == '__main__':
    # TODO: start the clock in the background
    # TODO: present a user menu
    # anything below here is for testing
    set_alarm('17:00', '5', 'exit_sound.mp3', 'Go Home', '* * *')
    set_alarm('09:00', '5', 'startup_sounds', 'Working', '* * *')
    set_alarm('09:00', '9', default_alarm_sound, 'Sample Alarm', '')
    ui_delete_alarm()
