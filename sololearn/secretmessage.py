#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Secret Message"""
abc = ' abcdefghijklmnopqrstuvwxyz '
zyx = abc[::-1]

message = input('Please type a message: ').lower()
secret = ''

for word in message.split():
    drow = ''
    for letter in word:
        drow = drow + zyx[abc.index(letter)]
    secret = secret + drow + ' '

print(secret.strip())
