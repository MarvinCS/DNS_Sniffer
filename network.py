from scapy.all import *
from scapy.layers.dns import DNS, DNSStrField
from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6

from util import executeAndSleep
from db import DB_Connector
from logging import getLogger

'''
You need root-permissions to execute this code
'''


def startMonitorMode(_interface='wlan1', channel=-1):
    executeAndSleep('ifconfig ' + _interface + ' down')
    executeAndSleep('iw dev ' + _interface + ' interface add mywlanmonitor type monitor')
    executeAndSleep('ifconfig mywlanmonitor down')
    executeAndSleep('iw dev mywlanmonitor set type monitor')
    executeAndSleep('ifconfig mywlanmonitor up')
    executeAndSleep(('iw dev mywlanmonitor set channel %s' % str(channel)))


def stopMonitorMode(_interface='wlan1'):
    executeAndSleep('ifconfig mywlanmonitor down')
    executeAndSleep('iw dev mywlanmonitor del')
    executeAndSleep('ifconfig ' + _interface + ' up')
    executeAndSleep('service network-manager restart')


def chooseInterface():
    print('Available network-interfaces:')
    os.system('ifconfig -a | sed \'s/[ \t].*//;/^\(lo\|\)$/d\'')
    return input('\nWhich one do you want to use?\n')


def captureDNS(_interface='mywlanmonitor'):
    print("Starting the scan:")
    sniff(iface=_interface, prn=filterPackage, filter="udp port 53", store=0)


def filterPackage(pkt: packet):
    try:
        if DNS in pkt:
            dns_str = str(pkt[DNS].summary())
            # Example dns_str: DNS Qry "b'id.google.com.'
            request = re.search('DNS Qry "b\'.*\'', dns_str)
            if request:
                substring = request.group(0)
                domain = re.search('\'.*\'', substring).group(0)[1:-2]
                src, dns_server = getSrcAndDst(pkt)
                print(domain, src, dns_server)
                dbc = DB_Connector.getInstance()
                dbc.addRequest(domain, dns_server, ip=src)
    except Exception:
        logger = getLogger("test")
        logger.exception("Fatal error in main loop")


def getSrcAndDst(pkt: packet):
    if IP in pkt:
        return pkt[IP].src, pkt[IP].dst
    elif IPv6 in pkt:
        return pkt[IPv6].src, pkt[IPv6].dst


if __name__ == '__main__':
    interface = chooseInterface()
    startMonitorMode(interface)
    captureDNS()
    stopMonitorMode(interface)
