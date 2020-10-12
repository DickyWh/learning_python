#!/usr/bin/env python
"""
Create an ssh_conn function. This function should have three parameters: ip_addr, username, and
password. The function should print out each of these three variables and clearly indicate which
variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.
"""
from __future__ import print_function, unicode_literals


def ssh_conn(ip_addr, username, password):
    print("IP address is: {}".format(ip_addr))
    print("username: {}".format(username))
    print("password: {}".format(password))
    return

#positional arguments
ssh_conn('192.168.1.1', 'admin',  'admin123')

print('-'*40)

#named arguments
ssh_conn(ip_addr='192.168.1.1', username='admin', password='admin123')

print('-'*40)
#mixed of positional and named arguments
ssh_conn('192.168.1.1', username='cisco', password='cisco123')
