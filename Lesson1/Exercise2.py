#!/usr/bin/env python
"""Prompt a user to enter in an IP address from standard input. Read the IP address in and break it
up into its octets. Print out the octets in decimal, binary, and hex.
Your program output should look like the following:
$ python exercise2.py
Please enter an IP address: 80.98.100.240
    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------
Four columns, fifteen characters wide, a header column, data centered in the column.
"""
from __future__ import print_function

try:
        #Pyhton2
	ip = raw_input ("Please enter an IP address: ")
except NameError:
        #Pyhton3
	ip = input ("Please enter an IP address: ")
	
oct = ip.split('.')
oct1 = "octet1"
oct2 = "octet2"
oct3 = "octet3"
oct4 = "octet4"
print("\n")
print("{:^15}{:^15}{:^15}{:^15}".format(oct1, oct2, oct3, oct4)) 
print("-" * 80)
print("{:^15}{:^15}{:^15}{:^15}".format(oct[0], oct[1], oct[2], oct[3]))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(oct[0])), bin(int(oct[1])), bin(int(oct[2])), bin(int(oct[3]))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(oct[0])), hex(int(oct[1])), hex(int(oct[2])), hex(int(oct[3]))))
print("-" * 80)      
print("\n")
