from jnpr.junos import Device

dev = Device('10.209.16.236', user='regress', password='MaRtInI')

dev.open()

print dev.cli("show version | match py")
