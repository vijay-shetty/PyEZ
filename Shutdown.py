from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

dev = Device('10.209.16.237', user='regress', password='MaRtInI')

dev.open()

sft= SW(dev)

print sft.poweroff()
