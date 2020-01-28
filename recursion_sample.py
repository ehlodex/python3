#!/usr/bin/env python3

alarm_defaults = {
    'time': {
        'prompt': 'Alarm time (like HH:MM)',
        'default': '06:00'},
    'snooze': {
        'prompt': 'Snooze time (in minutes)',
        'default': int(9)}
}

def set_var(var_name=None):
    if var_name == None:
        alarm_time = set_var('time')
        alarm_snooze = set_var('snooze')
    else:
        try:
            assert alarm_defaults[var_name]
            prompt = alarm_defaults[var_name]['prompt']
            default = alarm_defaults[var_name]['default']
            my_var = input('{} [{}] '.format(prompt, default))
        except KeyError:
            print(r'Whoops! The paramater "{}" does not exist!'.format(var_name))
            my_var = None
        return my_var


if __name__ == '__main__':
    set_var()
