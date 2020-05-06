#!/usr/bin/env python3
""" PyNet Lesson 1, Exercise 4
Create a show_version variable that contains the following

  show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "


Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
"""

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()

model_string, serial_number = show_version.split()[1:3]

print('Model contains "Cisco" : {}'.format('cisco' in model_string.lower()))
print('Model contains "881"   : {}'.format('881' in model_string.lower()))
print()
print('Serial :', serial_number)
print('Model  :', model_string)