# -*- coding: utf-8 -*-
import pymysql
from settings import *


class db_class():

    def open(self):
        '''
        连接数据库
        @return:
        '''
        self.conn = pymysql.connect(**SQL)
        self.cursor = self.conn.cursor()
        self._sql = None

    def select_all(self, table_name):
        '''
        查询指定表全部数据
        @param table_name:表名
        @return:
        '''
        try:
            self._sql = 'SELECT * FROM %s;' % table_name
            self.cursor.execute(self._sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_all_list(self, table_name):
        '''
        查询指定表全部数据
        @param table_name:表名
        @return:
        '''
        try:
            self._sql = 'SELECT id,title_img,name,area FROM %s;' % table_name
            self.cursor.execute(self._sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_all_area(self, table_name):
        '''
        查询指定表全部数据
        @param table_name:表名
        @return:
        '''
        try:
            self._sql = 'SELECT distinct area FROM %s;' % table_name
            self.cursor.execute(self._sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_count(self, table_name):
        '''
        查询指定表的数据条数
        @param table_name:表名
        @return:(条数,)
        '''
        try:
            self._sql = 'SELECT count(*) FROM %s;' % table_name
            self.cursor.execute(self._sql)
            result = self.cursor.fetchall()
            return result[0][0]
        except Exception as e:
            print(e)
            return None

    def select_count_condition(self, table_name, condition):
        '''
        条件查询\n
        @param table_name: 表名
        @param condition:条件
        @return: 条数
        '''
        try:
            self._sql = 'SELECT count(*) FROM ' + table_name + ' where ' + condition + ';'
            self.cursor.execute(self._sql)
            result = self.cursor.fetchall()
            return result[0][0]
        except Exception as e:
            print(e)
            return None

    def select_condition(self, table_name, condition):
        '''
        条件查询\n
        如:select * from table1 where id=1 and name='xx';\n
        传参数：{'id':'1','name':'xx'}\n
        @param table_name: 表名
        @param condition:{'字段':'值',,,}
        @return: 查询后的数据集合
        '''
        try:
            self._sql = 'SELECT id,title_img,name,area FROM ' + table_name + ' WHERE ' + condition + ';'
            self.cursor.execute(self._sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def select_uid(self, table_name, id):
        '''
        按id查询数据
        '''
        try:
            self._sql = "select * from " + table_name + " where id='" + id + "';"
            self.cursor.execute(self._sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def insert_many(self, table_name, obj_list):
        '''
        批量插入相同格式的一批数据\n
        如:\n
        insert table1(name,age) values('小明',30);\n
        insert table1(name,age) values('老王',30);\n
        可传参数:\n
        obj_list = [{'name':'小明','age':'10'},{'name':'老王','age':'30'}]\n
        @param table_name: 表名
        @param obj_list: [{'字段'：'值',,,},,,]
        @return: True|False
        '''
        try:
            self._sql = 'INSERT ' + table_name + '(' + ','.join([k for k in obj_list[0].keys()]) + ') VALUES(' + \
                        ','.join(['%s' for k in obj_list[0]]) + ');'
            datas = tuple(tuple(v for v in li.values()) for li in obj_list)
            self.cursor.executemany(self._sql, datas)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update_many(self, table_name, obj_list, condition_list):
        '''
        批量更新相同格式的一批数据\n
        如: \n
        update table1 set name='小明',age=10 where id=1;\n
        update table1 set name='老王',age=30 where id=2;\n
        可这样传参数:\n
        obj_list = [{'name':'小明','age':'10'},{'name':'老王','age':'30'}]\n
        condition_list = [{'id':'1'},{'id':'2'}]
        @param table_name: 表名
        @param obj_list: [{'字段'：'值',,,},,,]
        @param condition_list: [{'字段'：'值',,,},,,]
        @return:True|False
        '''
        try:
            self._sql = 'UPDATE ' + table_name + ' SET ' + ','.join(
                [k + '=%s' for k in obj_list[0].keys()]) + ' WHERE ' + \
                        ' and '.join([k + '=%s' for k in condition_list[0].keys()]) + ';'
            datas = tuple(
                tuple(obj.values()) + tuple(condition.values()) for obj, condition in zip(obj_list, condition_list))
            self.cursor.executemany(self._sql, datas)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_many(self, table_name, condition_list):
        '''
        批量删除\n
        如：\n
        delete from table1 where id=1 and name='xxx'\n
        delete from table1 where id=3 and name='yy'\n
        可传参数\n
        condition_list = [{id:'1','name':'xxx'},{id:'3','name':'yy'}]
        @param table_name: 表名
        @param condition_list: [{'字段': '值',,,},,,]
        @return: True|False
        '''
        try:
            self._sql = 'DELETE FROM ' + table_name + ' WHERE ' + ' and '.join(
                [k + '=%s' for k in condition_list[0].keys()]) + ';'
            datas = tuple(tuple(condition.values()) for condition in condition_list)
            self.cursor.executemany(self._sql, datas)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_all(self, table_name):
        '''
        删除全部
        '''
        try:
            self._sql = 'truncate table ' + table_name + ';'
            self.cursor.execute(self._sql)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False

    def close(self):
        '''
        关闭连接
        '''
        self.cursor.close()
        self.conn.close()
