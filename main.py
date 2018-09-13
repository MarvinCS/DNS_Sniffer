import sys
from time import sleep
from PyQt5 import QtWidgets

from config import Config
from qt.main_window import Ui_MainWindow
from visualisation import Pie_Chart
from action import ACTION, getAction
from network import Network


def scan():
    """Starts scanning for dns-packages"""
    try:
        Network.startMonitorMode()
        Network.captureDNS()
    except KeyboardInterrupt:
        print("Abort...")
    finally:
        Network.stopMonitorMode()
    exit(1)


def interfaceToMonitorMode():
    """Set interface to monitor-mode"""
    try:
        Network.startMonitorMode()
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("Abort...")
    finally:
        Network.stopMonitorMode()
    exit(1)


def gui():
    """Creats the gui's main-window"""
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.init(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    Config.parse_config()
    action = getAction()
    if action == ACTION.SCAN:
        scan()
    elif action == ACTION.INTERFACE:
        interfaceToMonitorMode()
    elif action == ACTION.EVALUATE:
        Pie_Chart.plotAllInOne()
    elif action == ACTION.GUI:
        gui()
