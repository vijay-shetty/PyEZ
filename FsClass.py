from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.utils.fs import FS
from pprint import pprint
import sys


dev = Device('host', user='user', password='pwd')

dev.open()

fs = FS(dev)

pprint (fs.ls(path="/var/tmp/", brief=True))

print fs.pwd()
