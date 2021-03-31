# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\100707158\Documents\calibre-master\calibre-master\src\calibre\gui2\catalog\catalog_epub_mobi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(742, 663)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 740, 661))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.catalogPresets = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catalogPresets.sizePolicy().hasHeightForWidth())
        self.catalogPresets.setSizePolicy(sizePolicy)
        self.catalogPresets.setObjectName("catalogPresets")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.catalogPresets)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.preset_field = QtWidgets.QComboBox(self.catalogPresets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_field.sizePolicy().hasHeightForWidth())
        self.preset_field.setSizePolicy(sizePolicy)
        self.preset_field.setObjectName("preset_field")
        self.horizontalLayout_9.addWidget(self.preset_field)
        self.preset_save_pb = QtWidgets.QPushButton(self.catalogPresets)
        self.preset_save_pb.setObjectName("preset_save_pb")
        self.horizontalLayout_9.addWidget(self.preset_save_pb)
        self.preset_delete_pb = QtWidgets.QPushButton(self.catalogPresets)
        self.preset_delete_pb.setObjectName("preset_delete_pb")
        self.horizontalLayout_9.addWidget(self.preset_delete_pb)
        self.verticalLayout_2.addWidget(self.catalogPresets)
        self.includedSections = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.includedSections.sizePolicy().hasHeightForWidth())
        self.includedSections.setSizePolicy(sizePolicy)
        self.includedSections.setMinimumSize(QtCore.QSize(0, 0))
        self.includedSections.setObjectName("includedSections")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.includedSections)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.generate_authors = QtWidgets.QCheckBox(self.includedSections)
        self.generate_authors.setEnabled(True)
        self.generate_authors.setChecked(False)
        self.generate_authors.setObjectName("generate_authors")
        self.gridLayout_2.addWidget(self.generate_authors, 0, 0, 1, 1)
        self.generate_titles = QtWidgets.QCheckBox(self.includedSections)
        self.generate_titles.setObjectName("generate_titles")
        self.gridLayout_2.addWidget(self.generate_titles, 2, 0, 1, 1)
        self.generate_series = QtWidgets.QCheckBox(self.includedSections)
        self.generate_series.setObjectName("generate_series")
        self.gridLayout_2.addWidget(self.generate_series, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.generate_genres = QtWidgets.QCheckBox(self.includedSections)
        self.generate_genres.setObjectName("generate_genres")
        self.horizontalLayout_2.addWidget(self.generate_genres)
        self.genre_source_field = QtWidgets.QComboBox(self.includedSections)
        self.genre_source_field.setObjectName("genre_source_field")
        self.horizontalLayout_2.addWidget(self.genre_source_field)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.generate_recently_added = QtWidgets.QCheckBox(self.includedSections)
        self.generate_recently_added.setMinimumSize(QtCore.QSize(0, 26))
        self.generate_recently_added.setObjectName("generate_recently_added")
        self.horizontalLayout_5.addWidget(self.generate_recently_added)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.generate_descriptions = QtWidgets.QCheckBox(self.includedSections)
        self.generate_descriptions.setMinimumSize(QtCore.QSize(0, 26))
        self.generate_descriptions.setObjectName("generate_descriptions")
        self.horizontalLayout_7.addWidget(self.generate_descriptions)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 4, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.includedSections)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 0, 1, 5, 1)
        self.line_5 = QtWidgets.QFrame(self.includedSections)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 1, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.includedSections)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 1, 2, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.includedSections)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 3, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.includedSections)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_2.addWidget(self.line_8, 3, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.includedSections)
        self.prefix_rules_gb = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefix_rules_gb.sizePolicy().hasHeightForWidth())
        self.prefix_rules_gb.setSizePolicy(sizePolicy)
        self.prefix_rules_gb.setObjectName("prefix_rules_gb")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.prefix_rules_gb)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addWidget(self.prefix_rules_gb)
        self.exclusion_rules_gb = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exclusion_rules_gb.sizePolicy().hasHeightForWidth())
        self.exclusion_rules_gb.setSizePolicy(sizePolicy)
        self.exclusion_rules_gb.setMinimumSize(QtCore.QSize(0, 0))
        self.exclusion_rules_gb.setObjectName("exclusion_rules_gb")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.exclusion_rules_gb)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.exclusion_rules_gb)
        self.excludedGenres = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excludedGenres.sizePolicy().hasHeightForWidth())
        self.excludedGenres.setSizePolicy(sizePolicy)
        self.excludedGenres.setMinimumSize(QtCore.QSize(0, 0))
        self.excludedGenres.setObjectName("excludedGenres")
        self.gridLayout = QtWidgets.QGridLayout(self.excludedGenres)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.excludedGenres)
        self.label.setMinimumSize(QtCore.QSize(175, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.exclude_genre = QtWidgets.QLineEdit(self.excludedGenres)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exclude_genre.sizePolicy().hasHeightForWidth())
        self.exclude_genre.setSizePolicy(sizePolicy)
        self.exclude_genre.setMinimumSize(QtCore.QSize(0, 0))
        self.exclude_genre.setToolTip("")
        self.exclude_genre.setObjectName("exclude_genre")
        self.gridLayout.addWidget(self.exclude_genre, 0, 1, 1, 1)
        self.reset_exclude_genres_tb = QtWidgets.QToolButton(self.excludedGenres)
        self.reset_exclude_genres_tb.setObjectName("reset_exclude_genres_tb")
        self.gridLayout.addWidget(self.reset_exclude_genres_tb, 0, 2, 1, 1)
        self.regex_results_label = QtWidgets.QLabel(self.excludedGenres)
        self.regex_results_label.setMinimumSize(QtCore.QSize(175, 0))
        self.regex_results_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.regex_results_label.setTextFormat(QtCore.Qt.AutoText)
        self.regex_results_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.regex_results_label.setWordWrap(True)
        self.regex_results_label.setObjectName("regex_results_label")
        self.gridLayout.addWidget(self.regex_results_label, 1, 0, 1, 1)
        self.exclude_genre_results = QtWidgets.QLabel(self.excludedGenres)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exclude_genre_results.sizePolicy().hasHeightForWidth())
        self.exclude_genre_results.setSizePolicy(sizePolicy)
        self.exclude_genre_results.setMinimumSize(QtCore.QSize(0, 0))
        self.exclude_genre_results.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exclude_genre_results.setText("")
        self.exclude_genre_results.setTextFormat(QtCore.Qt.PlainText)
        self.exclude_genre_results.setWordWrap(True)
        self.exclude_genre_results.setObjectName("exclude_genre_results")
        self.gridLayout.addWidget(self.exclude_genre_results, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.excludedGenres)
        self.otherOptions = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otherOptions.sizePolicy().hasHeightForWidth())
        self.otherOptions.setSizePolicy(sizePolicy)
        self.otherOptions.setMinimumSize(QtCore.QSize(0, 0))
        self.otherOptions.setObjectName("otherOptions")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.otherOptions)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.merge_with_comments_hl = QtWidgets.QHBoxLayout()
        self.merge_with_comments_hl.setObjectName("merge_with_comments_hl")
        self.merge_source_field = QtWidgets.QComboBox(self.otherOptions)
        self.merge_source_field.setMinimumSize(QtCore.QSize(0, 0))
        self.merge_source_field.setObjectName("merge_source_field")
        self.merge_with_comments_hl.addWidget(self.merge_source_field)
        self.line_2 = QtWidgets.QFrame(self.otherOptions)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.merge_with_comments_hl.addWidget(self.line_2)
        self.merge_before = QtWidgets.QRadioButton(self.otherOptions)
        self.merge_before.setObjectName("merge_before")
        self.merge_options_bg = QtWidgets.QButtonGroup(Form)
        self.merge_options_bg.setObjectName("merge_options_bg")
        self.merge_options_bg.addButton(self.merge_before)
        self.merge_with_comments_hl.addWidget(self.merge_before)
        self.merge_after = QtWidgets.QRadioButton(self.otherOptions)
        self.merge_after.setObjectName("merge_after")
        self.merge_options_bg.addButton(self.merge_after)
        self.merge_with_comments_hl.addWidget(self.merge_after)
        self.line = QtWidgets.QFrame(self.otherOptions)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.merge_with_comments_hl.addWidget(self.line)
        self.include_hr = QtWidgets.QCheckBox(self.otherOptions)
        self.include_hr.setObjectName("include_hr")
        self.merge_with_comments_hl.addWidget(self.include_hr)
        self.gridLayout_3.addLayout(self.merge_with_comments_hl, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.otherOptions)
        self.label_9.setMinimumSize(QtCore.QSize(175, 0))
        self.label_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.otherOptions)
        self.label_4.setMinimumSize(QtCore.QSize(175, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.replace_cover_hl = QtWidgets.QHBoxLayout()
        self.replace_cover_hl.setObjectName("replace_cover_hl")
        self.generate_new_cover = QtWidgets.QRadioButton(self.otherOptions)
        self.generate_new_cover.setChecked(True)
        self.generate_new_cover.setObjectName("generate_new_cover")
        self.cover_options_bg = QtWidgets.QButtonGroup(Form)
        self.cover_options_bg.setObjectName("cover_options_bg")
        self.cover_options_bg.addButton(self.generate_new_cover)
        self.replace_cover_hl.addWidget(self.generate_new_cover)
        self.use_existing_cover = QtWidgets.QRadioButton(self.otherOptions)
        self.use_existing_cover.setObjectName("use_existing_cover")
        self.cover_options_bg.addButton(self.use_existing_cover)
        self.replace_cover_hl.addWidget(self.use_existing_cover)
        self.spacer_label = QtWidgets.QLabel(self.otherOptions)
        self.spacer_label.setText("")
        self.spacer_label.setObjectName("spacer_label")
        self.replace_cover_hl.addWidget(self.spacer_label)
        self.gridLayout_3.addLayout(self.replace_cover_hl, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.otherOptions)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_note_source_field = QtWidgets.QComboBox(self.otherOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_note_source_field.sizePolicy().hasHeightForWidth())
        self.header_note_source_field.setSizePolicy(sizePolicy)
        self.header_note_source_field.setMinimumSize(QtCore.QSize(0, 0))
        self.header_note_source_field.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.header_note_source_field.setObjectName("header_note_source_field")
        self.horizontalLayout.addWidget(self.header_note_source_field)
        self.line_4 = QtWidgets.QFrame(self.otherOptions)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.label_10 = QtWidgets.QLabel(self.otherOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.thumb_width = QtWidgets.QDoubleSpinBox(self.otherOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumb_width.sizePolicy().hasHeightForWidth())
        self.thumb_width.setSizePolicy(sizePolicy)
        self.thumb_width.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.thumb_width.setDecimals(2)
        self.thumb_width.setMinimum(1.0)
        self.thumb_width.setMaximum(5.0)
        self.thumb_width.setSingleStep(0.1)
        self.thumb_width.setObjectName("thumb_width")
        self.horizontalLayout.addWidget(self.thumb_width)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.otherOptions)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.cross_references_hl = QtWidgets.QHBoxLayout()
        self.cross_references_hl.setObjectName("cross_references_hl")
        self.cross_reference_authors = QtWidgets.QCheckBox(self.otherOptions)
        self.cross_reference_authors.setObjectName("cross_reference_authors")
        self.cross_references_hl.addWidget(self.cross_reference_authors)
        self.gridLayout_3.addLayout(self.cross_references_hl, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.otherOptions)
        self.horizontalLayout_11.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_10.addWidget(self.scrollArea)
        self.label.setBuddy(self.exclude_genre)
        self.regex_results_label.setBuddy(self.exclude_genre)
        self.label_9.setBuddy(self.merge_source_field)
        self.label_3.setBuddy(self.header_note_source_field)
        self.label_10.setBuddy(self.merge_source_field)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.catalogPresets.setTitle(_("Presets"))
        self.preset_field.setToolTip(_("Select catalog preset to load"))
        self.preset_save_pb.setToolTip(_("Save current catalog settings as preset"))
        self.preset_save_pb.setText(_("Save"))
        self.preset_delete_pb.setToolTip(_("Delete current preset"))
        self.preset_delete_pb.setText(_("Delete"))
        self.includedSections.setToolTip(_("Enabled sections will be included in the generated catalog."))
        self.includedSections.setTitle(_("Included sections"))
        self.generate_authors.setToolTip(_("List of books, sorted by Author"))
        self.generate_authors.setText(_("&Authors"))
        self.generate_titles.setToolTip(_("List of books, sorted by Title"))
        self.generate_titles.setText(_("&Titles"))
        self.generate_series.setToolTip(_("List of series books, sorted by Series"))
        self.generate_series.setText(_("&Series"))
        self.generate_genres.setToolTip(_("List of books, sorted by genre"))
        self.generate_genres.setText(_("&Genres"))
        self.genre_source_field.setToolTip(_("Field containing genres"))
        self.generate_recently_added.setToolTip(_("List of books, sorted by date added to calibre"))
        self.generate_recently_added.setText(_("&Recently added"))
        self.generate_descriptions.setToolTip(_("Individual descriptions of books with cover thumbs, sorted by author"))
        self.generate_descriptions.setText(_("&Descriptions"))
        self.prefix_rules_gb.setToolTip(_("The first matching prefix rule applies a prefix to book listings in the generated catalog."))
        self.prefix_rules_gb.setTitle(_("Prefixes"))
        self.exclusion_rules_gb.setToolTip(_("Books matching any of the exclusion rules will be excluded from the generated catalog. "))
        self.exclusion_rules_gb.setTitle(_("Excluded books"))
        self.excludedGenres.setToolTip(_("A regular expression describing genres to be excluded from the generated catalog. Genres are derived from the tags applied to your books.\n"
"The default pattern \\[.+\\]|\\+ excludes tags of the form [tag], e.g., [Test book], and \'+\', the default tag for a read book."))
        self.excludedGenres.setTitle(_("Excluded genres"))
        self.label.setText(_("Genres to &exclude (regex):"))
        self.reset_exclude_genres_tb.setToolTip(_("Reset to default"))
        self.reset_exclude_genres_tb.setText(_("..."))
        self.regex_results_label.setText(_("Results of regex:"))
        self.exclude_genre_results.setToolTip(_("Tags that will be excluded as genres"))
        self.otherOptions.setTitle(_("Other options"))
        self.merge_source_field.setToolTip(_("Custom column containing additional content to be merged with comments metadata in the descriptions section."))
        self.merge_before.setToolTip(_("Merge additional content before comments in descriptions section."))
        self.merge_before.setText(_("&Before"))
        self.merge_after.setToolTip(_("Merge additional content after comments in descriptions section."))
        self.merge_after.setText(_("&After"))
        self.include_hr.setToolTip(_("Separate comments metadata and additional content with a horizontal rule in the descriptions section."))
        self.include_hr.setText(_("Include &separator"))
        self.label_9.setText(_("&Merge with comments:"))
        self.label_4.setText(_("Catalog cover:"))
        self.generate_new_cover.setText(_("Generate new cover"))
        self.use_existing_cover.setText(_("Use existing cover"))
        self.label_3.setText(_("E&xtra Description note:"))
        self.header_note_source_field.setToolTip(_("Custom column source for text to include in Descriptions section."))
        self.label_10.setText(_("&Thumb width:"))
        self.thumb_width.setToolTip(_("Size hint for cover thumbnails included in Descriptions section."))
        self.thumb_width.setSuffix(_(" inch"))
        self.label_2.setText(_("Author cross-references:"))
        self.cross_reference_authors.setText(_("For books with multiple authors, list each author separately"))
