import sys
import time
from PyQt5.QtGui import QPixmap
from loginWin import loginWin
from UI.Ui_mainWin import Ui_Form
from PyQt5.QtWidgets import QTableWidgetItem, QRadioButton, QLabel, QWidget, QApplication, QHeaderView
from db_class import db_class
from PyQt5.QtCore import QSize, Qt
from search_class import search_class
from infoWin import infoWin

class lolWin(Ui_Form, QWidget):
    def __init__(self, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super(lolWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        headerView = self.tableWidget.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)

        # self.setWindowFlags(
        #     Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.tableWidget.clicked.connect(self.t_check)
        self.tabWidget.currentChanged.connect(self.tabChange)
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_del.clicked.connect(self.btn_del)
        self.pushButton_clear.clicked.connect(self.btn_clear)
        self.pushButton_stop.clicked.connect(self.btn_stop)
        self.pushButton_search.clicked.connect(self.btn_search)
        self.pushButton_info.clicked.connect(self.btn_info)

        self.login = loginWin()
        self.login.Sig_login.connect(self.load)
        self.login.show()

    def load(self):
        '''
        显示主窗口
        '''
        self.show()

    def getCheckedRow(self):
        '''
        得到选中行
        '''
        row = None
        rowCount = self.tableWidget.rowCount()
        for r in range(rowCount):
            if self.tableWidget.cellWidget(r, 0).isChecked():
                row = r
                break
        return row

    def t_check(self, n):
        '''
        改变选中状态
        '''
        if self.tableWidget.cellWidget(n.row(), 0).isChecked():
            self.tableWidget.cellWidget(n.row(), 0).setChecked(False)
        else:
            self.tableWidget.cellWidget(n.row(), 0).setChecked(True)

    def run(self):
        '''
        运行爬虫
        '''
        self.pushButton_run.setDisabled(True)
        self.textBrowser.clear()
        self.textBrowser.append('运行开始！ ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        thread_count = self.spinBox_thread.text()
        self.search_class = search_class(thread_count)
        self.search_class.sig_one_end.connect(self.one_end)
        self.search_class.sig_end.connect(self.end)
        self.search_class.start()

    def btn_info(self):
        '''
        打开详细信息窗口
        '''
        row = self.getCheckedRow()
        if row != None:
            id = self.tableWidget.item(row, 1).text()
            self.infoWin = infoWin(id)
            self.infoWin.show()

    def btn_del(self):
        '''
        删除按钮
        '''
        row = self.getCheckedRow()
        if row != None:
            id = self.tableWidget.item(row, 1).text()
            db = db_class()
            db.open()
            db.delete_many('hero', [{'id': id}])
            db.close()
            self.tabChange(1)

    def btn_clear(self):
        '''
        清空按钮
        '''
        db = db_class()
        db.open()
        db.delete_all('hero')
        db.close()
        self.tabChange(1)

    def btn_search(self):
        '''
        搜索按钮
        '''
        condition = []
        area = self.comboBox.currentText()
        name = self.lineEdit.text().strip()
        if area != '全部':
            condition.append('area="' + area + '"')
        if name:
            condition.append('name like "%' + name + '%"')
        if condition:
            condition_str = ' and '.join(condition)
            db = db_class()
            db.open()
            result = db.select_condition('hero',condition_str)
            db.close()
            self.load_table(result)
        else:
            self.tabChange(1)

    def one_end(self, text):
        '''
        返回一个爬取结果信号
        '''
        self.textBrowser.append(text)

    def end(self, text):
        '''
        爬虫结果信号
        '''
        self.textBrowser.append(text)
        self.pushButton_run.setDisabled(False)

    def btn_stop(self):
        '''
        停止按钮
        '''
        if hasattr(self, 'search_class'):
            self.search_class.flag = False

    def tabChange(self, index):
        '''
        tab改变时，载入勾选项
        :param index:
        :return:
        '''
        if index == 1:
            db = db_class()
            db.open()
            result = db.select_all_list('hero')
            result_area = db.select_all_area('hero')
            db.close()
            self.load_table(result)
            self.comboBox.clear()
            self.comboBox.addItem('全部')
            self.comboBox.addItems([area[0] for area in result_area])

    def load_table(self, items):
        '''
        数据写入表
        :param items:数据集合
        :return:
        '''
        try:
            self.tableWidget.setRowCount(0)
            for n, item in enumerate(items):
                self.tableWidget.setRowCount(n + 1)
                radio = QRadioButton()
                pix = QPixmap(item[1])
                pix = pix.scaled(QSize(40, 40), Qt.KeepAspectRatio);
                lb1 = QLabel(self)
                lb1.setPixmap(pix)
                lb1.setAlignment(Qt.AlignHCenter)
                self.tableWidget.setCellWidget(n, 0, radio)
                self.tableWidget.setItem(n, 1, QTableWidgetItem(str(item[0])))
                self.tableWidget.setCellWidget(n, 2, lb1)
                self.tableWidget.setItem(n, 3, QTableWidgetItem(str(item[2])))
                self.tableWidget.setItem(n, 4, QTableWidgetItem(str(item[3])))
                self.tableWidget.setRowHeight(n, 40)
        except Exception as e:
            print(e)

    def closeEvent(self, evt):
        '''
        关闭
        '''
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = lolWin()
    # win.show()
    sys.exit(app.exec_())
