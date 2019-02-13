# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

import datetime

# Register your models here.


# Module admin model
class ArticleAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('title', 'keyword', 'app_system')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('title',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.update_time = datetime.datetime.now()
        obj.save()

    readonly_fields = ("author", "update_time", "page_view")


# register the model
admin.site.register(Article, ArticleAdmin)
