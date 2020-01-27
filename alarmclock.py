#!/usr/bin/env python3

from datetime import datetime
from time import sleep

# TODO: Configure default path for alarm sounds
# TODO: Allow custom alarm paths
# TODO: Configure alarm_repeats a la cron
# TODO: Create an alarm object
# TODO: Optimize alarm wait times, i.e. sleep()
# TODO: Construct the pseudocode
# TODO: Write the actual code

# This will execute each time the script is run or imported. This is not
# necessarily the best option, as it prevents the alarms from being saved. The
# alarms could (optionally) be saved into a separate file on the local disk for
# preservation, or stored in a database (overkill). For now, starting with an
# empty list, or a default list, is good enough for a rudimentary system.

# The alarm_path should be a 'universal' or default location for alarm sounds.
# Something like os.path.dirname(os.path.abspath(__file__)) could be used.
alarm_path = 'C:\\ProgramData\\PylarmClock\\'
sound_path = alarm_path + 'Sounds\\'
sound_exts = ('.mp3', '.flac')
alarm_list = [
    {'alarm_time': '16:00', 'alarm_snooze': '5', 'alarm_active': True,
     'alarm_sound': 'exit_sound',
     'alarm_name': 'Sample Alarm 1'},
    {'alarm_time': '08:00', 'alarm_snooze': '9', 'alarm_active': True,
     'alarm_sound': 'startup_sound',
     'alarm_name': 'Sample Alarm 2'},
    {'alarm_time': '13:37', 'alarm_snooze': '9', 'alarm_active': True,
     'alarm_sound': 'C:\\Users\\Username\\Music\\Artist\\Album\\Song.mp3',
     'alarm_name': 'Sample Alarm 3'}
]


def main():
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        for i, alarm in enumerate(alarm_list):
            how_soon = alarm['alarm_time'] + ":00"
            if how_soon == now:
                print('The alarm \'{}\' is active!'.format(alarm['alarm_name']))
                alarm_sound = alarm['alarm_sound']
                # test alarm sound path
                #   if it's a full path, use that
                #   else see if it exists in sound_path, with or without exts
                #   else use the default sound
                print('Playing the sound file at {}'.format(alarm_sound))
                # If snooze != 0, then prompt to snooze or cancel, presume that
                # the user wants to snooze after 1 minute of inactivity.
                # exit()
        # Wait half of the time until the next alarm (e.g. if the next alarm
        # sounds in 45 minutes, check the alarms again in 23 minutes). When the
        # alarm will sound in less than 5 minutes, check every minute, until
        # there is < 90 seconds remaining, then check every second.
        sleep(5)

def set_alarm():
    # args = alarm_name, alarm_time, alarm_snooze, alarm_sound
    # set_alarm('Wakeup 1', '05:45', '9', 'destiny.mp3')
    pass


def delete_alarm():
    # args = index_number or alarm_name
    # delete_alarm(1) or delete_alarm('Wakeup 1')
    pass


if __name__ == '__main__':
    main()
