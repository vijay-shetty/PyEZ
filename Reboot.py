from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
import sys

dev = Device('host', user='user', password='pwd')
try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)

sft= SW(dev)
print sft.reboot()
#print sft.reboot(in_min=5)
#print ("Before Shutdown\n")
#print sft.poweroff()
#print ("After Shutdown\n")
