from jnpr.junos import Device

dev = Device('host', user='user', password='pwd')

dev.open()

print dev.cli("show version | match py")
