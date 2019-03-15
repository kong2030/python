# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 期权订单表
class OptOrder(models.Model):
    trd_date = models.CharField(max_length=8)
    order_date = models.CharField(max_length=8)
    order_time = models.DateTimeField()
    order_id = models.CharField(max_length=20)
    order_status = models.CharField(max_length=1)
    int_org = models.CharField(max_length=8)
    cust_code = models.BigIntegerField()
    cust_name = models.CharField(max_length=100)
    cuacct_code = models.BigIntegerField()
    stkex = models.CharField(max_length=1)
    stkbd = models.CharField(max_length=2)
    stkpbu = models.CharField(max_length=8)
    trdacct = models.CharField(max_length=20)
    subacct_code = models.CharField(max_length=8)
    stk_biz = models.IntegerField()
    stk_biz_action = models.IntegerField()
    stk_biz_ex = models.CharField(max_length=8)
    opt_num = models.CharField(max_length=16)
    channel = models.CharField(max_length=1)


# 资源使用表,借用zabbix的命名
class History(models.Model):
    host_ip = models.CharField(max_length=16)
    clock = models.DateTimeField()
    item = models.CharField(max_length=50)
    value = models.FloatField()















