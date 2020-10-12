#!/usr/bin/env python
"""
Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with
a default value of 'cisco_ios'. Print all four of the function variables out as part of the
function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using
the **kwargs technique.
"""
from __future__ import print_function, unicode_literals




def ssh_conn(ip_addr, username, password, device_type='cisco_ios'):
    print("IP address is: {}".format(ip_addr))
    print("username: {}".format(username))
    print("password: {}".format(password))
    print("device_type: {}".format(device_type))
    print('-'*40)
    return

#default values
ssh_conn('192.168.1.1', password='admin123',  username='admin')

#+specifying device
ssh_conn('192.168.1.1', password='admin123',  username='admin', device_type='allied telesys')

#Calling func using dict

my_dict = {
    'ip_addr': '10.10.10.1',
    'username': 'cisco',
    'password': 'cisco123',
    'device_type': 'cisco_nxos',
}

ssh_conn(**my_dict)
