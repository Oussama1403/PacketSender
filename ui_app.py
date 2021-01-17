# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 562)
        MainWindow.setStyleSheet("/*\n"
"Material Dark Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Inspired on https://github.com/jxfwinter/qt-material-stylesheet\n"
"Company: GTRONICK\n"
"Last updated: 04/12/2018, 15:00.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/MaterialDark.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:#f3f3f3;\n"
"}\n"
"QDialog {\n"
"    background-color:#f3f3f3;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#f3f3f3;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#f3f3f3;\n"
"    \n"
"    border-style: solid;\n"
"    border-color: #919191;\n"
"\n"
"    border-width: 1px;\n"
"    color: #545454;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#007b50;\n"
"    background-color:#f3f3f3;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #545454;\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    \n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 4px;\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    color: #545454;\n"
"    padding: 2px;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: inset;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-width: 1px;\n"
"    color: #393947;\n"
"    padding: 2px;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #545454;\n"
"    padding: 2px;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #545454;\n"
"    padding-bottom: 1px;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: #37efba;\n"
"    border-right-color: #37efba;\n"
"    border-left-color: #37efba;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #545454;\n"
"    padding-bottom: 2px;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #37efba;\n"
"    padding-bottom: 1px;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #808086;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding-bottom: 1px;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px;\n"
"    border-color: #919191;\n"
"    border-style: solid;\n"
"    padding: 0 8px;\n"
"    color: #545454;\n"
"    background:#f3f3f3;\n"
"    selection-background-color:#007b50;\n"
"    selection-color: #f3f3f3;\n"
"}\n"
"QLabel {\n"
"    color: #545454;\n"
"}\n"
"QLCDNumber {\n"
"    color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#f3f3f3;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #04b97f;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"  background-color: #f3f3f3;\n"
"  padding: 2px;\n"
"  \n"
"  color: #545454;\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"  border: 1px solid #009dff;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background: transparent;\n"
"  padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  padding: 4px;\n"
"  background: transparent;\n"
"  border: 0px solid #32414B;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  padding: 4px;\n"
"  border: 0px solid #37efba;\n"
"  background-color: #37efba;\n"
"  color: rgb(50, 51, 75);\n"
"  margin-bottom: 0px;\n"
"  padding-bottom: 0px;\n"
"}\n"
"\n"
"/* QMenu ------------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenu\n"
"{\n"
"    background-color: #f3f3f3;\n"
"    border: 1px solid #4a5157;\n"
"    padding: 10px;\n"
"    color: #545454;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"    min-width: 200px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"       background-color: #242424;\n"
"    height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #37efba;\n"
"    border: #37efba;\n"
"    color: rgb(49, 49, 66);\n"
"\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#f3f3f3;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#f3f3f3;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #f3f3f3;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #545454;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#f3f3f3;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #545454;\n"
"    background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #545454;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #545454;\n"
"    background-color: #f3f3f3;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #545454;\n"
"    background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #545454;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #545454;    \n"
"    background-color: #f3f3f3;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #545454;    \n"
"    background-color: #f3f3f3;\n"
"}\n"
"QTimeEdit {\n"
"    color: #545454;    \n"
"    background-color: #f3f3f3;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #545454;    \n"
"    background-color: #f3f3f3;\n"
"}\n"
"QDateEdit {\n"
"    color: #545454;    \n"
"    background-color: #f3f3f3;\n"
"}\n"
"QComboBox {\n"
"    color: #545454;    \n"
"    background: #f3f3f3;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #f3f3f3;\n"
"    color: #545454;\n"
"    selection-background-color: #f3f3f3;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: #545454;    \n"
"    background: #f3f3f3;\n"
"    selection-color: #f3f3f3;\n"
"    selection-background-color: #f3f3f3;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #545454;    \n"
"    background: #f3f3f3;\n"
"}\n"
"QFontComboBox {\n"
"    color: #545454;    \n"
"    background-color: #f3f3f3;\n"
"}\n"
"QToolBox {\n"
"    color: #545454;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #545454;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #f3f3f3;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QScrollArea {\n"
"    color: #f3f3f3;\n"
"    background-color: #f3f3f3;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_ip = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_ip.sizePolicy().hasHeightForWidth())
        self.search_ip.setSizePolicy(sizePolicy)
        self.search_ip.setMinimumSize(QtCore.QSize(151, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.search_ip.setFont(font)
        self.search_ip.setObjectName("search_ip")
        self.horizontalLayout.addWidget(self.search_ip)
        self.dos_attack = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dos_attack.sizePolicy().hasHeightForWidth())
        self.dos_attack.setSizePolicy(sizePolicy)
        self.dos_attack.setMinimumSize(QtCore.QSize(151, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.dos_attack.setFont(font)
        self.dos_attack.setObjectName("dos_attack")
        self.horizontalLayout.addWidget(self.dos_attack)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(301, 17))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(10, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(301, 17))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.selected_ip = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_ip.sizePolicy().hasHeightForWidth())
        self.selected_ip.setSizePolicy(sizePolicy)
        self.selected_ip.setMinimumSize(QtCore.QSize(580, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.selected_ip.setFont(font)
        self.selected_ip.setText("")
        self.selected_ip.setObjectName("selected_ip")
        self.verticalLayout.addWidget(self.selected_ip)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.action_info = QtWidgets.QTextEdit(self.centralwidget)
        self.action_info.setObjectName("action_info")
        self.verticalLayout.addWidget(self.action_info)
        self.cancel_op = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_op.sizePolicy().hasHeightForWidth())
        self.cancel_op.setSizePolicy(sizePolicy)
        self.cancel_op.setMinimumSize(QtCore.QSize(50, 40))
        self.cancel_op.setMaximumSize(QtCore.QSize(150, 70))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cancel_op.setFont(font)
        self.cancel_op.setObjectName("cancel_op")
        self.verticalLayout.addWidget(self.cancel_op)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 28))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BS-PacketSender"))
        self.search_ip.setText(_translate("MainWindow", "Search IPs"))
        self.dos_attack.setText(_translate("MainWindow", "DOS attack"))
        self.label_3.setText(_translate("MainWindow", "Connected IPs in your network:"))
        self.label_4.setText(_translate("MainWindow", "Select Port:"))
        self.label_2.setText(_translate("MainWindow", "Selected IP:"))
        self.label.setText(_translate("MainWindow", "Action Information:"))
        self.cancel_op.setText(_translate("MainWindow", "Cancel operation"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
