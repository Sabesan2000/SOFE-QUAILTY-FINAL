# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\100707158\Documents\calibre-master\calibre-master\src\calibre\gui2\lrf_renderer\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 701)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("viewer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.stack = QtWidgets.QStackedWidget(self.central_widget)
        self.stack.setObjectName("stack")
        self.viewer_page = QtWidgets.QWidget()
        self.viewer_page.setObjectName("viewer_page")
        self.gridlayout = QtWidgets.QGridLayout(self.viewer_page)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setObjectName("gridlayout")
        self.graphics_view = BookView(self.viewer_page)
        self.graphics_view.setMouseTracking(True)
        self.graphics_view.setObjectName("graphics_view")
        self.gridlayout.addWidget(self.graphics_view, 0, 0, 1, 1)
        self.stack.addWidget(self.viewer_page)
        self.bar_page = QtWidgets.QWidget()
        self.bar_page.setObjectName("bar_page")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.bar_page)
        self.vboxlayout1.setObjectName("vboxlayout1")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.frame_2 = QtWidgets.QFrame(self.bar_page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.progress_bar = QtWidgets.QProgressBar(self.frame_2)
        self.progress_bar.setMaximum(0)
        self.progress_bar.setProperty("value", -1)
        self.progress_bar.setObjectName("progress_bar")
        self.vboxlayout2.addWidget(self.progress_bar)
        self.progress_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.progress_label.setFont(font)
        self.progress_label.setObjectName("progress_label")
        self.vboxlayout2.addWidget(self.progress_label)
        self.vboxlayout1.addWidget(self.frame_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem1)
        self.stack.addWidget(self.bar_page)
        self.vboxlayout.addWidget(self.stack)
        MainWindow.setCentralWidget(self.central_widget)
        self.tool_bar = QtWidgets.QToolBar(MainWindow)
        self.tool_bar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.tool_bar.setObjectName("tool_bar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.tool_bar)
        self.action_next_page = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(I("next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_next_page.setIcon(icon1)
        self.action_next_page.setObjectName("action_next_page")
        self.action_previous_page = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(I("previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_previous_page.setIcon(icon2)
        self.action_previous_page.setObjectName("action_previous_page")
        self.action_back = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(I("back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_back.setIcon(icon3)
        self.action_back.setObjectName("action_back")
        self.action_forward = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(I("forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_forward.setIcon(icon4)
        self.action_forward.setObjectName("action_forward")
        self.action_next_match = QtWidgets.QAction(MainWindow)
        self.action_next_match.setObjectName("action_next_match")
        self.action_open_ebook = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(I("document_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_ebook.setIcon(icon5)
        self.action_open_ebook.setObjectName("action_open_ebook")
        self.action_configure = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(I("config.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_configure.setIcon(icon6)
        self.action_configure.setObjectName("action_configure")
        self.tool_bar.addAction(self.action_back)
        self.tool_bar.addAction(self.action_forward)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.action_open_ebook)
        self.tool_bar.addAction(self.action_configure)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.action_previous_page)
        self.tool_bar.addAction(self.action_next_page)
        self.tool_bar.addSeparator()

        self.retranslateUi(MainWindow)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_("LRF viewer"))
        self.progress_label.setText(_("Parsing LRF file"))
        self.tool_bar.setWindowTitle(_("LRF viewer toolbar"))
        self.action_next_page.setText(_("Next page"))
        self.action_previous_page.setText(_("Previous Page"))
        self.action_back.setText(_("Back"))
        self.action_forward.setText(_("Forward"))
        self.action_next_match.setText(_("Next match"))
        self.action_open_ebook.setText(_("Open e-book"))
        self.action_configure.setText(_("Configure"))
from calibre.gui2.lrf_renderer.bookview import BookView

