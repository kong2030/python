# -*- coding: utf-8 -*-
from celery import shared_task
from djcelery.models import PeriodicTask, CrontabSchedule

from services import *

@shared_task()
def excute_sql(x,y):
    print "%d * %d = %d" % (x, y, x * y)
    return x * y


@shared_task()
def monitor_sql(*args, **kwargs):
    print kwargs["name"]
    print kwargs["sql"]

    task_name = kwargs["name"]
    datasource = kwargs["datasource"]
    sql = kwargs["sql"]
    tasks = PeriodicTask.objects.filter(name=task_name)
    if tasks.exists():
        task = tasks[0]
        print task.id
        data = get_sql_data(datasource, sql)
        if len(data) > 0:
            print data[0][0]
        for result in data:
            print result



    #print "id",monitor_sql.request.id


    count = 10
    return count
