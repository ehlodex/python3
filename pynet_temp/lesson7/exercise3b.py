#!/usr/bin/env python3
""" Lesson 7, Exercise 3b
Expand the data structure defined earlier in exercise3a. This time you should
have an 'interfaces' key that refers to a dictionary.

Use Python to read in this YAML data structure and print this to the screen.

The output of your Python script should look as follows (in other words, your
YAML data structure should yield the following when read by Python). You YAML
data structure should be written in expanded YAML format.

{'interfaces': {
    'Ethernet1': {'mode': 'access', 'vlan': 10},
    'Ethernet2': {'mode': 'access', 'vlan': 20},
    'Ethernet3': {'mode': 'trunk',
                  'native_vlan': 1,
                  'trunk_vlans': 'all'}
    }
}
"""

import pathlib
import yaml
from pprint import pprint

root_path = pathlib.Path(__file__).resolve().parent
yaml_path = pathlib.Path(f'{root_path}/exercise3b.yaml')

with open(yaml_path) as f:
    yaml_file = yaml.safe_load(f)

pprint(yaml_file)