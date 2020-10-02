#!/usr/bin/env python
"""
Create three separate lists of IP addresses. The first list should be the IP addresses for the
Houston data center routers and should have over ten IP addresses in it including some duplicate IP
addresses.

The second list should be the Atlanta data center routers and should have at least eight IP
addresses including some that overlap with the Houston data center.

The third list should be the Chicago data center routers and should have at least eight IP
addresses. The Chicago IP addresses have some overlap with the IP addresses in both Houston
and in Atlanta

Convert each of these three lists to a set.

Using set operations, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
"""
from __future__ import unicode_literals, print_function

Houston_routers = [
    '10.16.0.1',
    '10.17.0.1',
    '10.18.0.1',
    '10.19.0.1',
    '10.16.0.1',
    '10.20.0.1',
    '10.17.0.1',
    '10.21.0.1',
    '10.22.0.1',
    '10.23.0.1'
]

print('список ip роутеров Houston: {}{}'.format('\n', Houston_routers))
print('-'*30)

Atlanta_routers = [
    '172.16.0.1',
    '172.17.0.1',
    '172.18.0.1',
    '172.19.0.1',
    '172.16.0.1',
    '172.20.0.1',
    '10.22.0.1',
    '10.23.0.1'
]

print('список ip роутеров Atlanta: {}{}'.format('\n', Atlanta_routers))
print('-'*30)

Chicago_routers = [
    '192.168.0.1',
    '192.168.1.1',
    '192.168.2.1',
    '192.168.3.1',
    '172.16.0.1',
    '172.20.0.1',
    '10.22.0.1',
    '10.23.0.1'
]

print('список ip роутеров Chicago: {}{}'.format('\n', Chicago_routers))
print('-'*30)

set_Houston = set(Houston_routers)
print('Сконвертированный класс данных Houston: {}'.format(type(set_Houston)))

set_Atlanta = set(Atlanta_routers)
print('Сконвертированный класс данных Atlanta: {}'.format(type(set_Atlanta)))

set_Chicago = set(Chicago_routers)
print('Сконвертированный класс данных Chicago: {}'.format(type(set_Chicago)))

print()
print('Пересечение адресов в Houston и Atlanta: {}{}'.format('\n', set_Houston.intersection(set_Atlanta)))
print()

print('Пересечение адресов в Houston, Atlanta, Chicago:\n {}'.format(set_Houston & set_Atlanta & set_Chicago))
print()

print('Уникальные адреса для Chicago:\n {}'.format(set_Chicago.difference(set_Houston).difference(set_Atlanta)))
print('-'*30)
