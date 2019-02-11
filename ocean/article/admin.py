# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.


# Module admin model
class ArticleAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('title', 'keyword', 'app_system')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('title',)


# register the model
admin.site.register(Article, ArticleAdmin)
