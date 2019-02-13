# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import traceback
import logging
import datetime

from models import *


# Create your views here.
# 修改密码页
@login_required
def pwd_change_page(request):
    return render(request, "config/pwd_change.html")


# 修改密码
@login_required
@csrf_exempt
def save_password(request):
    try:
        old_password = request.POST["oldPwd"].replace(" ", "")
        new_password = request.POST["newPwd"].replace(" ", "")
        user = request.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return HttpResponse("success")
        else:
            return HttpResponse("old password is not right!")
    except Exception as e:
        traceback.print_exc()
        logging.error("save password has an error!")
        logging.exception("EXCEPTION")
        return HttpResponse("Sorry! save error.")


# 网址管理-页面
@login_required
def list_website_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "rcwh"
    sub_menu = "rcwh_wzgl"

    websites = Website.objects.all()
    return render(request, "config/website_list.html", {"main_memu": main_memu, "sub_menu": sub_menu, "websites": websites})


# 网址管理-页面
@login_required
def add_website_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "rcwh"
    sub_menu = "rcwh_wzgl"

    return render(request, "config/website_add.html", {"main_memu": main_memu, "sub_menu": sub_menu})


# 网址管理-页面
@login_required
def edit_website_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "rcwh"
    sub_menu = "rcwh_wzgl"

    website_id = request.GET["websiteId"]
    website = Website.objects.filter(id=website_id)[0]
    return render(request, "config/website_edit.html", {"main_memu": main_memu, "sub_menu": sub_menu, "website": website})


# 网址管理-页面
@login_required
@csrf_exempt
def save_website(request):
    try:
        # 先获取参数
        description = request.POST["description"].replace(" ", "")
        url = request.POST["url"].replace(" ", "")
        update_time = datetime.datetime.now()
        website = Website(description=description, url=url, update_time=update_time)
        # 如果是编辑就加上id,
        if request.POST.has_key("websiteId"):
            website_id = request.POST["websiteId"]
            website.id = website_id
        # 更新数据库
        website.save()

    except Exception as e:
        traceback.print_exc()
        logging.error("save website has an error!")
        logging.exception("EXCEPTION")

    finally:
        return HttpResponseRedirect("/ocean/config/listWebsite")

