import os
import time
from enum import Enum


def now():
    return str((time.strftime('%Y-%m-%d %H:%M:%S')))


def executeAndSleep(command: str, _time=1):
    os.system(command)
    time.sleep(_time)
