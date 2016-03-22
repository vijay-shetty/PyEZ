from jnpr.junos import Device
from lxml import etree

dev = Device('10.209.16.236', user='regress', password='MaRtInI')

try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)
	

#op = dev.rpc.get_interface_information()
op = dev.rpc.get_interface_information({'format': 'text'})
#op = dev.rpc.get_interface_information(interface_name='lo0', terse=True)
print (etree.tostring(op))

#for i in op.xpath('.//link-level-type'):
#    print i.text
dev.close()
