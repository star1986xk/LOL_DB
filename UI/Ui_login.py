# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(536, 330)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("#widget{border-image: url(:/newPrefix/img/bg2.jpg);}\n"
"QPushButton{color: rgb(255, 255, 255);border-style:none;border-radius: 10px;}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color: rgb(200, 200, 200,120);\n"
"}\n"
"QPushButton:pressed {  \n"
"    /* 改变背景色 */  \n"
"    background-color:rgb(180, 180, 180,120);  \n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:1px;  \n"
"    padding-top:1px;  \n"
"}\n"
"\n"
"QLineEdit{border: 1px solid #000000;border-radius:5px;}\n"
"\n"
"QLabel{color: rgb(255, 255, 255);}\n"
"QLabel{font-weight: bold;}\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(120, 30, 241, 50))
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setAcceptDrops(False)
        self.label.setObjectName("label")
        self.pushButton_close = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_close.setGeometry(QtCore.QRect(490, 0, 15, 15))
        self.pushButton_close.setMinimumSize(QtCore.QSize(15, 15))
        self.pushButton_close.setMaximumSize(QtCore.QSize(15, 15))
        self.pushButton_close.setStyleSheet("QPushButton{\n"
"padding:2px 2px 2px 2px;\n"
"background-color: rgba(255,255,255,0);\n"
"border-style:none;\n"
"border-radius: 5px;\n"
"image:url(:/newPrefix/img/关闭1.png);\n"
"width:15px;height:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"padding:2px 2px 2px 2px;\n"
"image:url(:/newPrefix/img/关闭.png);\n"
"background-color: rgb(220, 220, 220,100);\n"
"border-radius: 5px;\n"
"width:15px;height:15px;\n"
"}\n"
"QPushButton:pressed {\n"
"padding:2px 2px 2px 2px;\n"
"    image:url(:/newPrefix/img/关闭1.png);\n"
"    /* 改变背景色 */  \n"
"    background-color:rgb(180, 180, 180,100);  \n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:1px;  \n"
"    padding-top:1px;  \n"
"border-radius: 5px;\n"
"}")
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(-1, 20, -1, 10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_username.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_login = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_login.setMinimumSize(QtCore.QSize(80, 20))
        self.pushButton_login.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.pushButton_login)
        self.pushButton_register = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_register.setMinimumSize(QtCore.QSize(80, 20))
        self.pushButton_register.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout.addWidget(self.pushButton_register)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "英雄联盟数据库管理系统"))
        self.label_3.setText(_translate("Dialog", "密  码："))
        self.label_2.setText(_translate("Dialog", "用户名："))
        self.pushButton_login.setText(_translate("Dialog", "登  录"))
        self.pushButton_register.setText(_translate("Dialog", "注  册"))
        self.label_4.setText(_translate("Dialog", " 经济管理专业  信息管理与信息系统专业   xx制作 "))
import img_rc
