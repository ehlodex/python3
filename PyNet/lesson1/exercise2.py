#!/usr/bin/env python3
""" PyNet Lesson 1, Exercise 2
Prompt a user to enter in an IP address from standard input. Read the IP
address in and break it up into its octets. Print out the octets in decimal,
binary, and hex.

Your program output should look like the following:

Please enter an IP address: 80.98.100.240

     Octet1         Octet2         Octet3         Octet4
 ------------------------------------------------------------
       80             98             100            240
    0b1010000      0b1100010      0b1100100     0b11110000
      0x50           0x62           0x64           0xf0
 ------------------------------------------------------------


Four columns, fifteen characters wide, a header column, data centered in the
column.
"""

ip_addr = input('Please enter an IP address: ')
octet = [None]  # offset the list so octet[0] can be ignored
for i in ip_addr.split('.'):
    octet.append(int(i))
col = '{:^15}{:^15}{:^15}{:^15}'
sep = '-' * 60

print(col.format('Octet1', 'Octet2', 'Octet3', 'Octet4'))
print(sep)
print(col.format(octet[1], octet[2], octet[3], octet[4]))
print(col.format(bin(octet[1]), bin(octet[2]), bin(octet[3]), bin(octet[4])))
print(col.format(hex(octet[1]), hex(octet[2]), hex(octet[3]), hex(octet[4])))
print(sep)
