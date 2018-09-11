# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_chooser.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from config import Config


class Choose_interface_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(211, 248)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lv_interfaces = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lv_interfaces.setObjectName("lv_interfaces")
        self.verticalLayout.addWidget(self.lv_interfaces)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.dialog = Dialog
        self.__list_interfaces()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def init_buttons(self, old_dialog):
        self.old_dialog = old_dialog
        self.buttonBox.accepted.connect(self.__choose_interface)

    def __choose_interface(self):
        interface = self.lv_interfaces.selectedItems()[0].text()
        Config.interface = interface
        self.old_dialog.ti_interface.setText(str(Config.interface))
        self.dialog.accept()

    def __list_interfaces(self):
        interfaces = str(os.popen('ifconfig -a | sed \'s/[ \t].*//;/^\(lo\|\)$/d\'').read()).splitlines()
        for interface in interfaces:
            self.lv_interfaces.addItem(interface[0:-1])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Choose_interface_dialog()
    ui.setupUi(Dialog)
    ui.list_interfaces()
    Dialog.show()
    sys.exit(app.exec_())
