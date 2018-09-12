import os
import time
from config import Config


def now():
    """Returns the current time"""
    return str((time.strftime('%Y-%m-%d %H:%M:%S')))


def executeAndSleep(command: str, _time=1):
    """Executes the given bash-command and sleeps for the specified time"""
    os.system(command)
    time.sleep(_time)


def myprint(string: str):
    """Prints string to stdout, if I am not using a gui. Otherwise it's printed to the gui's log-widget"""
    if len(string) is not 0:
        if Config._log_window is None:
            print(string)
        else:
            Config._log_window.addItem(string)
