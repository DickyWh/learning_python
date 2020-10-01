#!/usr/bin/env python
"""
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' field is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' field is
'juniper', then set the 'platform' to 'junos'.

Create a second dictionary named bgp_fields. The bgp_fields should have a key for 'bgp_as',
'peer_as', and 'peer_ip'.

Using the .update() method add the bgp_fields key-value pairs to the network device dictionary.

Using a for-loop iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop iterate over the dictionary and print out all of the dictionary keys and
values.
"""
from __future__ import unicode_literals, print_function

net_device = {
    'ip_addr': '192.168.1.1',
    'vendor': 'cisco',
    'username': 'root',
    'password': 'admin'
    }

print('Оригинальный словарь: {}{}'.format('\n', net_device))
print()
print('IP адрес устройства: {}'.format(net_device['ip_addr']))
print()

if net_device['vendor'].lower() == 'cisco':
    net_device['platform'] = 'ios'
elif net_device['vendor'].lower() == 'juniper':
    net_device['platform'] = 'junos'

print('-'*30)
print('Дополнение платформы: {}{}'.format('\n', net_device))
print()

bgp_fields = {
    'bgp_as': '125',
    'peer_as': '33',
    'peer_ip': '192.168.1.33'
    }

net_device.update(bgp_fields)

print('-'*30)
print('Добавление данных из другого словаря: {}{}'.format('\n', net_device))
print()

for key in net_device:
    print('Ключи словаря: {}'.format(key))

print('-'*30)

for key, value in net_device.items():
    print('Ключ: {}'.format(key))
    print('Значение: {}'.format(value))
    print('-'*80)

print('В одну строку и ключ и значение')
print()
for key, value in net_device.items():
    print('{Ключ:} : {Значение:}'.format(Ключ=key, Значение=value))
    print('-'*30)
print()
