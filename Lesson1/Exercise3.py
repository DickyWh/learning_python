#!/usr/bin/env python
"""Create three different variables: the first variable should use all lower case characters with
underscore ( _ ) as the word separator. The second variable should use all upper case characters
with underscore as the word separator. The third variable should use numbers, letters, and
underscores, but still be a valid variable Python variable name.
Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
"""

from __future__ import unicode_literals

ipv6_addr1 = "ff80::123:1234:abcd:ef11"
IPV6_ADDR2 = "ff80::123:1234:adcd:ef12"
ipV6_Addr3 = "ff80::123:1234:abcd:ef13"

print("Variable #1 is IP address {}".format(ipv6_addr1))
print("Variable #2 is IP address {}".format(IPV6_ADDR2))
print("Variable #3 is IP address {}".format(ipV6_Addr3))

print("Comparing variable1 to variable2 is equal: {}".format(ipv6_addr1==IPV6_ADDR2))
print("Comparing variable1 to variable3 is not equal: {}".format(ipv6_addr1!=ipV6_Addr3))

