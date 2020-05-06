#!/usr/bin/env/ python3
"""SoloLearn > Code Coach > Jungle Camping"""

sounds = input('What sounds did you hear? ')
sounds = list(sounds.split())
sound_dict = {'Grr': 'Lion', 'Rawr': 'Tiger', 'Ssss': 'Snake', 'Chirp': 'Bird'}
animals =''

for sound in sounds:
    animals = animals + sound_dict[sound] + ' '

print(animals.strip())  # remove extra spaces
