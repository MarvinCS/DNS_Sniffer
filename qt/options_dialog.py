# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from config import Config


class Options_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 368)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 330, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_channel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_channel.setObjectName("lbl_channel")
        self.verticalLayout.addWidget(self.lbl_channel)
        self.lbl_interface = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_interface.setObjectName("lbl_interface")
        self.verticalLayout.addWidget(self.lbl_interface)
        self.lbl_update_interval = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_update_interval.setObjectName("lbl_update_interval")
        self.verticalLayout.addWidget(self.lbl_update_interval)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.ti_update_interval = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ti_update_interval.setObjectName("ti_update_interval")
        self.verticalLayout_2.addWidget(self.ti_update_interval)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 120, 461, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 140, 461, 181))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lv_domains = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.lv_domains.setObjectName("lv_domains")
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
        Dialog.setTabOrder(self.btn_choose_interface, self.ti_update_interval)
        Dialog.setTabOrder(self.ti_update_interval, self.lv_domains)
        Dialog.setTabOrder(self.lv_domains, self.btn_add_domain)
        Dialog.setTabOrder(self.btn_add_domain, self.btn_remove_domain)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_channel.setText(_translate("Dialog", "Channel:"))
        self.lbl_interface.setText(_translate("Dialog", "Interface:"))
        self.lbl_update_interval.setText(_translate("Dialog", "Auto-Update:"))
        self.btn_choose_interface.setText(_translate("Dialog", "Choose"))
        self.btn_add_domain.setText(_translate("Dialog", "Add"))
        self.btn_remove_domain.setText(_translate("Dialog", "Remove"))

    def insert_data(self):
        if Config.channel is not None:
            self.ti_channel.setText(str(Config.channel))
        if Config.interface is not None:
            self.ti_interface.setText(str(Config.interface))
        if Config.update_interval is not None:
            self.ti_update_interval.setText(str(Config.update_interval))
        for domain in Config.excluded_domains:
            self.lv_domains.addItem(str(domain))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Options_dialog()
    ui.setupUi(Dialog)
    ui.insert_data()
    Dialog.show()
    sys.exit(app.exec_())
