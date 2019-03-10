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
import os
import chardet

from models import *
from utils import log_helper


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


# 日志搜索-页面
@login_required
@csrf_exempt
def search_log_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "cygj"
    sub_menu = "cygj_rzss"

    return render(request, "config/log_search.html", {"main_memu": main_memu, "sub_menu": sub_menu, })


# 获取日志
@login_required
@csrf_exempt
def get_log(request):
    log_path = request.POST["logPath"]
    output_path = request.POST["outputPath"]
    log_type = request.POST["logType"]
    search_type = request.POST["searchType"]
    time_begin = request.POST["timeBegin"]
    interval = request.POST["interval"]
    keyword = request.POST["keyword"]

    print log_path,output_path,log_type,search_type,time_begin,interval,keyword

    log_1000 = ""
    for root,dirs,files in os.walk(log_path):
        for file_ in files:
            log_file = os.path.join(root, file_)
            if search_type == "time_type":
                if time_begin.replace(" ","") != "":
                    log_1000 = log_helper.cut_log(log_type,log_file,time_begin,int(interval))
            if search_type == "keyword_type":
                if keyword.replace(" ","") != "":
                    log_1000 = log_helper.search_log(log_type,log_file,keyword)

    print chardet.detect(log_1000)
    #log_1000 = log_1000.encode("ISO-8859-1")
    return HttpResponse(log_1000)