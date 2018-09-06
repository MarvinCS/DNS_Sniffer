import argparse
from enum import Enum


class ACTION(Enum):
    SCAN = 1,
    EVALUATE = 2


def getAction():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--scan', action="store_true", help="Use this option to start a new scan")
    parser.add_argument('-e', '--evaluate', action="store_true", help="Evaluate the results of previous scans")
    args = parser.parse_args()
    if args.scan:
        return ACTION.SCAN
    elif args.evaluate:
        return ACTION.EVALUATE
    else:
        parser.print_help()
        exit(1)
