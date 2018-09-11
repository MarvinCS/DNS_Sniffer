import os
import subprocess
import time

from PyQt5 import QtWidgets


def now():
    return str((time.strftime('%Y-%m-%d %H:%M:%S')))


def executeAndSleep(command: str, _time=1):
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print(out, err)
    time.sleep(_time)
    return out, err


def myprint(string: str, list_widget: QtWidgets.QListWidget = None):
    if len(string) is not 0:
        print(list_widget)
        if list_widget is None:
            print(string)
        else:
            print(1)
            list_widget.addItem(string)
