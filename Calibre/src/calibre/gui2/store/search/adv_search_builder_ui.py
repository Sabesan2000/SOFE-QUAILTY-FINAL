# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ravee\Desktop\calibre-master\src\calibre\gui2\store\search\adv_search_builder.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(752, 472)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.matchkind = QtWidgets.QComboBox(Dialog)
        self.matchkind.setObjectName("matchkind")
        self.matchkind.addItem("")
        self.matchkind.addItem("")
        self.matchkind.addItem("")
        self.gridLayout_2.addWidget(self.matchkind, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.all = QtWidgets.QLineEdit(self.groupBox)
        self.all.setObjectName("all")
        self.horizontalLayout.addWidget(self.all)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.phrase = QtWidgets.QLineEdit(self.groupBox)
        self.phrase.setObjectName("phrase")
        self.horizontalLayout_2.addWidget(self.phrase)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.any = QtWidgets.QLineEdit(self.groupBox)
        self.any.setObjectName("any")
        self.horizontalLayout_3.addWidget(self.any)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.none = QtWidgets.QLineEdit(self.groupBox_2)
        self.none.setObjectName("none")
        self.horizontalLayout_4.addWidget(self.none)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.sh_label = QtWidgets.QLabel(self.groupBox_2)
        self.sh_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.sh_label.setOpenExternalLinks(True)
        self.sh_label.setObjectName("sh_label")
        self.verticalLayout_2.addWidget(self.sh_label)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tab)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_11)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.title_box = EnLineEdit(self.tab_2)
        self.title_box.setObjectName("title_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.title_box)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.author_box = EnLineEdit(self.tab_2)
        self.author_box.setObjectName("author_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.author_box)
        self.price_label = QtWidgets.QLabel(self.tab_2)
        self.price_label.setObjectName("price_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.price_label)
        self.price_box = EnLineEdit(self.tab_2)
        self.price_box.setObjectName("price_box")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.price_box)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.format_box = QtWidgets.QLineEdit(self.tab_2)
        self.format_box.setObjectName("format_box")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.format_box)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.drm_combo = QtWidgets.QComboBox(self.tab_2)
        self.drm_combo.setObjectName("drm_combo")
        self.drm_combo.addItem("")
        self.drm_combo.setItemText(0, "")
        self.drm_combo.addItem("")
        self.drm_combo.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.drm_combo)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.download_combo = QtWidgets.QComboBox(self.tab_2)
        self.download_combo.setObjectName("download_combo")
        self.download_combo.addItem("")
        self.download_combo.setItemText(0, "")
        self.download_combo.addItem("")
        self.download_combo.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.download_combo)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.affiliate_combo = QtWidgets.QComboBox(self.tab_2)
        self.affiliate_combo.setObjectName("affiliate_combo")
        self.affiliate_combo.addItem("")
        self.affiliate_combo.setItemText(0, "")
        self.affiliate_combo.addItem("")
        self.affiliate_combo.addItem("")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.affiliate_combo)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clear_button = QtWidgets.QPushButton(self.tab_2)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_6.addWidget(self.clear_button)
        self.tab_2_button_box = QtWidgets.QDialogButtonBox(self.tab_2)
        self.tab_2_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.tab_2_button_box.setObjectName("tab_2_button_box")
        self.horizontalLayout_6.addWidget(self.tab_2_button_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 2)
        self.label_5.setBuddy(self.matchkind)
        self.label.setBuddy(self.all)
        self.label_2.setBuddy(self.all)
        self.label_3.setBuddy(self.all)
        self.label_4.setBuddy(self.all)
        self.label_7.setBuddy(self.title_box)
        self.label_8.setBuddy(self.author_box)
        self.price_label.setBuddy(self.price_box)
        self.label_10.setBuddy(self.format_box)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.all, self.phrase)
        Dialog.setTabOrder(self.phrase, self.any)
        Dialog.setTabOrder(self.any, self.none)
        Dialog.setTabOrder(self.none, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.title_box)
        Dialog.setTabOrder(self.title_box, self.author_box)
        Dialog.setTabOrder(self.author_box, self.price_box)
        Dialog.setTabOrder(self.price_box, self.format_box)
        Dialog.setTabOrder(self.format_box, self.clear_button)
        Dialog.setTabOrder(self.clear_button, self.tab_2_button_box)
        Dialog.setTabOrder(self.tab_2_button_box, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.matchkind)

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(_("Advanced search"))
        self.label_5.setText(_("&What kind of match to use:"))
        self.matchkind.setItemText(0, _("Contains: the word or phrase matches anywhere in the metadata field"))
        self.matchkind.setItemText(1, _("Equals: the word or phrase must match the entire metadata field"))
        self.matchkind.setItemText(2, _("Regular expression: the expression must match anywhere in the metadata field"))
        self.groupBox.setTitle(_("Find entries that have..."))
        self.label.setText(_("&All these words:"))
        self.label_2.setText(_("This exact &phrase:"))
        self.label_3.setText(_("&One or more of these words:"))
        self.groupBox_2.setTitle(_("But don\'t show entries that have..."))
        self.label_4.setText(_("Any of these &unwanted words:"))
        self.sh_label.setText(_("See the <a href=\"%s\">User Manual</a> for more help"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("A&dvanced search"))
        self.label_11.setText(_("Search only in specific fields:"))
        self.label_7.setText(_("&Title:"))
        self.title_box.setToolTip(_("Enter the title."))
        self.label_8.setText(_("&Author:"))
        self.price_label.setText(_("&Price:"))
        self.label_10.setText(_("&Format:"))
        self.label_13.setText(_("DRM:"))
        self.drm_combo.setItemText(1, _("true"))
        self.drm_combo.setItemText(2, _("false"))
        self.label_12.setText(_("Download:"))
        self.download_combo.setItemText(1, _("true"))
        self.download_combo.setItemText(2, _("false"))
        self.label_9.setText(_("Affiliate:"))
        self.affiliate_combo.setItemText(1, _("true"))
        self.affiliate_combo.setItemText(2, _("false"))
        self.clear_button.setText(_("&Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("Titl&e/author/price..."))
from calibre.gui2.widgets import EnLineEdit

