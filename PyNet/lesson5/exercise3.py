#!/usr/bin/env python3
""" PyNet Lesson 5, Exercise 3
Similar to lesson3, exercise4 write a function that normalizes a MAC
address to the following format: 01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion. It
should also handle converting '0000.aaaa.bbbb' and '00-00-aa-aa-bb-bb'.

The function should have one parameter, the mac_address.
It should return the normalized MAC address

Single digit bytes should be zero-padded to two digits.
In other words, this: a:b:c:d:e:f should be converted to: 0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.
"""

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


mac_daddy('a:b:c:d:e:f')
mac_daddy('123.456.789')
mac_daddy('1a-0-7-e5-aa-f4')
mac_daddy('This is a string')
