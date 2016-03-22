import json
import yaml
from jnpr.junos import Device
import sys
from pprint import pprint

dev = Device('10.209.16.236', user='vijay', password='Puppet', gather_facts=False)
try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)

print dev.facts_refresh(exception_on_failure=True)
pprint (dev.facts)

dev.close()