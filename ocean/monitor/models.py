# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cmdb.models import *


# Create your models here.
# 数据源 model
class DataBaseInfo(models.Model):
    """
    数据库信息
    """
    name = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name=u'名称')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'描述')
    server = models.CharField(max_length=255, null=True, blank=True, unique=True, verbose_name=u'主机')
    user = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'用户')
    password = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'密码')
    database = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'数据库实例')
    type = models.IntegerField(null=True, blank=True, verbose_name=u'数据库类型') # 1:mssql; 2:mysql 3:oracle
    app_system = models.ForeignKey(AppSystem, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.name


# 监控结果 model
class TaskResult(models.Model):
    task_id = models.IntegerField()
    task_name = models.CharField(max_length=255, null=True, blank=True)
    last_run_time = models.DateTimeField(null=True, blank=True)
    # "==":查询结果不变(需要判断上次的采集数据)；">=":达到阈值；"<"：小于阈值
    operator = models.CharField(max_length=255, null=True, blank=True)
    threshold = models.IntegerField(null=True, blank=True)  # 预设的阈值
    sql_data = models.IntegerField(null=True, blank=True) # 数据库的原始采集数据
    monitor_result = models.IntegerField(null=True, blank=True) # 根据阈值判断，0:正常；1：异常；-1：未知

    def __unicode__(self):
        return self.task_name
