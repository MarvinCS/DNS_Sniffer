from time import sleep

from network import *
from qt.main_window import Ui_MainWindow
from visualisation import plotAllInOne
from action import ACTION, getAction


def scan():
    try:
        startMonitorMode()
        captureDNS()
    except KeyboardInterrupt:
        print("Abort...")
    finally:
        stopMonitorMode()
    exit(1)


def interfaceToMonitorMode():
    try:
        startMonitorMode()
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("Abort...")
    finally:
        stopMonitorMode()
    exit(1)


def gui():
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
        plotAllInOne()
    elif action == ACTION.GUI:
        print(Config.db_name)
        gui()
