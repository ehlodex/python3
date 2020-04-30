#!/usr/bin/env python3
"""os.path -vs- pathlib"""

import os
import pathlib

# Get the home directory of the current user # ------------------------>

## os.path
o_home_path = os.path.expanduser("~")

## pathlib.Path
p_home_path = pathlib.Path.home()


# Get the script path # ----------------------------------------------->

## os.path
o_script_path = os.path.dirname(os.path.abspath(__file__))

if o_home_path == o_script_path:
    print('os.path is working from home!')
else:
    print(f'os.path is working in {o_script_path}')

## pathlib
p_script_path = pathlib.Path(__file__).resolve().parent

if o_home_path == p_script_path:
    print('pathlib is working from home')
else:
    print(f'pathlib is working from {p_script_path}')


# Append information to an existing path # ---------------------------->

## os.path
o_music_path = os.path.join(o_home_path, 'Music')

## pathlib
p_music_path = p_home_path.joinpath('Music')
p_music_path = pathlib.Path(p_home_path/'Music') # works cross-platform!


# Check for existing directory or file # ------------------------------>

##os.path
print(f'Testing {o_music_path} with os.path...')
o_dir = os.path.isdir(o_music_path)
o_file = os.path.isfile(o_music_path)
print(f'dir  : {o_dir}')
print(f'file : {o_file}')

##pathlib
print(f'Testing {p_music_path} with pathlib...')
p_dir = p_music_path.is_dir()
p_file = p_music_path.is_file()
print(f'dir  : {p_dir}')
print(f'file : {p_file}')
