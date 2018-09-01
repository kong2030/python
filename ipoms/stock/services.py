# -*- coding: utf-8 -*-
import datetime
import time


# 在插入数据库前，设置新股的状态
def set_stock_status(stock):
    today = datetime.date.today()
    #today = datetime.datetime.strptime("2017-04-08", "%Y-%m-%d").date()
    zg_start_date = stock.zg_start_date
    zg_end_date = stock.zg_end_date
    cl_start_date = stock.cl_start_date
    cl_end_date = stock.cl_end_date
    xj_start_date = stock.xj_start_date
    xj_end_date = stock.xj_end_date
    sg_start_date = stock.sg_start_date
    sg_end_date = stock.sg_end_date
    jk_start_date = stock.jk_start_date
    jk_end_date = stock.jk_end_date
    ss_date = stock.ss_date

    if today < zg_end_date:
        stock.current_status = 1
    elif today < cl_end_date:
        stock.current_status = 2
    elif today < xj_end_date:
        stock.current_status = 3
    elif today < sg_end_date:
        stock.current_status = 4
    elif today < jk_end_date:
        stock.current_status = 5
    elif ss_date is None or today < ss_date:
        stock.current_status = 6
    else:
        stock.current_status = 7
