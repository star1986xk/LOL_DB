import sys
from UI.Ui_login import Ui_Dialog
from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from db_class import db_class
from registerWin import registerWin


class loginWin(Ui_Dialog, QDialog):
    Sig_login = pyqtSignal()

    def __init__(self, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(loginWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_close.clicked.connect(self.quit)
        self.pushButton_register.clicked.connect(self.register)


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

    def login(self):
        '''
        登录按钮
        '''
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()
        if username and password:
            db = db_class()
            db.open()
            result = db.select_count_condition('user', 'username="' + username + '" and password="' + password+'"')
            db.close()
            if result:
                self.Sig_login.emit()
                self.close()
            else:
                QMessageBox.about(self,'提示','账号或密码错误！')

    def register(self):
        '''
        注册按钮
        '''
        self.registerWin = registerWin()
        self.registerWin.show()

    def quit(self):
        '''
        关闭
        '''
        sys.exit(0)
