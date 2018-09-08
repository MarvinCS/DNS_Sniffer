from time import sleep
from network import *
from visualisation import plotAllInOne
from action import ACTION, getAction


def scan():
    try:
        startMonitorMode()
        captureDNS()
    except KeyboardInterrupt:
        print("Abort...")
    finally:
        stopMonitorMode()
    exit(1)


def interfaceToMonitorMode():
    try:
        startMonitorMode()
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("Abort...")
    finally:
        stopMonitorMode()
    exit(1)


if __name__ == '__main__':
    Config.parse_config()
    action = getAction()
    if action == ACTION.SCAN:
        scan()
    if action == ACTION.INTERFACE:
        interfaceToMonitorMode()
    elif action == ACTION.EVALUATE:
        plotAllInOne()
