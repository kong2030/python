# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

# Register your models here.


# Underwriter admin model
class UnderwriterAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('id', 'underwriter', 'shortname', 'telephone')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'underwriter')


# Product admin model
class ProductAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('id', 'product_code', 'record_code', 'product_name')


# Stock admin model
class StockAdmin(admin.ModelAdmin):
    # show the key info
    list_display = ('id', 'stock_code', 'stock_name', 'underwriter')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'stock_name')


# register the model
admin.site.register(Underwriter, UnderwriterAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
