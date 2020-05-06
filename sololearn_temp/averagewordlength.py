#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Average Word Length"""

import math

sentence = input('Please type a sentence: ')
letters = 0
words = 0

common_symbols = ('.', '?', '!', ',', ':', ';')
for symbol in common_symbols:
    sentence = sentence.replace(symbol, '')

for word in sentence.split():
    letters = letters + len(word)
    words = words + 1

average = math.ceil(letters / words)

print(average)
