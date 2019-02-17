# -*- coding: utf-8 -*-
import os
import time
import sys
import base64

from models import *
from utils.mssql_helper import *


def get_sql_data(datasource, sql):
    database_info = DataBaseInfo.objects.filter(name=datasource)[0]
    # 解密
    decode_str = base64.decodestring(database_info.password)
    password = decode_str[-1] + decode_str[-2] + decode_str[2:-2] + decode_str[1] + decode_str[0]
    if database_info.type == 1:
        mssql_helper = MssqlHelper(database_info.server, database_info.user, password)
        data = mssql_helper.get_all(sql)
        return data