from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys

dev = Device('10.209.16.236', user='regress', password='MaRtInI', gather_facts=False)

try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)

cu = Config(dev)
data = """interfaces { 
    ge-1/0/1 {
        description "MPLS interface";
        unit 0 {
            family mpls;
        }      
    } 
    ge-1/0/2 {
        description "MPLS interface";
        unit 0 {
            family mpls;
        }      
    }   
}
protocols {
    mpls { 
        interface ge-1/0/1; 
        interface ge-1/0/2;            
    }
}
"""
cu.load(data, format='text')
cu.pdiff()
if cu.commit_check():
   cu.commit()
else:
   cu.rollback()

dev.close()