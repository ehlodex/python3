#!/usr/bin/env/ python3
"""Brief description of this file. Wrapped at 72 characters.

PEP8 says that you should always use double-quote marks and end the
docstring with the triple quote on its own line.
"""

# __all__ = []
# __version__ = '0.1'
# __author__ = 'ehlodex'

# IMPORTS
# [from module] import function [as alias]
from pathlib import Path


# GLOBALS / CONSTANTS
script_path = Path(__file__).resolve().parent

# FUNCTIONS
def main():
    pass


# IF NAME MAIN
if __name__ == '__main__':
    main()
