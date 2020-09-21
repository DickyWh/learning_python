#!/usr/bin/env python
"""
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract
all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list
where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data
structure to the screen. Your output should look as follows:

[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]

"""
from __future__ import unicode_literals, print_function
from pprint import pprint

vlansl = []
with open('show_vlan.txt') as f:
    vlist = f.read()

for line in vlist.splitlines():
    if 'VLAN' in line or '----' in line or line.startswith('   '):
        continue
    fields = line.split()
    vlan_id = fields[0]
    vlan_n = fields[1]
    vlansl.append((vlan_id, vlan_n))

print()
pprint(vlansl)
print()
#print(vlist)
