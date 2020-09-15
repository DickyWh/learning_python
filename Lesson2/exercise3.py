#!/usr/bin/env python

"""Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:
    ----
    from pprint import pprint
    pprint(some_var)
    ----
Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three arp entries back together as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".
"""
from __future__ import print_function, unicode_literals
from pprint import pprint
with open("show_arp.txt") as f:
    show_arp = f.readlines()

print("Полный вывод arp таблицы: {}{}".format('\n', show_arp))
print("-" * 30)
print(type(show_arp))
print("-"* 30)

show_arp = show_arp[1:]
print("Очищенный от заголовка список:")
pprint(show_arp)

#sorting records in list
show_arp.sort()
#cut the list till only 3 first records

outs = show_arp[:3]
outs = "\n".join(outs)
print("Первые три записи из arp таблицы:")

print(outs)

with open("arp_entries.txt", "wt") as f:
    f.write(outs)
