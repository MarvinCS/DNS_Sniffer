from network import *
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--scan', help="Use this option to start a new scan")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    print(createParser())
    '''
    interface = chooseInterface()
    startMonitorMode(interface)
    captureDNS()
    stopMonitorMode(interface)
    '''
