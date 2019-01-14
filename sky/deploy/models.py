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
    remark = models.CharField(max_length=256, null=True)  # 备注

    update_time = models.DateTimeField()  # 最新修改时间
    current_env = models.IntegerField(default=0)  # 0:刚新建
    env_1 = models.IntegerField(default=0)   # 环境间流转状态，0:没开始，1：待发布，2：已发布
    env_2 = models.IntegerField(default=0)
    env_3 = models.IntegerField(default=0)
    env_4 = models.IntegerField(default=0)
    env_5 = models.IntegerField(default=0)


# 发布单发布记录表 model
class OrderHost(models.Model):
    order_code = models.CharField(max_length=16)
    host_ip = models.CharField(max_length=20)
    module_name = models.CharField(max_length=50)
    deploy_status = models.IntegerField()  # 0:发布失败；1：发布成功；2：回滚失败；3：回滚成功
    deploy_time = models.DateTimeField()
    deploy_log = models.TextField(default=" ")

    # 附加参数
    class Meta:
        db_table = 'deploy_order_host'  # 指定数据库表名
