# -*- coding: utf-8 -*-
import pymssql
import traceback


class MssqlHelper(object):
    """
    数据访问层
    status：查询状态,True 查询正常，False 查询失败,默认为True
    """

    def __init__(self, server, user, password, database=None):
        self.__server = server
        self.__user = user
        self.__password = password
        self.__database = database
        self.rowcount = None
        self.error_msg = ''
        self.status = True

    def __conn(self):
        try:
            if self.__database is not None:
                conn = pymssql.connect(server=self.__server, user=self.__user, password=self.__password, database=self.__database, charset="utf8")
            else:
                conn = pymssql.connect(server=self.__server, user=self.__user, password=self.__password, charset="utf8")
        except Exception, e:
            self.error_msg = '%s' % e
            self.status = False
            conn = None
        return conn

    def get_all(self, sql, paramters=None):
        conn = self.__conn()
        if not conn:
            return None
        try:
            cur = conn.cursor()
            cur.execute(sql, paramters)
            data = cur.fetchall()
            self.rowcount = cur.rowcount
        except Exception, e:
            traceback.print_exc()
            data = None
        finally:
            cur.close()
            conn.commit()
            conn.close()
        return data