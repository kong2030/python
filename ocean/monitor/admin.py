# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *


class DataBaseInfoAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('name', 'server', 'user', 'database')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('name',)


# Register your models here.
admin.site.register(DataBaseInfo, DataBaseInfoAdmin)
