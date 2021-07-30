#!/usr/bin/env python3
"""FizzBuzz for Tom Scott"""

# __all__ = []
# __version__ = '0.1'
# __author__ = 'ehlodex'

# -- GLOBALS / CONSTANTS ---------------------------------------------->
fizzbuzz_limit = 100

for i in range(1,fizzbuzz_limit+1):
    say = ""
    if (i % 3 == 0): say = say + "Fizz"  # multiples of 3
    if (i % 5 == 0): say = say + "Buzz"  # multiples of 5
    if (say == ""): say = i
    print(say)
