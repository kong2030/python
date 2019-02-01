# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from models import *

# Register your models here.


# Define an inline admin descriptor for user model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name_plural = 'addition'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )


# Module admin model
class WebsiteAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('description', 'url')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('description',)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Website, WebsiteAdmin)


