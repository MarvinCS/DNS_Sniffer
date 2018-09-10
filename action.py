import argparse
from enum import Enum


class ACTION(Enum):
    SCAN = 1
    EVALUATE = 2
    INTERFACE = 3
    GUI = 4


def getAction():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--scan', action="store_true", help="Use this option to start a new scan")
    parser.add_argument('-e', '--evaluate', action="store_true", help="Evaluate the results of previous scans")
    parser.add_argument('-i', '--interface', action="store_true",
                        help="Config the network-interface to receive network-packages")
    parser.add_argument('-g', '--gui', action="store_true",
                        help="Starts a gui. You still need root-permissions to scan a network")
    args = parser.parse_args()
    if args.scan:
        return ACTION.SCAN
    elif args.evaluate:
        return ACTION.EVALUATE
    elif args.interface:
        return ACTION.INTERFACE
    elif args.gui:
        return ACTION.GUI
    else:
        parser.print_help()
        exit(1)
