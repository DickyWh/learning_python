#!/usr/bin/env python
"""
Read in the "show_version.txt" file. From this file use regular expressions to extract the
os_version, serial_number, and configuration register value.

Your output should look as follows:

            OS Version: 15.4(2)T1
        Serial Number: FTX0000038X
    Config Register: 0x2102

"""
from __future__ import unicode_literals, print_function
import re

with open('show_version.txt') as f:
    output = f.read()

#show_ver = output.splitlines()

match = re.search(r"^Cisco IOS Software,.*Version (.*),", output, flags=re.M)
if match:
    os_ver = match.group(1)

match = re.search(r"^Processor board ID (.*)$", output, flags=re.M)
if match:
    sn = match.group(1)

match = re.search(r"^Configuration register is (.*)$", output, flags=re.M)
if match:
    conf = match.group(1)

print()
print('OS Version: {}'.format(os_ver))
#print("{:>20}: {:15}".format("OS Version", os_ver))
print('Serial Number: {}'.format(sn))
#print("{:>20}: {:15}".format("Serial Number", sn))
print('Config Register: {}'.format(conf))
#print("{:>20}: {:15}".format("Config Register", conf))
print()
