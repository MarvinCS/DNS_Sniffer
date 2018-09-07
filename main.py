from time import sleep

from network import *
from visualisation import showTopTopDNSServer, showTopTenDomains, plotAllInOne
from action import ACTION, getAction

if __name__ == '__main__':
    action = getAction()
    interface = "wlp5s0"
    channel = 6
    if action == ACTION.SCAN or action == ACTION.MONITOR:
        # interface = chooseInterface()
        try:
            startMonitorMode(interface, channel)
            if action == ACTION.SCAN:
                captureDNS()
            else:
                while True:
                    sleep(1)
        except KeyboardInterrupt:
            print("Abort...")
        finally:
            stopMonitorMode(interface)
            exit(1)
    elif action == ACTION.EVALUATE:
        showTopTenDomains()
        showTopTopDNSServer()
        plotAllInOne()
        #sleep(5)
        #plotAllInOne(update=True)
    else:
        print("What to do??")
