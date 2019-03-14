# -*- coding: utf-8 -*-
import os
import time
import sys
import base64

from models import *
from monitor.services import get_sql_data


# 采集期权委托数据
def collect_data_qq(datasource, sql):
    try:
        data = get_sql_data(datasource, sql)
        for record in data:
            order = OptOrder()
            order.trd_date = record[0]
            order.order_date = record[1]
            order.order_time = record[2]
            order.order_id = record[5]
            order.order_status = record[7]
            order.int_org = record[10]
            order.cust_code = record[11]
            order.cust_name = record[12].encode("iso-8859-1").decode("gbk")
            order.cuacct_code = record[15]
            order.stkex = record[21]
            order.stkbd = record[22]
            order.stkpbu = record[23]
            order.trdacct = record[24]
            order.subacct_code = record[25]
            order.stk_biz = record[30]
            order.stk_biz_action = record[31]
            order.stk_biz_ex = record[32]
            order.opt_num = record[34]
            order.channel = record[75]

            # 插入本地库
            record_local = OptOrder.objects.filter(order_time=order.order_time, order_id=order.order_id)
            if not record_local.exists():
                order.save()

        return "success"

    except Exception as e:
        return str(e)
