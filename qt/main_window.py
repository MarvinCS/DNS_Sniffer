# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from network import *
from qt.options_dialog import Options_dialog
from visualisation import plotAllInOne


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(556, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 150, 541, 351))
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
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.tv_server = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tv_server.setObjectName("tv_server")
        self.tv_server.setColumnCount(0)
        self.tv_server.setRowCount(0)
        self.horizontalLayout.addWidget(self.tv_server)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 130, 541, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 541, 122))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lv_log = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.lv_log.setObjectName("lv_log")
        self.horizontalLayout_2.addWidget(self.lv_log)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_start = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout.addWidget(self.btn_start)
        self.btn_refresh = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_refresh.setObjectName("btn_refresh")
        self.verticalLayout.addWidget(self.btn_refresh)
        self.btn_options = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_options.setObjectName("btn_options")
        self.verticalLayout.addWidget(self.btn_options)
        self.btn_evaluate = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_evaluate.setObjectName("btn_evaluate")
        self.verticalLayout.addWidget(self.btn_evaluate)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lv_log, self.btn_start)
        MainWindow.setTabOrder(self.btn_start, self.btn_refresh)
        MainWindow.setTabOrder(self.btn_refresh, self.btn_options)
        MainWindow.setTabOrder(self.btn_options, self.btn_evaluate)
        MainWindow.setTabOrder(self.btn_evaluate, self.tv_domains)
        MainWindow.setTabOrder(self.tv_domains, self.tv_server)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_refresh.setText(_translate("MainWindow", "Refresh"))
        self.btn_options.setText(_translate("MainWindow", "Options"))
        self.btn_evaluate.setText(_translate("MainWindow", "Evaluate"))

    def init_buttons(self):
        self.btn_start.clicked.connect(self.on_click_start)
        self.btn_refresh.clicked.connect(self.on_click_refresh)
        self.btn_options.clicked.connect(self.on_click_options)
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

    def on_click_options(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Options_dialog()
        self.ui.setupUi(self.dialog)
        self.ui.insert_data()
        self.dialog.show()

    def on_click_evaluate(self):
        plotAllInOne()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.init_buttons()
    ui.init_tables()
    MainWindow.show()
    sys.exit(app.exec_())
