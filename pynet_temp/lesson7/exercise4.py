#!/usr/bin/env python3
""" Lesson 7, Exercise 4
Take the YAML file and corresponding data structure that you defined in
exercise3b.

From this YAML data input source, use Jinja templating to generate the
following configuration output:

interface Ethernet1
  switchport mode access
  switchport access vlan 10
interface Ethernet2
  switchport mode access
  switchport access vlan 20
interface Ethernet3
  switchport mode trunk
  switchport trunk native vlan 1
  switchport trunk allowed vlan all


The following should all be variables in your Jinja template (the names
may be different than below, but they should be variabilized and not be
hard-coded in your template).

interface_name
switchport_mode
access_vlan
native_vlan
trunk_vlans

All your Jinja2 variables should be retrieved from your YAML file. 

This exercise might be challenging.
"""
import jinja2
import pathlib
import yaml
from pprint import pprint

root_path = pathlib.Path(__file__).resolve().parent
yaml_path = pathlib.Path(f'{root_path}/exercise3b.yaml')
jinja_path = pathlib.Path(f'{root_path}/exercise4.jinja')

with open(yaml_path) as f:
    yaml_file = yaml.safe_load(f)

with open(jinja_path) as f:
    jinja_file = f.read()

t = jinja2.Template(jinja_file)
print(t.render(yaml_file))