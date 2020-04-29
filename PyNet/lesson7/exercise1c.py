#!/usr/bin/env python3
""" PyNet Lesson 7, Exercise 1c
Using Jinja2 templating and a for-loop inside the template, generate
the following configuration snippet:

vlan 501
   name blue501
vlan 502
   name blue502
vlan 503
   name blue503
vlan 504
   name blue504
vlan 505
   name blue505
vlan 506
   name blue506
vlan 507
   name blue507
vlan 508
   name blue508

Your template should be inside your Python program for simplicity.

It is fine for your VLAN IDs to be out of order in the generated
configuration (for example, VLAN ID 508 can come before VLAN ID 504).
"""

import jinja2

vlan_vars = {
    'vlans': {
        '501': 'blue501',
        '502': 'blue502',
        '503': 'blue503',
        '504': 'blue504',
        '505': 'blue505',
        '506': 'blue506',
        '507': 'blue507',
        '508': 'blue508',
    }
}

vlan_template = '''
{%- for id, name in vlans.items() %}
vlan {{ id }}
   name {{ name }}
{%- endfor %}
'''

t = jinja2.Template(vlan_template)
print(t.render(vlan_vars))