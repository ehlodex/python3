#!/usr/bin/env python3
"""
Example: Keep track of class instances
""" 

class MyClass:
    instances = []

    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.instances.append(self)


# You can create an instance without saving it to a variable...
MyClass('An Instance', 'Created without variable assignment')

# ...or you can save it for direct access later
saved_instance = MyClass('Another Instance', 'Saved to variable')

for instance in MyClass.instances:
    print(f'{instance.name} ... {instance.data}')