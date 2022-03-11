'''数据库操作'''
from woniusales_project.pytest_kdt_ui.config import mysql_dict
class mysql():
    def __init__(self):
        import pymysql
        self.cnn  = pymysql.connect(**mysql_dict) # 建立链接
        self.cur = self.cnn.cursor(pymysql.cursors.DictCursor) # 读取信息为字典,cur是一个数据库对象

    def query(self,sql):
        '''查询'''
        self.cur.execute(sql)
        return self.cur.fetchall() # 返回查询结果

    def execute(self,sql):
        '''数据语句操作'''
        self.cur.execute(sql)

    def __del__(self):
        self.cur.close()
        self.cnn.close() # 断开链接