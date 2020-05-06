#!/usr/bin/env python3
"""
Example: Jinja Templating From YAML
"""

import yaml

from jinja2 import Template
from pathlib import Path

## -- Resolve Local Path (Assume It's Not in PYTHONPATH) -------------->
script_path = Path(__file__).resolve().parent
yaml_path = Path(script_path/'example.yaml')
jinja_path = Path(script_path/'example.jinja')

# -- Safe Load the YAML File ------------------------------------------>
with open(yaml_path) as y:
    yaml_file = yaml.safe_load(y)

# -- Read the Jinja(2) File ------------------------------------------->
with open(jinja_path) as j:
    jinja_file = j.read()

jinja_template = Template(jinja_file)

## -- Render the Jinja(2) File Using Variables From YAML -------------->
print(jinja_template.render(yaml_file))
print()