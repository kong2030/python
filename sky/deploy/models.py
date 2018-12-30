# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from cmdb.models import *

# Create your models here.


# 发布单 model
class Order(models.Model):
    order_code = models.CharField(max_length=16, unique=True)
    type = models.IntegerField()  # 1：手动上传压缩包 2：sql脚本 3：jenkins方式
    app_system = models.ForeignKey(AppSystem, on_delete=models.PROTECT)
    module = models.ForeignKey(Module, on_delete=models.PROTECT)
    deploy_args = models.CharField(max_length=128, null=True)  # 部署需要的一些参数
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    create_time = models.DateTimeField()