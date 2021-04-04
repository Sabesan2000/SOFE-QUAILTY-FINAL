# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ravee\Desktop\calibre-master\src\calibre\gui2\convert\debug.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(436, 382)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.button_debug_dir = QtWidgets.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("document_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_debug_dir.setIcon(icon)
        self.button_debug_dir.setObjectName("button_debug_dir")
        self.gridLayout.addWidget(self.button_debug_dir, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.opt_debug_pipeline = QtWidgets.QLineEdit(Form)
        self.opt_debug_pipeline.setClearButtonEnabled(True)
        self.opt_debug_pipeline.setObjectName("opt_debug_pipeline")
        self.gridLayout.addWidget(self.opt_debug_pipeline, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.button_debug_dir.setToolTip(_("Choose debug folder"))
        self.button_debug_dir.setText(_("..."))
        self.label.setText(_("Choose a folder to put the debug output into. If you specify a folder, calibre will place a lot of debug output into it. This will be useful in understanding the conversion process and figuring out the correct values for conversion parameters like Table of Contents and Chapter detection."))
        self.label_2.setText(_("The debug process outputs the intermediate HTML generated at various stages of the conversion process. This HTML can sometimes serve as a good starting point for hand editing a conversion."))

