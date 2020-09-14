#!/usr/bin/env python
"""Create a list of five IP addresses.
Use the .append() method to add an IP address onto the end of the list. Use the .extend()
method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
P адрес из списка: {}".format(fulllist[0]))
P адрес из списка: {}".format(fulllist[0]))
Print out the entire list of ip addresses. Print out the first IP address in the list. Print out
the last IP address in the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in
the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address
in the list.
"""
from __future__ import print_function, unicode_literals

list_ip = ['192.168.1.1', '172.16.0.1', '10.194.99.2', '10.150.1.200']

list_ip.append("10.1.1.1")

list_ip.extend(["192.0.0.0", "255.255.255.255"])
fulllist = list_ip
print("Полный список адресов: {}".format(list_ip))
print('\n')
print("Первый IP адрес из списка: {}".format(fulllist[0]))
print('\n')
print("Последний IP адрес из списка: {}".format(fulllist[-1]))
print('\n')

list_ip.pop(0)
list_ip.pop()

print("Список с удаленными первым и последним IP адреса: {}".format(list_ip))
print('\n')

list_ip[0]="2.2.2.2"

print("измененный список IP адресов: {}".format(list_ip))
print('\n')

print("Первый IP адрес в измененном списке: {}".format(list_ip[0]))
