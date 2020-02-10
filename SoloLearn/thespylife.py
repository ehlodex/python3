#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > The Spy Life"""

import re

message = str(input())[::-1]

letters = re.compile('[^a-zA-Z ]')
print(letters.sub('', message))
