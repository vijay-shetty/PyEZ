from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import CommitError
from lxml.builder import E

dev = Device('host', user='user', password='pwd', gather_facts=False)

dev.open()

cu = Config(dev)


data = (
    E('firewall',
        E('filter',
     	    E('name', 'test'),
      	    E('term',
    		E('name', 'term1'),
    		E('from',
  			E('source-address',
  			E('name', '1.1.1.1/32')
  			)		
  		)
             )
         )
     )
)

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
