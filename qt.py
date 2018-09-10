# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItem

from db import DB_Connector
from PyQt5.QtCore import pyqtSlot, QRect, QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QListView, QHBoxLayout, QApplication, QDialog, QLayout, \
    QTableWidget, QTableWidgetItem, QHeaderView, QListWidget
from network import *
from visualisation import plotAllInOne


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 500)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(440, 10, 111, 120))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout.addWidget(self.btn_start)
        self.btn_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_refresh.setObjectName("btn_refresh")
        self.verticalLayout.addWidget(self.btn_refresh)
        self.btn_options = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_options.setObjectName("btn_options")
        self.verticalLayout.addWidget(self.btn_options)
        self.btn_evaluate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_evaluate.setObjectName("btn_evaluate")
        self.verticalLayout.addWidget(self.btn_evaluate)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 411, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lv_log = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.lv_log.setObjectName("lv_log")
        self.verticalLayout_2.addWidget(self.lv_log)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 139, 541, 351))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tv_domains = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tv_domains.setObjectName("tv_domains")
        self.tv_domains.setColumnCount(0)
        self.tv_domains.setRowCount(0)
        self.horizontalLayout.addWidget(self.tv_domains)
        self.tv_server = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tv_server.setObjectName("tv_server")
        self.tv_server.setColumnCount(0)
        self.tv_server.setRowCount(0)
        self.horizontalLayout.addWidget(self.tv_server)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_start.setText(_translate("Dialog", "Start"))
        self.btn_refresh.setText(_translate("Dialog", "Refresh"))
        self.btn_options.setText(_translate("Dialog", "Options"))
        self.btn_evaluate.setText(_translate("Dialog", "Evaluate"))

    def init_buttons(self):
        self.btn_start.clicked.connect(self.on_click_start)
        self.btn_refresh.clicked.connect(self.on_click_refresh)
        self.btn_evaluate.clicked.connect(self.on_click_evaluate)

    def init_tables(self):
        self.tv_domains.setRowCount(0)
        self.tv_domains.setColumnCount(2)
        self.tv_domains.setHorizontalHeaderLabels(["domain", "count"])
        self.tv_server.setRowCount(0)
        self.tv_server.setColumnCount(2)
        self.tv_server.setHorizontalHeaderLabels(["server", "count"])

    def on_click_start(self):
        if Config.interface is None:
            self.lv_log.addItem("Please press the \"Option\"-button and set an interface")
            return
        if self.btn_start.text() == "Start":
            self.btn_start.setText("Stop")
            startMonitorMode()
            captureDNS()
        elif self.btn_start.text() == "Stop":
            self.btn_start.setText("Start")
            stopMonitorMode()

    def on_click_refresh(self):
        dbc = DB_Connector.getInstance()
        domains = dbc.getDomains()
        self.tv_domains.setRowCount(len(domains))
        counter = 0
        for domain in domains:
            self.tv_domains.setItem(counter, 0, QTableWidgetItem(domain[0]))
            self.tv_domains.setItem(counter, 1, QTableWidgetItem(str(domain[1])))
            counter += 1

        server = dbc.getTopTenDNSServer()
        self.tv_server.setRowCount(len(server))
        counter = 0
        for s in server:
            self.tv_server.setItem(counter, 0, QTableWidgetItem(s[0]))
            self.tv_server.setItem(counter, 1, QTableWidgetItem(str(s[1])))
            counter += 1

    def on_click_evaluate(self):
        plotAllInOne()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.init_buttons()
    ui.init_tables()
    Dialog.show()
    sys.exit(app.exec_())
