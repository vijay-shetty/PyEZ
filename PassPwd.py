from jnpr.junos import Device
import sys
from getpass import getpass

#password = getpass()
#dev = Device('10.209.16.236', user='regress', password=password)
dev = Device('10.209.1.228', user='regress')  #nms5-mx240-a

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