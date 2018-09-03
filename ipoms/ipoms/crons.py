# -*- coding: utf-8 -*-

"""

定时任务相关

"""

import datetime
import time

from stock.models import *
from stock import services
from . import crawler


# 定时任务，更新新股的状态
def update_stock_status():
    try:
        # 开始时间
        start_time = datetime.datetime.now()
        print start_time, ", begin update_stock_status cron task..."

        # 更新没有上市时间的新股
        stocks = Stock.objects.filter(ss_date__isnull=True)
        for stock in stocks:
            crawler_stock_info = crawler.get_stock_info(stock.stock_code)
            ss_date = crawler_stock_info["ss_date"]
            print ss_date
            Stock.objects.filter(stock_code=stock.stock_code).update(ss_date=ss_date)

        # 更新新股本身的状态，除了已经上市的
        stocks = Stock.objects.filter(current_status__lt=7)
        for stock in stocks:
            services.set_stock_status(stock)
            Stock.objects.filter(stock_code=stock.stock_code).update(current_status=stock.current_status)

        # 结束时间
        end_time = datetime.datetime.now()
        print end_time, ", finish update_stock_status cron task..."
    except Exception as e:
        print e
