#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > YouTube Link Finder"""

yt = input()

if '?v=' in yt:
    id = yt.split('=')[1]
else
    id = yt.split('.be/')[1]

print(id)
