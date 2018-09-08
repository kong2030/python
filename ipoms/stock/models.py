# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 承销商 model
class Underwriter(models.Model):
    underwriter = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.underwriter


# 打新产品 model
class Product(models.Model):
    product_code = models.CharField(max_length=50)
    record_code = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50)
    sz_account = models.CharField(max_length=50, null=True, blank=True)
    sh_account = models.CharField(max_length=50, null=True, blank=True)
    bank_account = models.CharField(max_length=256, null=True, blank=True)
    # 产品状态：0：已到期；1：正常
    status = models.IntegerField(default=1)


# 新股 model
class Stock(models.Model):
    stock_code = models.CharField(max_length=50, unique=True)
    stock_name = models.CharField(max_length=50)
    # 上市地点：深市 或 沪市
    stock_type = models.CharField(max_length=50)
    # 外键，关联承销商
    underwriter = models.ForeignKey(Underwriter, on_delete=models.PROTECT)
    # 招股公告开始与结束时间
    zg_start_date = models.DateField()
    zg_end_date = models.DateField()
    # 材料提交开始与结束时间
    cl_start_date = models.DateField()
    cl_end_date = models.DateField()
    # 初步询价开始与结束时间
    xj_start_date = models.DateField()
    xj_end_date = models.DateField()
    # 网下申购开始与结束时间
    sg_start_date = models.DateField()
    sg_end_date = models.DateField()
    # 配售缴款开始与结束时间
    jk_start_date = models.DateField()
    jk_end_date = models.DateField()
    # 上市时间
    ss_date = models.DateField(null=True, blank=True)
    # 当前状态: 0：开始; 1：招股公告；2：材料提交；3：初步询价；4：网下申购；5：配售缴款；6：准备上市；7：结束
    current_status = models.IntegerField(default=0)

    def __unicode__(self):
        return self.stock_name


# 新股申购 model
class Operation(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    stock_code = models.CharField(max_length=50)
    stock_name = models.CharField(max_length=50)
    step = models.IntegerField()
    current_status = models.IntegerField()
    done_time = models.DateTimeField()
    product_list = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shares = models.IntegerField(null=True, blank=True)
    operator = models.CharField(max_length=50, null=True, blank=True)
    reviewer = models.CharField(max_length=50, null=True, blank=True)
    remark = models.CharField(max_length=255, null=True, blank=True)

