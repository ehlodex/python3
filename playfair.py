#!/usr/bin/env python3
"""Fairplay Cipher
"""

# playfair.py -g 5 -k FAIRPLAY -m 'Hello, World!'
# playfair.py --gridsize 9x9 --keyword 'Mundo' --message 'Hello, World!'

import numpy as np
import string
import argparse

BOGUS_LETTER = 'X'.upper()
UNUSED_LETTER = 'J'.upper()
REPLACEMENT_LETTER = 'I'.upper()
DEFAULT_GRID_SIZE = 5
DEFAULT_KEYWORD = 'Tesla'
DEFAULT_MESSAGE = 'Hello, World!'
NUMBERS = string.digits
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
SYMBOLS = '.@!#%&*-/:=?_ $+,;^'  # list in priority order, not sorted()!

FAIRPLAY_GRID = (
    sorted(UPPERCASE),  # 5x5
    sorted(UPPERCASE + NUMBERS),  # 6x6
    sorted(UPPERCASE + NUMBERS + SYMBOLS[:13]),  # 7x7
    sorted(UPPERCASE + LOWERCASE + NUMBERS + SYMBOLS[:2]),  #8x8
    sorted(UPPERCASE + LOWERCASE + NUMBERS + SYMBOLS[:19])  # 9x9
)


def fairplay_prep(grid_size, oldlist, allow_duplicates=False):
    newlist = []
    for i in oldlist:
        i = i.upper() if grid_size <= 7 else i
        if grid_size == 5 and i == UNUSED_LETTER:
            i = REPLACEMENT_LETTER
        if (i not in newlist or allow_duplicates) and i in list(FAIRPLAY_GRID[grid_size - 5]):
            newlist.append(i)
    return newlist


def fairplay(grid_size=DEFAULT_GRID_SIZE, keyword=DEFAULT_KEYWORD, message=DEFAULT_MESSAGE):
    grid_size = grid_size if grid_size <= len(FAIRPLAY_GRID) + 4 else len(FAIRPLAY_GRID) + 4

    letters = list(FAIRPLAY_GRID[grid_size - 5])
    if grid_size == 5:
        letters.remove(UNUSED_LETTER)
    keyword = fairplay_prep(grid_size, list(keyword))

    # Remove keyword from letters
    for i in keyword:
        if i in letters:
            letters.remove(i)
    grid = np.array(keyword + letters).reshape(grid_size, grid_size)

    # prep message for Fairplay
    message = fairplay_prep(grid_size, list(message), True)

    # check for double letters in pair
    for i in range(0, len(message), 2):
        try:
            if message[i] == message[i+1]:
                message.insert(i+1, BOGUS_LETTER)
        except:
            pass
    
    # Append a training BOGUS_LETTER to make pairs
    if len(message) % 2 != 0:
        message.append(BOGUS_LETTER)

    result = ''
    for i in range(0, len(message), 2):
        a = np.where(grid == message[i])
        b = np.where(grid == message[i+1])
        a, b = (a[0], b[1]), (b[0], a[1])
        result += grid[a][0] + grid[b][0]
    
    for i in range(0, len(result)-3, 1):
        try:
            if result[i] == result[i+2] and result[i+1] == BOGUS_LETTER:
                result = result[:i+1] + result[i+2:]
        except:
            pass

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--gridsize', help='grid size should be between 5 and 9')
    parser.add_argument('-k', '--keyword', help='single keyword')
    parser.add_argument('-m', '--message', help='message to encode/decode')
    args = parser.parse_args()

    if not args.gridsize or not args.keyword or not args.message:
        print('Welcome to Fairplay!\n')
    
    if args.gridsize:
        try:
            grid_size = int(args.gridsize[0])
        except:
            grid_size = DEFAULT_GRID_SIZE
    else:
        grid_size = int(input('Please select a grid size (5-9): ') or DEFAULT_GRID_SIZE)

    if args.keyword:
        try:
            keyword = str(args.keyword)
        except:
            keyword = DEFAULT_KEYWORD
    else:
        keyword = input('Please enter a keyword for encryption and decryption: ') or DEFAULT_KEYWORD

    if args.message:
        try:
            message = str(args.message)
        except:
            message = DEFAULT_MESSAGE
    else:
        message = input('Please type or paste the text below:\n') or DEFAULT_MESSAGE

    print(fairplay(grid_size, keyword, message))

if __name__ == '__main__':
    main()
