import os
import pyshark

'''
You need root-permissions to execute this code
'''


def startMonitorMode(interface='wlan1'):
    os.system('ifconfig ' + interface + ' down')
    os.system('iw dev ' + interface + ' interface add mywlanmonitor type monitor')
    os.system('ifconfig mywlanmonitor down')
    os.system('iw dev mywlanmonitor set type monitor')
    os.system('ifconfig mywlanmonitor up')


def stopMonitorMode(interface='wlan1'):
    os.system('ifconfig mywlanmonitor down')
    os.system('iw dev mywlanmonitor del')
    os.system('ifconfig ' + interface + ' up')
    os.system('service network-manager restart')


def captureDNS(interface='mywlanmonitor'):
    capture = pyshark.LiveCapture(interface=interface, bpf_filter='udp port 53')
    for packet in capture.sniff_continuously(packet_count=2):
        if 'DNS Layer' in str(packet.layers):
            print("Source: " + packet.ip.src)
            print("Target: " + packet.ip.dst)
            print(packet.dns)


startMonitorMode('wlp5s0')
captureDNS()
stopMonitorMode('wlp5s0')
