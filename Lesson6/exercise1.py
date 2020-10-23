#!/usr/bin/env python
"""Establish a connection to the network device and print out the device's prompt."""

from __future__ import print_function, unicode_literals
#ConnectHandler
from netmiko import Netmiko
from getpass import getpass

try:
    host = raw_input("Enter host to connect to: ")
except NameError:
    host = input("Enter host to connect to: ")

net_conn = Netmiko(host=host, username='cisco',
                   password=getpass(), device_type='cisco_ios')

print(net_conn.find_prompt())

