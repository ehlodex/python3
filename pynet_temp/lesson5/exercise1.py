#!/usr/bin/env python3
""" PyNet Lesson 5, Exercise 1
A. Create an ssh_conn function. This function should have three parameters:
ip_addr, username, and password. The function should print out each of these
three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.
Call this ssh_conn function using entirely named arguments.
Call this ssh_conn function using a mix of positional and named arguments.

B. Expand on the ssh_conn function from exercise1 except add a fourth
parameter 'device_type' with a default value of 'cisco_ios'. Print all four
of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying device_type

Create a dictionary that maps to the function's parameters.
Call this ssh_conn2 function using the **kwargs technique.
"""

# 1a
def ssh_conn(ip_addr, username, password):
    print('ip_addr     : {}'.format(ip_addr))
    print('username    : {}'.format(username))
    print('password    : {}'.format(password))
    print('-' * 20)

ssh_conn('192.168.144.10', 'root', 'toortoor')
ssh_conn(ip_addr='192.168.144.10', username='root', password='toortoor')
ssh_conn('192.168.144.10', username='root', password='toortoor')

# 1b
def ssh_conn2(ip_addr, username, password, device_type='cisco_ios'):
    print('ip_addr     : {}'.format(ip_addr))
    print('username    : {}'.format(username))
    print('password    : {}'.format(password))
    print('device_type : {}'.format(device_type))
    print('-' * 20)

ssh_conn2('192.168.144.10', 'root', 'toortoor')
ssh_conn2('192.168.144.10', 'root', 'toortoor', 'linux')

ubuntu_box = {
    'ip_addr': '192.168.144.100',
    'username': 'groot',
    'password': 'toorg',
    'device_type': 'linux'
}
ssh_conn2(**ubuntu_box)