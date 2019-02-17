# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cmdb.models import *


# Create your models here.
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