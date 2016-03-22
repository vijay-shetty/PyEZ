from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys

dev = Device('10.209.1.228', user='regress', password='MaRtInI')

try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)
	
dev.bind(cu=Config)
dev.cu.lock()
dev.cu.load('set interfaces ge-0/0/0 description test15',format='set')
dev.cu.pdiff()
dev.cu.commit(detail=True)
dev.cu.unlock()
dev.close()
