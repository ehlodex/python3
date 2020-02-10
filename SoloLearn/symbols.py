#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Symbols"""

import re

sentence = input('Please type a sentence with random characters added: ')
letters = re.compile('[^a-zA-Z0-9 ]')
sentence = letters.sub('', sentence)
print(sentence)
