from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

dev = Device('host', user='user', password='pwd')

dev.open()

sft= SW(dev)

print sft.poweroff()
