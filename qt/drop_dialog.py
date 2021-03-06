# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drop_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from db import Connection_handler
from qt.drop_error_dialog import Drop_Error_Dialog


class Drop_DB_Dialog(object):
    def setupUi(self, Dialog):
        """Creates the ui. Mostly autogenerated"""
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 110)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 70, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lbl_text = QtWidgets.QLabel(Dialog)
        self.lbl_text.setGeometry(QtCore.QRect(10, 10, 301, 51))
        self.lbl_text.setScaledContents(False)
        self.lbl_text.setWordWrap(True)
        self.lbl_text.setObjectName("lbl_text")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """Autogenerated function to retranslate the ui"""
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_text.setText(
            _translate("Dialog", "Do you really want to drop the database? All data will be lost forever!"))

    def init(self, Dialog):
        """Init the ui"""
        self.dialog = Dialog
        self.setupUi(Dialog)
        self.buttonBox.accepted.connect(self.drop_db)

    def drop_db(self):
        """Trys to drop the database"""
        dropped = Connection_handler.drop_database()
        if not dropped:
            self.show_error()

    def show_error(self):
        """Shows an error-dialog"""
        self.drop_dialog = QtWidgets.QDialog()
        self.ui = Drop_Error_Dialog()
        self.ui.setupUi(self.drop_dialog)
        self.drop_dialog.show()
