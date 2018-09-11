# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from config import Config
from qt.add_domain import Add_domain
from qt.interface_chooser import Choose_interface_dialog


class Options_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 344)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 310, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_database = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_database.setObjectName("lbl_database")
        self.verticalLayout.addWidget(self.lbl_database)
        self.lbl_channel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_channel.setObjectName("lbl_channel")
        self.verticalLayout.addWidget(self.lbl_channel)
        self.lbl_interface = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_interface.setObjectName("lbl_interface")
        self.verticalLayout.addWidget(self.lbl_interface)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ti_db_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ti_db_name.setObjectName("ti_db_name")
        self.verticalLayout_2.addWidget(self.ti_db_name)
        self.ti_channel = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ti_channel.setObjectName("ti_channel")
        self.verticalLayout_2.addWidget(self.ti_channel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ti_interface = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ti_interface.setObjectName("ti_interface")
        self.horizontalLayout_2.addWidget(self.ti_interface)
        self.btn_choose_interface = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_choose_interface.setObjectName("btn_choose_interface")
        self.horizontalLayout_2.addWidget(self.btn_choose_interface)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 100, 461, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 120, 461, 181))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lv_domains = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.lv_domains.setObjectName("lv_domains")
        item = QtWidgets.QListWidgetItem()
        self.lv_domains.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lv_domains.addItem(item)
        self.horizontalLayout_3.addWidget(self.lv_domains)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_add_domain = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_add_domain.setObjectName("btn_add_domain")
        self.verticalLayout_4.addWidget(self.btn_add_domain)
        self.btn_remove_domain = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_remove_domain.setObjectName("btn_remove_domain")
        self.verticalLayout_4.addWidget(self.btn_remove_domain)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.ti_channel, self.ti_interface)
        Dialog.setTabOrder(self.ti_interface, self.btn_choose_interface)
        Dialog.setTabOrder(self.btn_choose_interface, self.lv_domains)
        Dialog.setTabOrder(self.lv_domains, self.btn_add_domain)
        Dialog.setTabOrder(self.btn_add_domain, self.btn_remove_domain)
        self.save_dialog = Dialog

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_database.setText(_translate("Dialog", "Database"))
        self.lbl_channel.setText(_translate("Dialog", "Channel:"))
        self.lbl_interface.setText(_translate("Dialog", "Interface:"))
        self.btn_choose_interface.setText(_translate("Dialog", "Choose"))
        __sortingEnabled = self.lv_domains.isSortingEnabled()
        self.lv_domains.setSortingEnabled(False)
        item = self.lv_domains.item(0)
        item.setText(_translate("Dialog", "test1"))
        item = self.lv_domains.item(1)
        item.setText(_translate("Dialog", "test2"))
        self.lv_domains.setSortingEnabled(__sortingEnabled)
        self.btn_add_domain.setText(_translate("Dialog", "Add"))
        self.btn_remove_domain.setText(_translate("Dialog", "Remove"))

    def __save(self):
        channel = self.ti_channel.text()
        interface = str(self.ti_interface.text())
        db_name = str(self.ti_db_name.text())
        Config.channel = channel if len(str(channel)) is not 0 else None
        Config.interface = interface if len(interface) is not 0 else None
        Config.db_name = db_name if len(str(db_name)) is not 0 else None
        Config.save()
        self.save_dialog.accept()

    def __add_domain(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Add_domain()
        self.ui.setupUi(self.dialog)
        self.ui.init_buttons(self)
        self.dialog.show()

    def __remove_domain(self):
        selected = self.lv_domains.selectedItems()
        for domain in selected:
            Config.excluded_domains.remove(str(domain.text()))
        self.load_domains()

    def __choose_interface(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Choose_interface_dialog()
        self.ui.setupUi(self.dialog)
        self.ui.init_buttons(self)
        self.dialog.show()

    def insert_data(self):
        if Config.db_name is not None:
            self.ti_db_name.setText(str(Config.db_name))
        if Config.channel is not None:
            self.ti_channel.setText(str(Config.channel))
        if Config.interface is not None:
            self.ti_interface.setText(str(Config.interface))
        self.load_domains()

    def load_domains(self):
        self.lv_domains.clear()
        for domain in Config.excluded_domains:
            self.lv_domains.addItem(str(domain))

    def init__buttons(self):
        self.buttonBox.accepted.connect(self.__save)
        self.btn_add_domain.clicked.connect(self.__add_domain)
        self.btn_remove_domain.clicked.connect(self.__remove_domain)
        self.btn_choose_interface.clicked.connect(self.__choose_interface)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Options_dialog()
    ui.setupUi(Dialog)
    ui.insert_data()
    Dialog.show()
    sys.exit(app.exec_())
