from jnpr.junos import Device
import sys
from getpass import getpass

dev = Device('host', user='user', password='pwd')

#dev = Device('10.209.16.236')
try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)

print dev.facts
dev.facts_refresh()
print dev.facts

print dev.cli("show version | display xml rpc")
dev.close()
