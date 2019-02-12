# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from models import *
import cmdb.services

# Create your views here.


# 组件列表
@login_required
def list_article_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "zsk"
    sub_menu = "zsk_zslb"

    app_systems = cmdb.services.get_apps_by_user(request.user)
    articles = Article.objects.filter(app_system__in=app_systems)
    return render(request, "article/article_list.html", {"main_memu":main_memu, "sub_menu": sub_menu, "articles": articles})


# 查看知识库文章
@login_required
def view_article(request, id):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "zsk"
    sub_menu = "zsk_zslb"

    article = Article.objects.filter(id=id)[0]
    # 更新点击量
    article.page_view = article.page_view + 1
    article.save()

    return render(request, "article/article_detail.html", {"main_memu":main_memu, "sub_menu": sub_menu,"article": article})