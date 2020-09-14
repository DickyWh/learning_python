#!/usr/bin/env python
"""Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file
contents to a variable. Print out the file contents to the screen. Also print out the type of the
variable (you should have a string at this point).
Close the file.
Open the file a second time using a Python context manager (with statement). Read in the file
contents using the .readlines() method. Print out the file contents to the screen. Also print out
the type of the variable (you should have a list at this point).
"""
from __future__ import print_function, unicode_literals

banner = "*-*" * 33
f = open("show_version.txt")
output = f.read()
print(output)
print(banner)
print(type(output))
f.close

with open("show_version.txt") as f:
    out = f.readlines()

print("\n" + banner)
print(out)
print(banner)
print(type(out))
f.close
