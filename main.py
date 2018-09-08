from time import sleep
from network import *
from visualisation import plotAllInOne
from action import ACTION, getAction

if __name__ == '__main__':
    Config.parse_config()
    action = getAction()
    if action == ACTION.SCAN:
        scann()
    if action == ACTION.INTERFACE:
        monitorMode()
    elif action == ACTION.EVALUATE:
        plotAllInOne()


def scann():
    try:
        startMonitorMode()
        captureDNS()
    except KeyboardInterrupt:
        print("Abort...")
    finally:
        stopMonitorMode()
    exit(1)


def interdaceToMonitorMode():
    try:
        startMonitorMode()
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("Abort...")
    finally:
        stopMonitorMode()
    exit(1)
