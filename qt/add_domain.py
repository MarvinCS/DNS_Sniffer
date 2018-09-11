# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_domain.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from config import Config


class Add_domain(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(331, 111)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_domain_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_domain_name.setObjectName("lbl_domain_name")
        self.horizontalLayout.addWidget(self.lbl_domain_name)
        self.ti_domain_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ti_domain_name.setObjectName("ti_domain_name")
        self.horizontalLayout.addWidget(self.ti_domain_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btns = QtWidgets.QHBoxLayout()
        self.btns.setObjectName("btns")
        self.btn_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btns.addWidget(self.btn_cancel)
        self.btn_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_save.setObjectName("btn_save")
        self.btns.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.btns)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.ti_domain_name, self.btn_save)
        Dialog.setTabOrder(self.btn_save, self.btn_cancel)
        self.dialog = Dialog

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_domain_name.setText(_translate("Dialog", "Domain"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))
        self.btn_save.setText(_translate("Dialog", "Save"))

    def init_buttons(self, dialog):
        self.old_dialog = dialog
        self.btn_cancel.clicked.connect(self.dialog.reject)
        self.btn_save.clicked.connect(self.__save)

    def __save(self):
        domain = str(self.ti_domain_name.text()).strip()
        Config.excluded_domains.append(domain)
        self.dialog.accept()
        self.old_dialog.load_domains()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Add_domain()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
