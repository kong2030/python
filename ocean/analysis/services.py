# -*- coding: utf-8 -*-
import os
import time
import sys
import base64
import datetime

from models import *
from monitor.services import get_sql_data


# 采集期权委托数据
def collect_data_qq(datasource, sql):
    try:
        data = get_sql_data(datasource, sql)
        count = 0
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
                count = count + 1
                order.save()

        return "success, total:",count

    except Exception as e:
        return str(e)


# 采集主机资源使用率数据
def collect_data_host(collect_path):
    try:
        today_date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        today_time_str = today_date_str + " " + "00:00:00"
        today_time = datetime.datetime.strptime(today_time_str, "%Y-%m-%d %H:%M:%S")
        for root,dir,files in os.walk(collect_path):
            for file_ in files:
                host_ip = file_.split("_")[0]
                item = "cpu_usage"
                file_path = os.path.join(root, file_)
                with open(file_path,'r') as f:
                    count = 0
                    for line in f:
                        clock_str = line.split(",")[0]
                        clock = datetime.datetime.strptime(clock_str, "%Y-%m-%d %H:%M:%S")
                        if clock >= today_time:
                            value = line.split(",")[2]

                            record_local = History.objects.filter(host_ip=host_ip, clock=clock, item=item)
                            if not record_local.exists():
                                count = count + 1
                                cpu_data = History(host_ip=host_ip, clock=clock, item=item, value=value)
                                cpu_data.save()

        return "success, total:",count
    except Exception as e:
        return str(e)