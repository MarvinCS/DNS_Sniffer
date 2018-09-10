from time import sleep

from PyQt5.QtWidgets import QApplication, QDialog

from network import *
from qt import Ui_Dialog
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
        app = QApplication(sys.argv)
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.init_buttons()
        ui.init_tables()
        Dialog.show()
        sys.exit(app.exec_())
