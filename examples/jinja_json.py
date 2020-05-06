#!/usr/bin/env python3
"""
Example: Jinja Templating from JSON
"""

import json

from jinja2 import Template
from pathlib import Path

## -- Resolve Local Path (Assume It's Not in PYTHONPATH) -------------->
script_path = Path(__file__).resolve().parent
json_path = Path(script_path/'example.json')
jinja_path = Path(script_path/'example.jinja')

# -- Load the JSON File ----------------------------------------------->
with open(json_path) as j:
    json_file = json.load(j)

# -- Read the Jinja(2) File ------------------------------------------->
with open(jinja_path) as j:
    jinja_file = j.read()

jinja_template = Template(jinja_file)

## -- Render the Jinja(2) File Using Variables From JSON -------------->
print(jinja_template.render(json_file))
print()