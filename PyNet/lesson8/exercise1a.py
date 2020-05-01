#!/usr/bin/env python3
""" PyNet Lesson 8, Exercise 1a
Import the 'datetime' library. Print out the module that is being
imported by datetime (the __file__ attribute)

Import the Python ipaddress library. Print out the module that is being
imported by ipaddress (the __file__ attribute). If you are using Python
2.7, you will need to pip install the ipaddress library.

Import sys and use pprint to pprint sys.path
"""

import datetime
import ipaddress
from pprint import pprint
import sys

print(f'datetime imported from  : {datetime.__file__}')
print(f'ipaddress imported from : {ipaddress.__file__}')
print('pprint sys.path         :')
pprint(sys.path)