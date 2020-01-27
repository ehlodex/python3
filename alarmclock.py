#!/usr/bin/env python3

import os
import time
from datetime import datetime
from playsound import playsound

# TODO: Allow custom alarm paths
# TODO: Configure alarm_repeat a la cron
# TODO: Create an alarm object
# TODO: Optimize alarm wait times, i.e. time.sleep()
# TODO: Construct the pseudocode
# TODO: Write the actual code

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
alarm_list = [
    {'alarm_time': '16:00', 'alarm_snooze': '5', 'alarm_active': True,
     'alarm_sound': 'exit_sound',
     'alarm_name': 'Sample Alarm 1'},
    {'alarm_time': '08:00', 'alarm_snooze': '9', 'alarm_active': True,
     'alarm_sound': 'startup_sound',
     'alarm_name': 'Sample Alarm 2'},
    {'alarm_time': '13:32', 'alarm_snooze': '9', 'alarm_active': True,
     'alarm_sound': r'C:\Users\Username\Music\Artist\Album\Song.mp3',
     'alarm_name': 'Sample Alarm 3'}
]


def main():
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        for i, alarm in enumerate(alarm_list):
            how_soon = alarm['alarm_time'] + ":00"
            # calculate time delta
            # If the delta is smaller, change the delta
            if how_soon == now:
                print('The alarm \'{}\' is active!'.format(alarm['alarm_name']))
                alarm_sound = get_alarm_sound(alarm['alarm_sound'])
                print('Playing the sound file at {}'.format(alarm_sound))
                try:
                    playsound(alarm_sound)
                except:
                    print('Cannot play any sounds! *beep* *beep* *beep*')
                finally:
                    # write the name and time of the next alarm, based on delta
                    pass
                # If snooze != 0, then prompt to snooze or cancel, presume that
                # the user wants to snooze after 1 minute of inactivity.
                exit()
        time.sleep(1)


def set_alarm(alarm_name, alarm_time, alarm_snooze, alarm_sound):
    # create a new alarm
    # add the alarm to alarm_list
    pass


def ui_set_alarm():
    # prompt for alarm values
    # set_alarm(*args)
    pass


def delete_alarm(alarm_id):
    # if alarm_id is a string:
    #     enumerate through alarm_list to find a match
    #     set alarm_id to a number
    # if alarm_id is a number:
    #     remove it from the alarm_list
    # else:
    #     The alarm cannot be found
    #     Print a list of available alarms
    pass


def ui_delete_alarm():
    # print a list of alarm_name, alarm_time, alarm_repeat
    # alarm_id = input('Which alarm would you like to delete? ')
    # delete_alarm(alarm_id)
    pass


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
    main()
