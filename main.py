from network import *
from visualisation import showTopTopDNSServer, showTopTenDomains
import action

if __name__ == '__main__':
    action = action.getAction()
    if action == action.ACTION.SCANN:
        interface = chooseInterface()
        startMonitorMode(interface)
        captureDNS()
        stopMonitorMode(interface)
    elif action == action.ACTION.EVALUATE:
        showTopTenDomains()
        showTopTopDNSServer()
    else:
        print("What to do??")
