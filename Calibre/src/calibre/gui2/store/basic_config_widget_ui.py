# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\100707158\Documents\calibre-master\calibre-master\src\calibre\gui2\store\basic_config_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(460, 69)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.tags = QtWidgets.QLineEdit(Form)
        self.tags.setObjectName("tags")
        self.gridLayout.addWidget(self.tags, 1, 1, 1, 1)
        self.open_external = QtWidgets.QCheckBox(Form)
        self.open_external.setObjectName("open_external")
        self.gridLayout.addWidget(self.open_external, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.label.setText(_("Added tags:"))
        self.open_external.setText(_("Open store in external web browser"))