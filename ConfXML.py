from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import CommitError

dev = Device('host', user='user', password='pwd')

dev.open()

cu = Config(dev)

data1 = """<snmp>
      <community>
        <name>iBGP</name>
      </community>
    </snmp>
"""

data = """
<interfaces>
  <interface>
    <name>ge-0/0/20</name>
    <unit>
      <name>0</name>
      <family>
        <ethernet-switching>
        <native-vlan-id>Pink</native-vlan-id>
        </ethernet-switching>
      </family>
    </unit>
  </interface>
</interfaces>
"""

#cu.load(data, format='xml')
cu.load(data)

print "\nconfig# show | compare"
cu.pdiff()

if cu.commit_check():
    print "\nCommiting..\n"
#   cu.commit(comment="Configuring ge-1/0/1 interfaces")
    cu.commit(sync=True)
else:
    cu.rollback()

print "Rolling back the configuration"
cu.rollback(rb_id=1)
cu.commit(detail=True)
