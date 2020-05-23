# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_register.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(301, 448)
        Dialog.setStyleSheet("#widget{border-image: url(:/newPrefix/img/bg3.png);}\n"
"\n"
"QLineEdit{border: 1px solid #000000;border-radius:5px;}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("QLabel{color: rgb(255, 255, 255);}\n"
"QLabel{font-weight: bold;}\n"
"\n"
"\n"
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
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout.setContentsMargins(-1, 20, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(20, -1, 20, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMinimumSize(QtCore.QSize(60, 0))
        self.label_4.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMinimumSize(QtCore.QSize(60, 0))
        self.label_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_username.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 0, 1, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_password_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_password_2.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_password_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_password_2.setText("")
        self.lineEdit_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_2.setObjectName("lineEdit_password_2")
        self.gridLayout.addWidget(self.lineEdit_password_2, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_register = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_register.setMinimumSize(QtCore.QSize(80, 20))
        self.pushButton_register.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout_2.addWidget(self.pushButton_register)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(80, 20))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "用 户 注 册"))
        self.label_4.setText(_translate("Dialog", "密  码："))
        self.label_5.setText(_translate("Dialog", "确认密码："))
        self.label_2.setText(_translate("Dialog", "用户名："))
        self.pushButton_register.setText(_translate("Dialog", "注  册"))
        self.pushButton_cancel.setText(_translate("Dialog", "取  消"))
import img_rc
