from UI.Ui_info import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import  QLabel
from db_class import db_class
from PyQt5.QtCore import QSize, Qt




class infoWin(Ui_Dialog, QDialog):

    def __init__(self, id=None, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(infoWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        db = db_class()
        db.open()
        result  = db.select_uid('hero', id)
        db.close()

        self.widget_2.setStyleSheet("image: url("+ result[0][4] +");")

        self.label_3.setText(result[0][1])
        self.label_4.setText(result[0][2])
        self.textEdit.setHtml(result[0][3])

        self.pushButton.clicked.connect(self.up)
        self.pushButton_2.clicked.connect(self.down)
        self.pushButton_3.clicked.connect(self.close)

        self.img_list =  eval(result[0][5])
        self.loadImg()

    def loadImg(self):
        '''
        载入图片
        '''
        # 清空stackedWidget
        for i in range(self.stackedWidget.count(), -1, -1):
            widget = self.stackedWidget.widget(i)
            self.stackedWidget.removeWidget(widget)
        # 写入图片
        for img in self.img_list:
            page = QWidget()
            verticalLayout = QVBoxLayout(page)
            label = QLabel(self)
            pix = QPixmap(img)
            fitpixmap = pix.scaled(900, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation);
            label.setPixmap(QPixmap(fitpixmap))
            verticalLayout.addWidget(label)
            self.stackedWidget.addWidget(page)
        self.page_now = self.stackedWidget.currentIndex() + 1
        self.page_count = len(self.img_list)
        self.label.setText(str(self.page_now) + '/' + str(self.page_count))

    def up(self):
        '''
        上一页
        :return:
        '''
        index = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(index - 1)
        self.label.setText(str(self.stackedWidget.currentIndex() + 1) + '/' + str(self.page_count))

    def down(self):
        '''
        下一页
        :return:
        '''
        index = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(index + 1)
        self.label.setText(str(self.stackedWidget.currentIndex() + 1) + '/' + str(self.page_count))

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