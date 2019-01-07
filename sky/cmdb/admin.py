# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

# Register your models here.


# Environment admin model
class EnvironmentAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('env_id', 'env_name', 'network')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('env_id', 'env_name')


# OSystem admin model
class OSystemAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('os_id', 'os_name')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('os_id', 'os_name')


# AppSystem admin model
class AppSystemAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('id', 'app_name', 'chinese_name')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'app_name')


# Module admin model
class ModuleAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('id', 'module_name', 'chinese_name')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'module_name')


# Module admin model
class HostAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('id', 'ip', 'host_name', 'environment')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'ip')


# register the model
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(OSystem, OSystemAdmin)
admin.site.register(AppSystem, AppSystemAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Host, HostAdmin)