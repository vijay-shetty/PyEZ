import os, sys, logging
from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
from jnpr.junos.exception import ConnectError

host = '10.209.1.228'
package = '/var/tmp/jpuppet-3.6.1_3.0_x86-32.tgz'
remote_path = '/var/tmp'
validate = True
logfile = '/var/log/install.log'

def update_progress(dev, report):
    # log the progress of the installing process
    logging.info(report)

def main():
    # initialize logging
    logging.basicConfig(filename=logfile, level=logging.INFO,
    format='%(asctime)s:%(name)s: %(message)s')
    logging.getLogger().name = host
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info('Information logged in {0}'.format(logfile))
    # verify package exists
    if not (os.path.isfile(package)):
        msg = 'Software package does not exist: {0}. '.format(package)
        logging.error(msg)
        sys.exit()

    try:
        dev = Device(host=host, user='user', password='pwd')
        dev.open()
    except ConnectError as err:
        logging.error('Cannot connect to device: {0}\n'.format(err))
        return

    # Create an instance of SW
    sw = SW(dev)
    try:
        logging.info('Starting the software upgrade process: {0}'.format(package))
        ok = sw.install(package=package, progress=update_progress)
    except Exception as err:
        msg = 'Unable to install software, {0}'.format(err)
        logging.error(msg)
        ok = False

    if ok is True:
        logging.info('Software installation complete. Rebooting')
#        rsp = sw.reboot()
        logging.info('Upgrade pending reboot cycle, please be patient.')
        logging.info(rsp)
    else:
        msg = 'Unable to install software, {0}'.format(ok)
        logging.error(msg)

    # End the NETCONF session and close the connection
    dev.close()

if __name__ == "__main__":
    main()
