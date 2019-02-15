# -*- coding: utf-8 -*-
from celery import shared_task


@shared_task()
def excute_sql(x,y):
    print "%d * %d = %d" % (x, y, x * y)
    return x * y


@shared_task()
def monitor_sql(**kwargs):
    print kwargs["sql"]
    count = 10
    return count
