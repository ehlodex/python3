#!/usr/bin/env python3
"""SoloLearn > Code Coach > Pig Latin"""

english = input('Enter a phrase without punctuation: ').lower()
piglatin = ''

# Sanitize the string
common_punctuation = ('.', '?', '!', ',', ';', ':')
for punctuation in common_punctuation:
    english = english.replace(punctuation, '')

# igpay atinlay
for word in english.split():
    wordlen = len(word)
    word = word[1:wordlen] + word[0] + 'ay'
    piglatin = piglatin + word + ' '

print(piglatin.strip())
