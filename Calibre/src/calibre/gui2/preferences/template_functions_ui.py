# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ravee\Desktop\calibre-master\src\calibre\gui2\preferences\template_functions.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(788, 663)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = ScrollingTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout1 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout1.setObjectName("gridLayout1")
        self.st_textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.st_textBrowser.setMaximumSize(QtCore.QSize(16777215, 75))
        self.st_textBrowser.setObjectName("st_textBrowser")
        self.gridLayout1.addWidget(self.st_textBrowser, 0, 0, 1, 2)
        self.template_editor = EmbeddedTemplateDialog(self.tab)
        self.template_editor.setObjectName("template_editor")
        self.gridLayout1.addWidget(self.template_editor, 3, 1, 1, 1)
        self.st_button_layout = QtWidgets.QVBoxLayout()
        self.st_button_layout.setObjectName("st_button_layout")
        self.st_clear_button = QtWidgets.QPushButton(self.tab)
        self.st_clear_button.setObjectName("st_clear_button")
        self.st_button_layout.addWidget(self.st_clear_button)
        self.st_delete_button = QtWidgets.QPushButton(self.tab)
        self.st_delete_button.setObjectName("st_delete_button")
        self.st_button_layout.addWidget(self.st_delete_button)
        self.st_replace_button = QtWidgets.QPushButton(self.tab)
        self.st_replace_button.setObjectName("st_replace_button")
        self.st_button_layout.addWidget(self.st_replace_button)
        self.st_create_button = QtWidgets.QPushButton(self.tab)
        self.st_create_button.setObjectName("st_create_button")
        self.st_button_layout.addWidget(self.st_create_button)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.st_button_layout.addItem(spacerItem)
        self.gridLayout1.addLayout(self.st_button_layout, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout2 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout2.setObjectName("gridLayout2")
        self.line = QtWidgets.QFrame(self.tab1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout2.addWidget(self.line, 1, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.function_name = QtWidgets.QComboBox(self.tab1)
        self.function_name.setEditable(True)
        self.function_name.setObjectName("function_name")
        self.gridLayout_3.addWidget(self.function_name, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab1)
        self.label_3.setToolTip("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.argument_count = QtWidgets.QSpinBox(self.tab1)
        self.argument_count.setMinimum(-1)
        self.argument_count.setObjectName("argument_count")
        self.gridLayout_3.addWidget(self.argument_count, 1, 1, 1, 1)
        self.documentation = QtWidgets.QTextEdit(self.tab1)
        self.documentation.setObjectName("documentation")
        self.gridLayout_3.addWidget(self.documentation, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab1)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clear_button = QtWidgets.QPushButton(self.tab1)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_2.addWidget(self.clear_button)
        self.delete_button = QtWidgets.QPushButton(self.tab1)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_2.addWidget(self.delete_button)
        self.replace_button = QtWidgets.QPushButton(self.tab1)
        self.replace_button.setObjectName("replace_button")
        self.horizontalLayout_2.addWidget(self.replace_button)
        self.create_button = QtWidgets.QPushButton(self.tab1)
        self.create_button.setObjectName("create_button")
        self.horizontalLayout_2.addWidget(self.create_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout1 = QtWidgets.QVBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.label_41 = QtWidgets.QLabel(self.tab1)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout1.addWidget(self.label_41)
        self.program = QtWidgets.QPlainTextEdit(self.tab1)
        self.program.setMinimumSize(QtCore.QSize(400, 0))
        self.program.setDocumentTitle("")
        self.program.setTabStopWidth(30)
        self.program.setObjectName("program")
        self.horizontalLayout1.addWidget(self.program)
        self.horizontalLayout.addLayout(self.horizontalLayout1)
        self.gridLayout2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab1)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout2.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab1, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.label_2.setBuddy(self.function_name)
        self.label_3.setBuddy(self.argument_count)
        self.label_4.setBuddy(self.documentation)
        self.label_41.setBuddy(self.program)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.st_clear_button.setText(_("&Clear"))
        self.st_delete_button.setText(_("D&elete"))
        self.st_replace_button.setText(_("&Replace"))
        self.st_create_button.setText(_("C&reate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("&Stored Templates"))
        self.label_2.setText(_("F&unction:"))
        self.function_name.setToolTip(_("Enter the name of the function to create."))
        self.label_3.setText(_("Argument &count:"))
        self.argument_count.setToolTip(_("Set this to -1 if the function takes a variable number of arguments"))
        self.label_4.setText(_("D&ocumentation:"))
        self.clear_button.setText(_("Clear"))
        self.delete_button.setText(_("Delete"))
        self.replace_button.setText(_("Replace"))
        self.create_button.setText(_("C&reate"))
        self.label_41.setText(_("P&rogram code (Follow Python indenting rules):"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _("&Template Functions"))
from calibre.gui2.dialogs.template_dialog import EmbeddedTemplateDialog
from calibre.gui2.widgets2 import ScrollingTabWidget
