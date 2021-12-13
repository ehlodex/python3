#!/usr/bin/env python3
"""Convert DDLC *.chr files

This is for K, if she ever gets to the best ending :)

Copy the 'characters' folder here before running the script.
"""

# __all__ = []
# __version__ = '0.1'
# __author__ = 'ehlodex'

# -- IMPORTS ---------------------------------------------------------->
import base64
from pathlib import Path
from PIL import Image  # python3 -m pip install --upgrade pillow

# -- GLOBALS / CONSTANTS ---------------------------------------------->
script_path = Path(__file__).resolve().parent
literature_club = ['monika', 'natsuki', 'sayori', 'yuri']  # alphabetical
characters_path = Path(script_path/"characters")  # use local copies


# -- FUNCTIONS -------------------------------------------------------->
def main():

    # roll call
    for member in literature_club:
        if not Path(characters_path/member).with_suffix(".chr").is_file():
            print(f'Oh, no! {member} is missing from the Literature Club!')
            literature_club.remove(member)
    
    if ('monika' in literature_club): decypher_monika()
    if ('natsuki' in literature_club): decypher_natsuki()
    if ('sayori' in literature_club): decypher_sayori()
    if ('yuri' in literature_club): decypher_yuri()

#TODO: Add switches for specific characters, but default to all
#      e.g. './ddlc.py --all' would be the same as './ddlc.py', but you
#      can also choose a specific member like './ddlc.py --monika'
#TODO: If only one character is selected, open the file after decyphering
#TODO: Add an --interactive (-i) option that displays a menu of available
#      members, and which members have already been decyphered


def decypher_monika():
    # Monika is PNG image
    i = Path(characters_path/"monika.chr")
    o = Path(script_path/"monika.png")
    o.write_bytes(i.read_bytes())  # copy and rename without shutil
    
    # ... that contains binary code in the form of black and white pixels ...
    im = Image.open(o, 'r')
    width, height = im.size
    pixels = list(im.getdata())
    binary = ''
    for y in range (330,470):
        for x in range (330,470):
            pixel = '1' if pixels[width*y+x] == (255,255,255) else '0'
            binary = binary + pixel
    monika_data = int(binary, 2).to_bytes(len(binary) // 8, byteorder='big')
    
    # ... which is actually Base64 decoded text file.
    o = Path(script_path/"monika.txt")
    monika_text = base64.b64decode(monika_data).decode('utf-8')
    monika_file = open(o, 'w', encoding='utf-8')
    monika_file.write(monika_text)
    monika_file.close()


def decypher_natsuki():
    # Natsuki is a JFIF image.
    i = Path(characters_path/"natsuki.chr")
    o = Path(script_path/"natsuki.jfif")
    o.write_bytes(i.read_bytes())  # copy and rename without shutil


def decypher_sayori():
    # Sayori is an OGG audio clip.
    i = Path(characters_path/"sayori.chr")
    o = Path(script_path/"sayori.ogg")
    o.write_bytes(i.read_bytes())  # copy and rename without shutil


def decypher_yuri():
    # Yuri is a Base64 decoded text file.
    i = Path(characters_path/"yuri.chr")
    o = Path(script_path/"yuri.txt")
    yuri_data = open(i, 'r').read()
    yuri_text = base64.b64decode(yuri_data).decode('utf-8')
    yuri_file = open(o, 'w', encoding='utf-8')
    yuri_file.write(yuri_text)
    yuri_file.close()
    # This code variation is more compact, but harder to read
    # i = base64.b64decode(open(Path(characters_path/"yuri.chr"), 'r').read())
    # o = open(Path(characters_path/"yuri.txt"), 'w')
    # o.write(i)
    # o.close()


# -- __main__ --------------------------------------------------------->
if __name__ == '__main__':
    main()

