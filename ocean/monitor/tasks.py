# -*- coding: utf-8 -*-
from celery import shared_task
from djcelery.models import PeriodicTask, CrontabSchedule
import datetime
from django.db.models import Max, Count

from services import *


# 测试任务
@shared_task()
def excute_sql(x,y):
    print "%d * %d = %d" % (x, y, x * y)
    return x * y


# 监控任务：查询数据库并进行告警
@shared_task()
def monitor_sql(*args, **kwargs):
    print kwargs["name"]
    print kwargs["sql"]

    task_name = kwargs["name"]
    datasource = kwargs["datasource"]
    sql = kwargs["sql"]
    operator = kwargs["operator"]
    threshold = kwargs["threshold"]
    tasks = PeriodicTask.objects.filter(name=task_name)
    if tasks.exists():
        task = tasks[0]
        data = get_sql_data(datasource, sql)
        # -1:表示没查到数据，无法判断是否异常
        sql_result = -1
        monitor_result = -1
        if len(data) > 0:
            sql_result = data[0][0]

            monitor_result = 0
            # 达到设定阈值
            if operator == ">=":
                if sql_result >= threshold:
                    monitor_result = 1  # 异常
            # 小于设定阈值
            elif operator == "<":
                if sql_result < threshold:
                    monitor_result = 1  # 异常
            # 查询记录不变
            elif operator == "==":
                task_results = TaskResult.objects.filter(task_id=task.id)
                if task_results.exists():
                    task_result_before = task_results.latest('last_run_time')
                    sql_data_before = task_result_before.sql_data
                    if sql_result == sql_data_before:
                        monitor_result = 1  # 异常

        # 保存采集数据
        task_result = TaskResult(task_id=task.id, task_name=task.name, last_run_time=datetime.datetime.now(),
                                 operator=operator, threshold=threshold, sql_data=sql_result,
                                 monitor_result=monitor_result)
        task_result.save()

    return sql_result
