# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.


# Order admin model
class OrderAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('order_code', 'module', 'app_system', 'creator', 'create_time')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('order_code',)


# register the model
admin.site.register(Order, OrderAdmin)