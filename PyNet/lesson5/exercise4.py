#!/usr/bin/env python3
""" PyNet Lesson 4, Exercise 4
Copy your solution from exercise3 to exercise4. Add an 'import pdb' and
pdb.set_trace() statement outside of your function (i.e. where you have your
function calls)..
"""

import pdb
import re
mac_formats = (
    re.compile('^([0-9A-F]{1,2}[:]){5}([0-9A-F]{1,2})$'),
    re.compile('^([0-9A-F]{1,4}[.]){2}([0-9A-F]{1,4})$')
)


def mac_daddy(mac_address):
    mac_address = mac_address.upper()
    mac_address = mac_address.replace('-', ':')
    new_mac = []

    # 00:00:AA:AA:BB:BB
    if re.match(mac_formats[0], mac_address):
        for octet in mac_address.split(':'):
            octet = octet if len(octet) == 2 else octet.zfill(2)
            new_mac.append(octet)

    # 0000.aaaa.bbbb
    elif re.match(mac_formats[1], mac_address):
        for octet in mac_address.split('.'):
            octet = octet if len(octet) == 4 else octet.zfill(4)
            new_mac.append(octet[0:2])
            new_mac.append(octet[2:4])

    # No match, invalid format
    else:
        raise ValueError("Something doesn't look right...")

    mac_address = ''
    for octet in new_mac:
        mac_address = mac_address + ":" + str(octet)
    print(mac_address[1:])


pdb.set_trace()
mac_daddy('a:b:c:d:e:f')
mac_daddy('123.456.789')
mac_daddy('1a-0-7-e5-aa-f4')
mac_daddy('This is a string')
