# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ravee\Desktop\calibre-master\src\calibre\gui2\store\config\search\search_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(465, 396)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.opt_timeout = QtWidgets.QSpinBox(self.groupBox)
        self.opt_timeout.setMinimum(1)
        self.opt_timeout.setObjectName("opt_timeout")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.opt_timeout)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.opt_hang_time = QtWidgets.QSpinBox(self.groupBox)
        self.opt_hang_time.setMinimum(1)
        self.opt_hang_time.setMaximum(99)
        self.opt_hang_time.setSingleStep(1)
        self.opt_hang_time.setProperty("value", 1)
        self.opt_hang_time.setObjectName("opt_hang_time")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.opt_hang_time)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.opt_max_results = QtWidgets.QSpinBox(self.groupBox_2)
        self.opt_max_results.setMinimum(1)
        self.opt_max_results.setObjectName("opt_max_results")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.opt_max_results)
        self.opt_open_external = QtWidgets.QCheckBox(self.groupBox_2)
        self.opt_open_external.setObjectName("opt_open_external")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.opt_open_external)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.opt_search_thread_count = QtWidgets.QSpinBox(self.groupBox_3)
        self.opt_search_thread_count.setMinimum(1)
        self.opt_search_thread_count.setObjectName("opt_search_thread_count")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.opt_search_thread_count)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.opt_cache_thread_count = QtWidgets.QSpinBox(self.groupBox_3)
        self.opt_cache_thread_count.setMinimum(1)
        self.opt_cache_thread_count.setObjectName("opt_cache_thread_count")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.opt_cache_thread_count)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.opt_cover_thread_count = QtWidgets.QSpinBox(self.groupBox_3)
        self.opt_cover_thread_count.setMinimum(1)
        self.opt_cover_thread_count.setObjectName("opt_cover_thread_count")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.opt_cover_thread_count)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.opt_details_thread_count = QtWidgets.QSpinBox(self.groupBox_3)
        self.opt_details_thread_count.setMinimum(1)
        self.opt_details_thread_count.setObjectName("opt_details_thread_count")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.opt_details_thread_count)
        self.verticalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Time"))
        self.label.setText(_("Number of seconds to wait for a store to respond:"))
        self.label_2.setText(_("Number of seconds to let a store process results:"))
        self.groupBox_2.setTitle(_("Display"))
        self.label_3.setText(_("Maximum number of results to show per store:"))
        self.opt_open_external.setText(_("Open search result in system browser"))
        self.groupBox_3.setTitle(_("Threads"))
        self.label_4.setText(_("Number of search threads to use:"))
        self.label_5.setText(_("Number of cache update threads to use:"))
        self.label_6.setText(_("Number of cover download threads to use:"))
        self.label_7.setText(_("Number of details threads to use:"))
