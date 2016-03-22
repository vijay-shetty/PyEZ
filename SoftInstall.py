from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
import sys

dev = Device('10.209.1.228', user='regress', passwd='MaRtInI')
try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)

sft= SW(dev)
print sft.install('/var/tmp/jpuppet-3.6.1_3.0_x86-32.tgz')
print dev.cli("show version", warning=False)
#print sft.reboot()

dev.close()