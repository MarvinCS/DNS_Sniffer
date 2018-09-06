from network import *
import Action

if __name__ == '__main__':
    action = Action.getAction()
    if action == Action.ACTION.SCANN:
        interface = chooseInterface()
        startMonitorMode(interface)
        captureDNS()
        stopMonitorMode(interface)
    elif action == Action.ACTION.EVALUATE:
        print("We must code the evaluation :D")
    else:
        print("What to do??")
