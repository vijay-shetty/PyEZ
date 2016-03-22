from jnpr.junos import Device

dev = Device('10.209.16.236', user='vijay', password='Puppet', gather_facts=False)
try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)

print dev.cli("show version", warning=False)

dev.close()
