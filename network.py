from logging import getLogger

from PyQt5 import QtWidgets
from scapy.all import *
from scapy.layers.dns import DNS
from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6

from util import executeAndSleep, myprint
from db import Connection_handler
from config import Config
import tldextract


class Network:
    """You need root-permissions to execute the code in this class"""

    @staticmethod
    def startMonitorMode():
        """Set the specified interface to monitor-mode"""
        if Config.interface is None:
            Config.interface = Config.chooseInterface()
        executeAndSleep('ifconfig %s down' % Config.interface),
        executeAndSleep('iw dev %s interface add mywlanmonitor type monitor' % Config.interface)
        executeAndSleep('ifconfig mywlanmonitor down')
        executeAndSleep('iw dev mywlanmonitor set type monitor')
        executeAndSleep('ifconfig mywlanmonitor up')
        executeAndSleep(('iw dev mywlanmonitor set channel %s' % str(Config.channel)))

    @staticmethod
    def stopMonitorMode():
        """Resets the normal state of interface"""
        executeAndSleep('ifconfig mywlanmonitor down')
        executeAndSleep('iw dev mywlanmonitor del')
        executeAndSleep('ifconfig %s up' % Config.interface)
        executeAndSleep('service network-manager restart')

    @staticmethod
    def captureDNS(_interface='mywlanmonitor'):
        """Start capturing dns-packages and saves them in the database"""
        myprint("Starting the scan:")
        try:
            sniff(iface=_interface, prn=Network.filterPackage, filter="udp port 53", store=0)
        except OSError:
            Connection_handler.remove_connection()

    @staticmethod
    def filterPackage(pkt: packet):
        """This method is called by every captured network-package. Saves the relevant data of a matching dns-package to database"""
        try:
            if DNS in pkt:
                dns_str = str(pkt[DNS].summary())
                # Example dns_str: DNS Qry "b'id.google.com.'
                request = re.search('DNS Qry "b\'.*\'', dns_str)
                if request:
                    domain = re.search('\'.*\'', request.group(0)).group(0)[1:-2]
                    if not Config.subdomains:
                        domain = Network.remove_subdomain(domain)
                    src, dns_server = Network.getSrcAndDst(pkt)
                    myprint("Domain: %s, src: %s, dns-server: %s" % (domain, src, dns_server))
                    dbc = Connection_handler.getConnection()
                    dbc.addRequest(domain, dns_server, ip=src)
        except Exception:
            logger = getLogger("network")
            logger.exception("Fatal error in main loop")

    @staticmethod
    def getSrcAndDst(pkt: packet) -> (str, str):
        """Return source and destination of the given package"""
        if IP in pkt:
            return pkt[IP].src, pkt[IP].dst
        elif IPv6 in pkt:
            return pkt[IPv6].src, pkt[IPv6].dst

    @staticmethod
    def remove_subdomain(domain: str) -> str:
        """Trys to delet the subdomain an the given domain-string"""
        try:
            extract = tldextract.TLDExtract(
                suffix_list_urls=["file://%s/%s" % (Config.project_path, "suffix_list.dat")])
            extracted = extract(domain)
            return "%s.%s" % (extracted.domain, extracted.suffix)
        except Exception:
            myprint("Error while deleting subdomain of %s" % domain)
            return domain
