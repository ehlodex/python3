#!/urs/bin/env/ python3
""" SoloLearn > Code Coach > Password Validation"""

import re

password = input('Password? ')
nums = re.compile('[0-9]')
chars = re.compile(r'[!@#$%&*]')

num_count = len(nums.findall(password))
char_count = len(chars.findall(password))
password_len = len(password)

if num_count >= 2 and char_count >= 2 and password_len >= 7:
    print('Strong')
else:
    print('Weak')
