import os
import time

from PyQt5 import QtWidgets

from config import Config


def now():
    return str((time.strftime('%Y-%m-%d %H:%M:%S')))


def executeAndSleep(command: str, _time=1):
    os.system(command)
    time.sleep(_time)


def myprint(string: str):
    "Prints string to stdout, if I am not using a gui"
    if len(string) is not 0:
        if Config._log_window is None:
            print(string)
        else:
            Config._log_window.addItem(string)
