from jnpr.junos import Device
from lxml import etree

dev = Device('host', user='user', password='pwd')

dev.open()

# for xml out, from which you can get any detail easily
op = dev.rpc.get_software_information()
print etree.tostring(op)

# say to fetch junos-version
print op.findtext('junos-version')

# for text output
op = dev.rpc.get_software_information({'format':'text'})
print op.text

dev.close()
