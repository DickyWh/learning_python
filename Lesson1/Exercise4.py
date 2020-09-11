#!/usr/bin/env python
"""Create a show_version variable that contains the following

show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "

Remove all leading and trailing whitespace from the string.
Split the string and extract the model and serial_number from it.
Check if 'Cisco' is contained in the model string (ignore capitalization).
Check if '881' is in the model string.
Print out both the serial number and the model.
"""
from __future__ import print_function, unicode_literals

show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "
variables = show_version.split()

model = variables[1]
model_881 = "881" in model
vendor_cisco = "cisco" in model.lower()
sn = variables[2]



print("all code: {}".format(variables))


print("model: {}".format(model))
print("Checking that Cisco is vendor: {}".format(vendor_cisco))
print("Checking that Model is 881 series: {}".format(model_881))
print("s/n: {}".format(sn))






