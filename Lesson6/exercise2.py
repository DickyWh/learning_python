#!/usr/bin/env python
"""
Use send_command() to send a show command down the SSH channel. Retrieve the results and print the
results to the screen.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

password = getpass()
try:
        host = raw_input("Enter host to connect to: ")
except NameError:
        host = input("Enter host to connect to: ")

my_dev = {
        'host': host,
        'username': 'cisco',
        'password': password,
        'secret': password,
        'device_type': 'cisco_ios'
}

command_arp = 'sh arp'
command_sh_ip = 'sh ip int brief'
net_conn = Netmiko(**my_dev)
output1 = net_conn.send_command(command_arp)
output2 = net_conn.send_command(command_sh_ip)


print('-'*30)
print(output1)
print('-'*30)
print(output2)
print('-'*30)

