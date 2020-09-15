#!/usr/bin/env python
"""Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
"""
from __future__ import print_function, unicode_literals

with open('show_ip_bgp_summ.txt') as f:
    showbgp = f.readlines()

firstline = showbgp[0].strip()
locAS = firstline.split()
locASnum = locAS[-1]

lastline = showbgp[-1].strip()
bgppeer = lastline.split()
bgppeerip = bgppeer[0]
print("Номер локальной AS BGP: {}, IP адрес BGP peer: {}".format(locASnum, bgppeerip))
