from PyQt5 import QtWidgets
from scapy.all import *
from scapy.layers.dns import DNS
from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6

from util import executeAndSleep, myprint
from db import DB_Connector
from logging import getLogger
from config import Config
import tldextract

'''
You need root-permissions to execute this code
'''


def startMonitorMode(list_widget: QtWidgets.QListWidget = None):
    if Config.interface is None:
        Config.interface = Config.chooseInterface()
    myprint(executeAndSleep('ifconfig ' + Config.interface + ' down'), list_widget)
    myprint(executeAndSleep('iw dev ' + Config.interface + ' interface add mywlanmonitor type monitor'), list_widget)
    myprint(executeAndSleep('ifconfig mywlanmonitor down'), list_widget)
    myprint(executeAndSleep('iw dev mywlanmonitor set type monitor'), list_widget)
    myprint(executeAndSleep('ifconfig mywlanmonitor up'), list_widget)
    myprint(executeAndSleep(('iw dev mywlanmonitor set channel %s' % str(Config.channel))), list_widget)


def stopMonitorMode(list_widget: QtWidgets.QListWidget = None):
    myprint(executeAndSleep('ifconfig mywlanmonitor down'), list_widget)
    myprint(executeAndSleep('iw dev mywlanmonitor del'), list_widget)
    myprint(executeAndSleep('ifconfig ' + Config.interface + ' up'), list_widget)
    myprint(executeAndSleep('service network-manager restart'), list_widget)


def captureDNS(_interface='mywlanmonitor', list_widget: QtWidgets.QListWidget = None):
    myprint("Starting the scan:", list_widget)
    sniff(iface=_interface, prn=lambda x: filterPackage(x, list_widget), filter="udp port 53", store=0)


def filterPackage(pkt: packet, list_widget: QtWidgets.QListWidget = None):
    try:
        if DNS in pkt:
            dns_str = str(pkt[DNS].summary())
            # Example dns_str: DNS Qry "b'id.google.com.'
            request = re.search('DNS Qry "b\'.*\'', dns_str)
            if request:
                domain = re.search('\'.*\'', request.group(0)).group(0)[1:-2]
                src, dns_server = getSrcAndDst(pkt)
                log_string = "Domain: %s, src: %s, dns-server: %s" % (domain, src, dns_server)
                myprint(log_string, list_widget)
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
