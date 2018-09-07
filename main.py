from time import sleep
from network import *
from visualisation import showTopTopDNSServer, showTopTenDomains, plotAllInOne
from action import ACTION, getAction

if __name__ == '__main__':
    Config.parse_config()
    action = getAction()

    if action == ACTION.SCAN or action == ACTION.INTERFACE:
        try:
            startMonitorMode()
            if action == ACTION.SCAN:
                captureDNS()
            else:
                while True:
                    sleep(1)
        except KeyboardInterrupt:
            print("Abort...")
        finally:
            stopMonitorMode()
            exit(1)
    elif action == ACTION.EVALUATE:
        plotAllInOne()
        sleep(5)
        plotAllInOne(update=True)
    elif action == ACTION.MONITOR:
        print(-1)
        ## TODO Multithreading
