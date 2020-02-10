#!/usr/bin/env/ python3

import os

# Set a fixed, absolute path based on the Operating System
if os.name == 'nt':  # aka Microsoft Windows
    fixed_path = r'C:\Users\Public\Music'
else:
    fixed_path = r'/home/share/Music'

# Look for the 'Sounds' sub-directory wherever this script is located
script_path = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(script_path, 'Sounds')


def test_path(path):
    try:
        assert os.path.isdir(path)
        print('Using path: {}'.format(path))
    except AssertionError:
        print('Path Error! {}'.format(path))


test_path(fixed_path)
test_path(script_path)
