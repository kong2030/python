# -*- coding: utf-8 -*-
import datetime
import time

from stock.models import *
from stock import services


# 定时任务，更新新股的状态
def update_stock_status():
    try:
        # 开始时间
        start_time = datetime.datetime.now()
        print start_time, ", begin update_stock_status cron task..."

        stocks = Stock.objects.all()
        for stock in stocks:
            services.set_stock_status(stock)
            Stock.objects.filter(stock_code=stock.stock_code).update(current_status=stock.current_status)

        # 结束时间
        end_time = datetime.datetime.now()
        print end_time, ", finish update_stock_status cron task..."
    except Exception as e:
        print e.message


