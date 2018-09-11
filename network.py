from scapy.all import *
from scapy.layers.dns import DNS
from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6

from util import executeAndSleep
from db import DB_Connector
from logging import getLogger
from config import Config
import tldextract

'''
You need root-permissions to execute this code
'''


def startMonitorMode():
    if Config.interface is None:
        Config.interface = Config.chooseInterface()
    executeAndSleep('ifconfig ' + Config.interface + ' down')
    executeAndSleep('iw dev ' + Config.interface + ' interface add mywlanmonitor type monitor')
    executeAndSleep('ifconfig mywlanmonitor down')
    executeAndSleep('iw dev mywlanmonitor set type monitor')
    executeAndSleep('ifconfig mywlanmonitor up')
    executeAndSleep(('iw dev mywlanmonitor set channel %s' % str(Config.channel)))


def stopMonitorMode():
    executeAndSleep('ifconfig mywlanmonitor down')
    executeAndSleep('iw dev mywlanmonitor del')
    executeAndSleep('ifconfig ' + Config.interface + ' up')
    executeAndSleep('service network-manager restart')


def captureDNS(_interface='mywlanmonitor'):
    print("Starting the scan:")
    sniff(iface=_interface, prn=filterPackage, filter="udp port 53", store=0)


def filterPackage(pkt: packet):
    try:
        print(pkt.summary())
        if DNS in pkt:
            dns_str = str(pkt[DNS].summary())
            # Example dns_str: DNS Qry "b'id.google.com.'
            request = re.search('DNS Qry "b\'.*\'', dns_str)
            if request:
                domain = re.search('\'.*\'', request.group(0)).group(0)[1:-2]
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


def getDomain(dns_string: str):
    domain = re.search('\'.*\'', dns_string).group(0)[1:-2]
    return tldextract.extract(domain).registered_domain
