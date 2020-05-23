import os
import requests
from lxml import etree
import re
from settings import *
import copy
import time
import json
from db_class import db_class
from PyQt5.QtCore import QThread
from threading import Thread
from PyQt5.QtCore import pyqtSignal


# 搜索类
class search_class(QThread):
    sig_one_end = pyqtSignal(str)
    sig_end = pyqtSignal(str)

    def __init__(self, thread_count=None):
        '''
        初始化
        :param url_class: 类型url
        :param page_count: 查询页数
        :param thread_count: 线程数
        '''
        super(search_class, self).__init__()
        self.flag = True
        self.thread_count = int(thread_count)

    def requestGET(self, url, headers):
        '''
        get请求
        :param url: url
        :return: 返回text或none
        '''
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            return None

    def saveIMG(self, dir, name, url):
        '''
        保存图片
        '''
        try:
            if not os.path.exists('./img/' + dir):
                os.makedirs('./img/' + dir)
            response = requests.get(url, headers)
            if response.status_code == 200:
                with open('./img/' + dir + '/' + name, 'wb') as f:
                    f.write(response.content)
        except Exception as e:
            print(e)

    def parser_index(self, area, table):
        '''
        解析索引页
        :param url: 索引页url
        :return:
        '''
        try:
            db = db_class()
            db.open()
            # 请求索引页
            title_img_list = table.xpath('.//td//img/@src')
            url_list = table.xpath('.//td/p[2]/a/@href')
            name_list = table.xpath('.//td/p[2]/a/text()')
            for title_img, url, name in zip(title_img_list, url_list, name_list):
                try:
                    if self.flag:
                        text = self.requestGET(url, headers)
                        if text:
                            html = etree.HTML(text)
                            text = text.replace('\n','')
                            content1 = re.search('<strong>背景故事</strong>\s*?</p>(.*?)<hr.*?>', text, flags=re.DOTALL | re.S | re.I)
                            if content1:
                                content = content1[1]
                                self.saveIMG(name, 'title.' + title_img.split('.')[-1], title_img)
                                title_path = './img/' + name + '/' + 'title.' + title_img.split('.')[-1]
                                skin_img_list = html.xpath('//p[@align="center"]//a/img/@src')
                                skin_path = []
                                for n,skin_img in enumerate(skin_img_list):
                                    self.saveIMG(name, str(n)+'.' + skin_img.split('.')[-1],skin_img)
                                    skin_url = './img/' + name + '/' + str(n)+'.' + skin_img.split('.')[-1]
                                    skin_path.append(skin_url)
                                hero = {}
                                hero['name'] = name
                                hero['area'] = area
                                hero['content'] = content
                                hero['title_img'] = title_path
                                hero['skin_img'] = str(skin_path)
                                db.insert_many('hero',[hero])
                                self.sig_one_end.emit(name+' 抓取成功！')
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
            print(area)
        finally:
            db.close()



    def thread_pool(self):
        '''
        线程池,多线程解析索引页
        :return:
        '''
        try:
            text = self.requestGET('https://www.newyx.net/gl/564430_1.htm', headers)
            if text:
                html = etree.HTML(text)
                area_list = html.xpath('//span[@style="color:#337FE5;"]/text()')
                table_list = html.xpath('//span[@style="color:#337FE5;"]/../../following-sibling::table')
                area_list = area_list[:13]
                table_list = table_list[:13]
                for i in range(1, len(area_list), self.thread_count):
                    if self.flag:
                        self.result = []
                        self.task_list = [Thread(target=self.parser_index, args=(area, table)) for area, table in
                                          zip(area_list[i:i + self.thread_count], table_list[i:i + self.thread_count])]
                        [task.start() for task in self.task_list]
                        [task.join() for task in self.task_list]
                        time.sleep(1)
        except Exception as e:
            print(e)
        finally:
            self.sig_end.emit('运行结束！ ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 执行函数
    def run(self):
        '''
        运行爬虫
        '''
        self.thread_pool()
