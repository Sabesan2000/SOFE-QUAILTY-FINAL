# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\100707158\Documents\calibre-master\calibre-master\src\calibre\gui2\preferences\metadata_sources.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(733, 673)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stack = QtWidgets.QStackedWidget(Form)
        self.stack.setObjectName("stack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.sources_view = QtWidgets.QTableView(self.groupBox)
        self.sources_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.sources_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sources_view.setObjectName("sources_view")
        self.verticalLayout_3.addWidget(self.sources_view)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.configure_plugin_button = QtWidgets.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("plugins.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.configure_plugin_button.setIcon(icon)
        self.configure_plugin_button.setObjectName("configure_plugin_button")
        self.verticalLayout_3.addWidget(self.configure_plugin_button)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fields_view = QtWidgets.QListView(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fields_view.sizePolicy().hasHeightForWidth())
        self.fields_view.setSizePolicy(sizePolicy)
        self.fields_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.fields_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.fields_view.setFlow(QtWidgets.QListView.LeftToRight)
        self.fields_view.setProperty("isWrapping", True)
        self.fields_view.setResizeMode(QtWidgets.QListView.Adjust)
        self.fields_view.setObjectName("fields_view")
        self.gridLayout_2.addWidget(self.fields_view, 0, 0, 1, 2)
        self.select_all_button = QtWidgets.QPushButton(self.groupBox_2)
        self.select_all_button.setObjectName("select_all_button")
        self.gridLayout_2.addWidget(self.select_all_button, 1, 0, 1, 1)
        self.clear_all_button = QtWidgets.QPushButton(self.groupBox_2)
        self.clear_all_button.setObjectName("clear_all_button")
        self.gridLayout_2.addWidget(self.clear_all_button, 1, 1, 1, 1)
        self.select_default_button = QtWidgets.QPushButton(self.groupBox_2)
        self.select_default_button.setObjectName("select_default_button")
        self.gridLayout_2.addWidget(self.select_default_button, 2, 0, 1, 1)
        self.set_as_default_button = QtWidgets.QPushButton(self.groupBox_2)
        self.set_as_default_button.setObjectName("set_as_default_button")
        self.gridLayout_2.addWidget(self.set_as_default_button, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 356, 462))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.opt_txt_comments = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.opt_txt_comments.setObjectName("opt_txt_comments")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.opt_txt_comments)
        self.opt_swap_author_names = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.opt_swap_author_names.setObjectName("opt_swap_author_names")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.opt_swap_author_names)
        self.opt_append_comments = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.opt_append_comments.setObjectName("opt_append_comments")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.opt_append_comments)
        self.opt_keep_dups = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.opt_keep_dups.setObjectName("opt_keep_dups")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.opt_keep_dups)
        self.opt_fewer_tags = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.opt_fewer_tags.setObjectName("opt_fewer_tags")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.opt_fewer_tags)
        self.tag_map_rules_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tag_map_rules_button.setObjectName("tag_map_rules_button")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.tag_map_rules_button)
        self.author_map_rules_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.author_map_rules_button.setObjectName("author_map_rules_button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.author_map_rules_button)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.opt_max_tags = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.opt_max_tags.setObjectName("opt_max_tags")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.opt_max_tags)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.opt_wait_after_first_identify_result = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.opt_wait_after_first_identify_result.setObjectName("opt_wait_after_first_identify_result")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.opt_wait_after_first_identify_result)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.opt_wait_after_first_cover_result = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.opt_wait_after_first_cover_result.setObjectName("opt_wait_after_first_cover_result")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.opt_wait_after_first_cover_result)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.stack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stack.addWidget(self.page_2)
        self.gridLayout_3.addWidget(self.stack, 0, 0, 1, 1)
        self.label_2.setBuddy(self.opt_max_tags)
        self.label_3.setBuddy(self.opt_wait_after_first_identify_result)
        self.label_4.setBuddy(self.opt_wait_after_first_cover_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Metadata sources"))
        self.label.setText(_("Disable any metadata sources you do not want by unchecking them. You can also set the cover priority. Covers from sources that have a higher (smaller) priority will be preferred when bulk downloading metadata."))
        self.label_5.setText(_("Sources with a red X next to their names must be configured before they will be used. "))
        self.configure_plugin_button.setText(_("C&onfigure selected source"))
        self.groupBox_2.setTitle(_("Metadata fields to download"))
        self.fields_view.setToolTip(_("If you uncheck any fields, metadata for those fields will not be downloaded"))
        self.select_all_button.setText(_("&Select all"))
        self.clear_all_button.setText(_("Sele&ct none"))
        self.select_default_button.setToolTip(_("Restore your own subset of checked fields that you define using the \'Set as default\' button"))
        self.select_default_button.setText(_("Select &default"))
        self.set_as_default_button.setToolTip(_("Store the currently checked fields as the default, you can quickly apply the default using the \'Select default\' button"))
        self.set_as_default_button.setText(_("&Set as default"))
        self.opt_txt_comments.setText(_("Convert all downloaded comments to plain &text"))
        self.opt_swap_author_names.setText(_("Swap &author names from FN LN to LN, FN"))
        self.opt_append_comments.setToolTip(_("<p>When downloading comments, append the downloaded comments to any existing comment, instead of overwriting them."))
        self.opt_append_comments.setStatusTip(_("When downloading comments, append the downloaded comments to any existing comment, instead of overwriting them."))
        self.opt_append_comments.setText(_("Append comments to &existing"))
        self.opt_keep_dups.setToolTip(_("<p>Normally, the metadata download system will keep only a single result per metadata source. This option will cause it to keep all results returned from every metadata source. Useful if you only use one or two sources and want to select individual results from them by hand. Note that result with identical title/author/identifiers are still merged."))
        self.opt_keep_dups.setText(_("Keep more than one entry per source"))
        self.opt_fewer_tags.setToolTip(_("<p>Different metadata sources have different sets of tags for the same book. If this option is checked, then calibre will use the smaller tag sets. These tend to be more like genres, while the larger tag sets tend to describe the books content.\n"
"<p>Note that this option will only make a practical difference if one of the metadata sources has a genre like tag set for the book you are searching for. Most often, they all have large tag sets."))
        self.opt_fewer_tags.setStatusTip(_("Prefer smaller tag sets when picking tags from different metadata sources"))
        self.opt_fewer_tags.setText(_("Prefer &fewer tags"))
        self.tag_map_rules_button.setText(_("Create &rules to filter/transform tags"))
        self.author_map_rules_button.setText(_("Create rules to &transform author names"))
        self.label_2.setText(_("Max. &number of tags to download:"))
        self.label_3.setText(_("Max. &time to wait after first match is found:"))
        self.opt_wait_after_first_identify_result.setSuffix(_(" secs"))
        self.label_4.setText(_("Max. time to wait after first &cover is found:"))
        self.opt_wait_after_first_cover_result.setSuffix(_(" secs"))
