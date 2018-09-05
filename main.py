import os
import pyshark

'''
You need root-permissions to execute this code
'''


def startMonitorMode(_interface='wlan1'):
    os.system('ifconfig ' + _interface + ' down')
    os.system('iw dev ' + _interface + ' interface add mywlanmonitor type monitor')
    os.system('ifconfig mywlanmonitor down')
    os.system('iw dev mywlanmonitor set type monitor')
    os.system('ifconfig mywlanmonitor up')


def stopMonitorMode(_interface='wlan1'):
    os.system('ifconfig mywlanmonitor down')
    os.system('iw dev mywlanmonitor del')
    os.system('ifconfig ' + _interface + ' up')
    os.system('service network-manager restart')


def chooseInterface():
    print('Available network-interfaces:')
    os.system('ifconfig -a | sed \'s/[ \t].*//;/^\(lo\|\)$/d\'')
    return input('\nWhich one do you want to use?\n')


def captureDNS(_interface='mywlanmonitor'):
    capture = pyshark.LiveCapture(interface=_interface, bpf_filter='udp port 53')
    for packet in capture.sniff_continuously(packet_count=2):
        if 'DNS Layer' in str(packet.layers):
            if packet.dns.qry_name:
                try:
                    print("Source: " + packet.ip.src)
                    print("Target: " + packet.ip.dst)
                except AttributeError:
                    print("IP-informations are not available")
                print(packet.dns)



interface = chooseInterface()
startMonitorMode(interface)
captureDNS()
stopMonitorMode(interface)
