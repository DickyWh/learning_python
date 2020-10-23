#!/usr/bin/env python
"""
Optional, use send_command() in conjunction with ntc-templates to execute a show command. Have
TextFSM automatically convert this show command output to structured data.
"""
from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

try:
    host = raw_input("Enter host to connect to: ")
except NameError:
    host = input("Enter host to connect to: ")

password = getpass()
dev = {
    "host": host,
    "username": "cisco",
    "password": password,
    "device_type": "cisco_ios",
}

command = "show ip int brief"
net_connect = ConnectHandler(**dev)
output = net_connect.send_command(command, use_textfsm=True)

print()
print("-" * 80)
pprint(output)
print("-" * 80)
print()
