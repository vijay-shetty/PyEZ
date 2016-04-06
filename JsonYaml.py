import json
#import yaml
import sys
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from pprint import pprint

dev = Device('host', user='user', password='pwd')

try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)

dev.facts_refresh(exception_on_failure=True)
#print yaml.dump(dev.facts)
print json.dumps(dev.facts)
op = json.dumps(dev.facts)
pprint (op)
dev.close()
