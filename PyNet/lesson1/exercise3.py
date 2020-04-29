#!/usr/bin/env python3
""" PyNet Lesson 1, Exercise 3
Create three different variables the first variable should use all lower
case characters with underscore ( _ ) as the word separator. The second
variable should use all upper case characters with underscore as the word
separator. The third variable should use numbers, letters, and underscore,
but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are
unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
"""

from __future__ import unicode_literals

ipv6_addr1 = '::1'
IPV6_ADDR2 = '::1'
IPv6_Addr3 = '::1'

print('{} == {} : {}'.format(ipv6_addr1, IPV6_ADDR2, ipv6_addr1 == IPV6_ADDR2))
print('{} != {} : {}'.format(ipv6_addr1, IPv6_Addr3, ipv6_addr1 != IPv6_Addr3))