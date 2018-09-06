import os
import time


def now():
    return str((time.strftime('%Y-%m-%d %H:%M:%S')))


def executeAndSleep(command: str, time=1):
    os.system(command)
    time.sleep(time)
