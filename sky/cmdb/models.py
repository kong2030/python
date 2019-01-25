# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 环境信息 model
class Environment(models.Model):
    env_id = models.IntegerField(primary_key=True) # 1：测试环境，2：预发布环境，3：生产环境，4：同城灾备，5：异地灾备
    env_name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=20, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    network = models.CharField(max_length=128, null=True, blank=True)  # 网段信息

    def __unicode__(self):
        return self.env_name


# 应用系统 model
class AppSystem(models.Model):
    app_name = models.CharField(max_length=50, unique=True)
    chinese_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.chinese_name


# 操作系统类型 model
class OSystem(models.Model):
    os_id = models.IntegerField(primary_key=True) # 1：windows，2：linux，
    os_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.os_name

    # 附加参数
    class Meta:
        db_table = 'cmdb_os'  # 指定数据库表名


# 组件 model
class Module(models.Model):
    module_name = models.CharField(max_length=50, unique=True)
    chinese_name = models.CharField(max_length=50)
    program_path = models.CharField(max_length=128)   # 程序安装路径
    script_path = models.CharField(max_length=128)    # 部署需用到的本地脚本路径
    app_system = models.ForeignKey(AppSystem, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.module_name


# 主机 model
class Host(models.Model):
    host_name = models.CharField(max_length=20, unique=True)
    ip = models.CharField(max_length=20, unique=True)
    host_user = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    os_type = models.ForeignKey(OSystem, on_delete=models.PROTECT, default=1)
    environment = models.ForeignKey(Environment, on_delete=models.PROTECT)
    module = models.ManyToManyField(Module)

    def __unicode__(self):
        return self.ip


# 用户-系统 model （用户有权限管理的系统）
class UserApp(models.Model):
    user_id = models.IntegerField()
    user_code = models.CharField(max_length=5)
    user_name = models.CharField(max_length=50)
    app_id = models.IntegerField()
    app_name = models.CharField(max_length=50)

    # 附加参数
    class Meta:
        db_table = 'cmdb_app_user'  # 指定数据库表名