from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.utils.sw import SW
import sys

dev = Device('nms5-mx240-a', user='regress', passwd='MaRtInI')

dev.open()

print "===========Setting the configuration==========="

cu = Config(dev)

#rsp = cu.load( path="config-example.conf" )
config_set = """set system extensions providers juniper license-type juniper deployment-scope commercial"""

cu.load(config_set, format="set", merge=True)

cu.commit(comment="===========Set the configuration successfully===========")
print dev.cli("show configuration system extensions providers", warning=False)

cu.rollback(rb_id=1)
cu.commit(detail=True)

print dev.cli("show configuration system extensions providers", warning=False)
