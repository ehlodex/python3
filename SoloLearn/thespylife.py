/usr/bin/env/ python3
"""SoloLearn > Code Coach > The Spy Life"""

import re

message = input()[::-1]

letters = re.compile('[^a-zA-Z]')
print(letter.sub('', message)
