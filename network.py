import os
from time import sleep
import pyshark
from sympy import pretty_print
from util import executeAndSleep
from db import DB_Connector

'''
You need root-permissions to execute this code
'''


def startMonitorMode(_interface='wlan1'):
    executeAndSleep('ifconfig ' + _interface + ' down')
    executeAndSleep('iw dev ' + _interface + ' interface add mywlanmonitor type monitor')
    executeAndSleep('ifconfig mywlanmonitor down')
    executeAndSleep('iw dev mywlanmonitor set type monitor')
    executeAndSleep('ifconfig mywlanmonitor up')


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
    dbc = DB_Connector.getInstance()
    capture = pyshark.LiveCapture(interface=_interface, bpf_filter='udp port 53')
    for packet in capture.sniff_continuously(packet_count=2):
        if 'DNS Layer' in str(packet.layers):  # We only want DNS traffic
            # if packet.dns.qry_name:
            try:
                #pretty_print(packet.ip)
                src = packet.ip.src
                dst = packet.ip.dst
                # domain = packet.dns.qry_name
                # response = packet.dns.resp_name
                print(src, dst)  # , domain, response)
            except AttributeError:
                print("IP-informations are not available")
                print(packet)


if __name__ == '__main__':
    interface = chooseInterface()
    startMonitorMode(interface)
    captureDNS()
    stopMonitorMode(interface)
