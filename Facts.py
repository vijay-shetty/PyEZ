import json
import yaml
from jnpr.junos import Device
import sys

dev = Device('10.209.16.236', user='regress', password='MaRtInI')
try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)

#print dev.facts_chassis['model']	
#print dev.facts_refresh(exception_on_failure=True)
print dev.facts
#print yaml.dump(dev.facts)
#print json.dumps(dev.facts)

dev.close()