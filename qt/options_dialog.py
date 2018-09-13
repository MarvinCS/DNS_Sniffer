# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QLineEdit

from config import Config
from qt.add_domain import Add_domain
from qt.drop_dialog import Drop_DB_Dialog
from qt.interface_chooser import Choose_interface_dialog


class Options_dialog(object):
    def setupUi(self, Dialog):
        """Creates the ui. Mostly autogenerated"""
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 430)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 381, 461, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 155))
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
        self.lbl_auto_update = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_auto_update.setObjectName("lbl_auto_update")
        self.verticalLayout.addWidget(self.lbl_auto_update)
        self.lbl_subdomains = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_subdomains.setObjectName("lbl_subdomains")
        self.verticalLayout.addWidget(self.lbl_subdomains)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ti_db_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ti_db_name.setObjectName("ti_db_name")
        self.horizontalLayout_4.addWidget(self.ti_db_name)
        self.btn_clear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_4.addWidget(self.btn_clear)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
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
        self.ti_auto_update = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ti_auto_update.setObjectName("ti_auto_update")
        self.verticalLayout_2.addWidget(self.ti_auto_update)
        self.cb_subdomains = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.cb_subdomains.setObjectName("cb_subdomains")
        self.verticalLayout_2.addWidget(self.cb_subdomains)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 160, 461, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 190, 461, 181))
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
        Dialog.setTabOrder(self.btn_choose_interface, self.lv_domains)
        Dialog.setTabOrder(self.lv_domains, self.btn_remove_domain)

    def retranslateUi(self, Dialog):
        """Autogenerated function to retranslate the ui"""
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Options"))
        self.lbl_database.setText(_translate("Dialog", "Database:"))
        self.lbl_channel.setText(_translate("Dialog", "Channel:"))
        self.lbl_interface.setText(_translate("Dialog", "Interface:"))
        self.lbl_auto_update.setText(_translate("Dialog", "Auto-update:"))
        self.lbl_subdomains.setText(_translate("Dialog", "Subdomains:"))
        self.btn_clear.setText(_translate("Dialog", "Clear DB"))
        self.btn_choose_interface.setText(_translate("Dialog", "Choose"))
        self.cb_subdomains.setText(_translate("Dialog", "Remove subdomains from scanned urls"))
        self.btn_add_domain.setText(_translate("Dialog", "Add"))
        self.btn_remove_domain.setText(_translate("Dialog", "Remove"))
        # IMPORTANT
        self.save_dialog = Dialog

    def init(self, Dialog):
        """Init the ui"""
        self.setupUi(Dialog)
        self.init_buttons()
        self.insert_data()
        self.load_domains()
        self.__db_exists()
        self.ti_db_name.editingFinished.connect(self.__db_exists)

    def __db_exists(self):
        """Enables/disables the 'drop db' button, if there is no database with db typed (line edit) name"""
        input = self.ti_db_name.text().strip().lower()
        if not input.endswith(".db"):
            input += ".db"
            self.ti_db_name.setText(input)
        filename = "%s/%s" % (Config.project_path, input)
        self.btn_clear.setDisabled(Config._scanning_thread or not os.path.isfile(filename))

    def init_buttons(self):
        """Initialises the functionality of all buttons"""
        self.buttonBox.accepted.connect(self.__save)
        self.btn_add_domain.clicked.connect(self.__add_domain)
        self.btn_remove_domain.clicked.connect(self.__remove_domain)
        self.btn_choose_interface.clicked.connect(self.__choose_interface)
        self.btn_choose_interface.setDisabled(Config._scanning_thread)
        self.btn_clear.clicked.connect(self.__ask_drop_db)
        self.btn_clear.setDisabled(Config._scanning_thread)

    def __ask_drop_db(self):
        """Opens a new dialog and asks if you really want to drop the db"""
        Config.db_name = self.ti_db_name.text()
        self.drop_dialog = QtWidgets.QDialog()
        self.ui = Drop_DB_Dialog()
        self.ui.init(self.drop_dialog)
        self.drop_dialog.show()

    def __save(self):
        """Saves the configuration to the config.json-file"""
        channel = self.ti_channel.text()
        interface = str(self.ti_interface.text())
        db_name = str(self.ti_db_name.text())
        auto_update = self.ti_auto_update.text()
        Config.channel = channel if len(str(channel).strip()) is not 0 else None
        Config.interface = interface if len(interface) is not 0 else None
        Config.db_name = db_name if len(str(db_name).strip()) is not 0 else None
        Config.update_interval = auto_update if len(str(auto_update).strip()) is not 0 else None
        Config.subdomains = not self.cb_subdomains.isChecked()
        Config.save()
        self.save_dialog.accept()

    def __add_domain(self):
        """Creates a new dialog to add an domain to the 'excluded'-list"""
        self.dialog = QtWidgets.QDialog()
        self.ui = Add_domain()
        self.ui.setupUi(self.dialog)
        self.ui.init_buttons(self)
        self.dialog.show()

    def __remove_domain(self):
        """Removes the selected domain from the 'excluded'-list"""
        selected = self.lv_domains.selectedItems()
        for domain in selected:
            Config.excluded_domains.remove(str(domain.text()))
        self.load_domains()

    def __choose_interface(self):
        """Creates a new dialog to choose a network-interface"""
        self.dialog = QtWidgets.QDialog()
        self.ui = Choose_interface_dialog()
        self.ui.setupUi(self.dialog)
        self.ui.init_buttons(self)
        self.dialog.show()

    def insert_data(self):
        """Insert the data from config-class into the gui's formulas"""
        if Config.db_name is not None:
            self.ti_db_name.setText(str(Config.db_name))
            self.ti_db_name.setDisabled(Config._scanning_thread)
        if Config.channel is not None:
            self.ti_channel.setText(str(Config.channel))
            self.ti_channel.setDisabled(Config._scanning_thread)
        if Config.interface is not None:
            self.ti_interface.setText(str(Config.interface))
            self.ti_interface.setDisabled(Config._scanning_thread)
        if Config.update_interval is not None:
            self.ti_auto_update.setText(str(Config.update_interval))
        self.cb_subdomains.setChecked(not Config.subdomains)

    def load_domains(self):
        """Loads and displays all domains in the 'excluded'-list"""
        self.lv_domains.clear()
        for domain in Config.excluded_domains:
            self.lv_domains.addItem(str(domain))
