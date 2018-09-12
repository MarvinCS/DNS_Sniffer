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
        executeAndSleep('ifconfig ' + Config.interface + ' down'),
        executeAndSleep('iw dev ' + Config.interface + ' interface add mywlanmonitor type monitor')
        executeAndSleep('ifconfig mywlanmonitor down')
        executeAndSleep('iw dev mywlanmonitor set type monitor')
        executeAndSleep('ifconfig mywlanmonitor up')
        executeAndSleep(('iw dev mywlanmonitor set channel %s' % str(Config.channel)))

    @staticmethod
    def stopMonitorMode():
        """Resets the normal state of interface"""
        executeAndSleep('ifconfig mywlanmonitor down')
        executeAndSleep('iw dev mywlanmonitor del')
        executeAndSleep('ifconfig ' + Config.interface + ' up')
        executeAndSleep('service network-manager restart')

    @staticmethod
    def captureDNS(_interface='mywlanmonitor'):
        """Start capturing dns-packages and saves them in the database"""
        myprint("Starting the scan:")
        sniff(iface=_interface, prn=Network.filterPackage, filter="udp port 53", store=0)

    @staticmethod
    def filterPackage(pkt: packet):
        """This method is called by every captured network-package. Saves the relevant data of a matching dns-package to database"""
        if Config._scanning_thread:  # This is to stop the capturing of packages while multithreading
            try:
                if DNS in pkt:
                    dns_str = str(pkt[DNS].summary())
                    # Example dns_str: DNS Qry "b'id.google.com.'
                    request = re.search('DNS Qry "b\'.*\'', dns_str)
                    if request:
                        domain = re.search('\'.*\'', request.group(0)).group(0)[1:-2]
                        src, dns_server = Network.getSrcAndDst(pkt)
                        myprint("Domain: %s, src: %s, dns-server: %s" % (domain, src, dns_server))
                        dbc = Connection_handler.getConnection()
                        dbc.addRequest(domain, dns_server, ip=src)
            except Exception:
                pass
        else:
            if Config._log_window is not None:
                Config._log_window.lv_log.addItem("Stopping...")
            Connection_handler.remomveConnection()
            # stopMonitorMode()
            exit(0)

    @staticmethod
    def getSrcAndDst(pkt: packet):
        """Return source and destination of the given package"""
        if IP in pkt:
            return pkt[IP].src, pkt[IP].dst
        elif IPv6 in pkt:
            return pkt[IPv6].src, pkt[IPv6].dst

    @staticmethod
    def getDomain(dns_string: str):
        """Delets the subdomain an the given domain-string"""
        domain = re.search('\'.*\'', dns_string).group(0)[1:-2]
        return tldextract.extract(domain).registered_domain
