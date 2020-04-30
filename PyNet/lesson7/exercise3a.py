#!/usr/bin/env python3
""" PyNet Lesson 7, Exercise 3a
Create a YAML file that defines a list of interface names.
Use the expanded form of YAML.

Use a Python script to read in this YAML list and print it to the screen.

The output of your Python script should be:

['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4', 'Ethernet5',
'Ethernet6', 'Ethernet7', 'Management1', 'Vlan1']
"""

import pathlib
import yaml

root_path = pathlib.Path(__file__).resolve().parent
yaml_path = pathlib.Path(f'{root_path}/exercise3a.yaml')

with open(yaml_path) as f:
    yaml_file = yaml.full_load(f)

print(yaml_file)