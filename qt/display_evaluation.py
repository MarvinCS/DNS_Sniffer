# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display_evaluation.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 640)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 881, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gv_image = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.gv_image.setObjectName("gv_image")
        self.verticalLayout.addWidget(self.gv_image)
        self.btn_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_refresh.setObjectName("btn_refresh")
        self.verticalLayout.addWidget(self.btn_refresh)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_refresh.setText(_translate("Dialog", "Refresh"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
