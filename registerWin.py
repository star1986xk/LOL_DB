import sys
from UI.Ui_register import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from db_class import db_class


class registerWin(Ui_Dialog, QDialog):
    Sig_login = pyqtSignal(list)

    def __init__(self, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(registerWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.pushButton_register.clicked.connect(self.register)
        self.pushButton_cancel.clicked.connect(self.close)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    def register(self):
        '''
        注册按钮
        '''
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()
        password2 = self.lineEdit_password_2.text().strip()
        if username and password and password2:
            if password == password2:
                db = db_class()
                db.open()
                result = db.select_count_condition('user', 'username ="' + username + '"')
                if not result:
                    result = db.insert_many('user',[{'username':username,'password':password}])
                    if result:
                        QMessageBox.about(self, '提示', '注册成功！')
                    else:
                        QMessageBox.about(self, '提示', '注册失败！')
                else:
                    QMessageBox.about(self, '提示', '用户名已存在！')
            else:
                QMessageBox.about(self, '提示', '两次密码不一致！')
