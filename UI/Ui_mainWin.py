# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1063, 727)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ico/数据.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget{background-color: #212121;}\n"
"\n"
"QTableWidget{\n"
"color:#DCDCDC;\n"
"background:#444444;\n"
"border:1px solid #242424;\n"
"alternate-background-color:#525252;/*交错颜色*/\n"
"gridline-color:#242424;\n"
"}\n"
"\n"
"/*选中item*/\n"
"QTableWidget::item:selected{\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);\n"
"}\n"
"\n"
"/*\n"
"悬浮item*/\n"
"QTableWidget::item:hover{\n"
"background:#5B5B5B;\n"
"}\n"
"/*表头*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"background:#5E5E5E;\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#DCDCDC;\n"
"border:1px solid #242424;\n"
"border-left-width:0;\n"
"}\n"
"\n"
"/*表右侧的滑条*/\n"
"QScrollBar:vertical{\n"
"background:#484848;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"/*滑块*/\n"
"QScrollBar::handle:vertical{\n"
"background:#CCCCCC;\n"
"}\n"
"/*\n"
"滑块悬浮，按下*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:#A7A7A7;\n"
"}\n"
"/*\n"
"滑块已经划过的区域*/\n"
"QScrollBar::sub-page:vertical{\n"
"background:444444;\n"
"}\n"
"\n"
"/*\n"
"滑块还没有划过的区域*/\n"
"QScrollBar::add-page:vertical{\n"
"background:5B5B5B;\n"
"}\n"
"\n"
"/*页面下移的按钮*/\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"/*页面上移的按钮*/\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"QGroupBox{\n"
"background-color:rgb(80, 80, 80);color:white;border-radius: 5px;border: 1px solid rgb(255, 170, 0);margin-top: 5px;\n"
"}\n"
"QGroupBox::title{top:-5px;left:10px;}\n"
"QlistWidget{background-color: rgb(68, 68, 68);color:white;}\n"
"QGroupBox QWidget{background-color: rgb(80, 80, 80);color:white;}\n"
"QTextBrowser{background-color: rgb(68, 68, 68);}\n"
"QLabel{color:white;}\n"
"QPushButton{border-radius: 10px;}\n"
"QPushButton:hover{\n"
"color:black;\n"
"background-color: rgb(150, 150, 150);\n"
"}")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setStyleSheet("#tabWidget>QWidget>QWidget{/*tab页*/\n"
"background-color: rgb(80, 80, 80);\n"
"}\n"
"#tabWidget::tab-bar{\n"
"alignment:left;/*tab位置*/\n"
"}\n"
"#tabWidget::pane { /*内容区域*/\n"
"background-color: rgb(80, 80, 80);/*背景色-空隙颜色*/\n"
"\n"
"} \n"
"#tabWidget QTabBar{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"#tabWidget QTabBar::tab{/*页签*/\n"
"min-height:20px;\n"
"width:120px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"margin-right:1px;\n"
"margin-bottom:1px;\n"
"background-color:rgb(80, 80, 80);\n"
"}\n"
"#tabWidget QTabBar::tab:hover{\n"
"color:black;\n"
"background-color: rgb(255, 170, 0);\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"#tabWidget QTabBar::tab:selected{\n"
"color:rgb(255, 170, 0);\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"#tabWidget QTabBar::tab:selected:hover{\n"
"color:black;\n"
"}\n"
"#tabWidget QTabBar::tear{/*选项过多时的。。。*/\n"
"imag:;\n"
"}\n"
"#tabWidget QTabBar::scroller{\n"
"width:60px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setMinimumSize(QtCore.QSize(0, 100))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.spinBox_thread = QtWidgets.QSpinBox(self.widget)
        self.spinBox_thread.setMinimum(1)
        self.spinBox_thread.setProperty("value", 1)
        self.spinBox_thread.setObjectName("spinBox_thread")
        self.verticalLayout_2.addWidget(self.spinBox_thread)
        self.verticalLayout_3.addWidget(self.widget)
        self.pushButton_run = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_run.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_run.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_run.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/img/13.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_run.setIcon(icon1)
        self.pushButton_run.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_run.setObjectName("pushButton_run")
        self.verticalLayout_3.addWidget(self.pushButton_run, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_stop.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_stop.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/img/12.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_stop.setIcon(icon2)
        self.pushButton_stop.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout_3.addWidget(self.pushButton_stop, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_5.addWidget(self.textBrowser)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_9.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border: 1px solid rgb(255, 170, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(40,40,40);\n"
"}\n"
"QLineEdit:focus{border: 2px solid rgb(255, 170, 0)}")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_9.addWidget(self.lineEdit)
        self.pushButton_search = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_search.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_search.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_search.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/img/17.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search.setIcon(icon3)
        self.pushButton_search.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_search.setObjectName("pushButton_search")
        self.verticalLayout_9.addWidget(self.pushButton_search, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.pushButton_info = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_info.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_info.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_info.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/img/14.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_info.setIcon(icon4)
        self.pushButton_info.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_info.setObjectName("pushButton_info")
        self.verticalLayout_4.addWidget(self.pushButton_info, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_del = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_del.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_del.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setIcon(icon3)
        self.pushButton_del.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_del.setObjectName("pushButton_del")
        self.verticalLayout_4.addWidget(self.pushButton_del, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_clear.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_clear.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/img/16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_clear.setIcon(icon5)
        self.pushButton_clear.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout_4.addWidget(self.pushButton_clear, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "英雄数据库"))
        self.groupBox_2.setTitle(_translate("Form", "爬虫程序"))
        self.label_4.setText(_translate("Form", "线程数量："))
        self.pushButton_run.setText(_translate("Form", "运行"))
        self.pushButton_stop.setText(_translate("Form", "停止"))
        self.groupBox.setTitle(_translate("Form", "运行日志"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "数据抓取"))
        self.groupBox_3.setTitle(_translate("Form", "查询数据"))
        self.pushButton_search.setText(_translate("Form", "搜索"))
        self.pushButton_info.setText(_translate("Form", "查看"))
        self.pushButton_del.setText(_translate("Form", "删除"))
        self.pushButton_clear.setText(_translate("Form", "清空"))
        self.groupBox_4.setTitle(_translate("Form", "英雄数据库"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "选择"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "头像"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "英雄"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "地区"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "数据管理"))

import img_rc
