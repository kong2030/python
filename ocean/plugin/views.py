# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import traceback
import logging
import datetime
import os
import chardet
import services

# Create your views here.

# 日志搜索（本地）-页面
@login_required
@csrf_exempt
def search_log_local_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "cygj"
    sub_menu = "cygj_rzss_local"

    return render(request, "plugin/log_search_local.html", {"main_memu": main_memu, "sub_menu": sub_menu, })


# 日志搜索（远程）-页面
@login_required
@csrf_exempt
def search_log_remote_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "cygj"
    sub_menu = "cygj_rzss_remote"

    return render(request, "plugin/log_search_remote.html", {"main_memu": main_memu, "sub_menu": sub_menu, })


# 日志拷贝（远程）-页面
@login_required
@csrf_exempt
def copy_log_remote_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "cygj"
    sub_menu = "cygj_rzkb"

    return render(request, "plugin/log_copy_remote.html", {"main_memu": main_memu, "sub_menu": sub_menu, })


# 获取日志
@login_required
@csrf_exempt
def get_log_local(request):
    log_path = request.POST["logPath"]
    output_path = request.POST["outputPath"]
    log_type = request.POST["logType"]
    search_type = request.POST["searchType"]
    time_begin = request.POST["timeBegin"]
    interval = request.POST["interval"]
    keyword = request.POST["keyword"]

    print log_path,output_path,log_type,search_type,time_begin,interval,keyword

    #print chardet.detect(keyword)

    log_preview_all = str("")
    for root, dirs, files in os.walk(log_path):
        for file_ in files:
            log_preview_all = log_preview_all + str(file_ + "<br><br>")
            log_file = os.path.join(root, file_)
            if search_type == "time_type":
                if time_begin.replace(" ","") != "":
                    log_1000 = services.cut_log(log_type,log_file,time_begin,int(interval))
                    log_preview_all = log_preview_all+ log_1000 + "<br><br><br>".encode("gb2312")

            if search_type == "keyword_type":
                if keyword.replace(" ","") != "":
                    log_1000 = services.search_log(log_type,log_file,keyword)
                    log_preview_all = log_preview_all + log_1000 + "<br><br><br>".encode("gb2312")

    #print chardet.detect(log_1000)
    return HttpResponse(log_preview_all)


# 获取日志
@login_required
@csrf_exempt
def get_log_remote(request):
    log_path = request.POST["logPath"]
    output_path = request.POST["outputPath"]
    log_type = request.POST["logType"]
    search_type = request.POST["searchType"]
    time_begin = request.POST["timeBegin"]
    interval = request.POST["interval"]
    keyword = request.POST["keyword"]

    print log_path,output_path,log_type,search_type,time_begin,interval,keyword

    #print chardet.detect(keyword)

    log_preview_all = ""
    for root, dirs, files in os.walk(log_path):
        for file_ in files:
            log_file = os.path.join(root, file_)
            if search_type == "time_type":
                if time_begin.replace(" ","") != "":
                    log_1000 = services.cut_log(log_type,log_file,time_begin,int(interval))
                    if chardet.detect(log_1000)["encoding"].lower() == "iso-8859-1":
                        log_preview_all = log_preview_all + log_1000.decode("iso-8859-1")
                    elif chardet.detect(log_1000)["encoding"].lower() == "utf-8":
                        log_preview_all = log_preview_all + log_1000.decode("utf-8")
                    else:
                        log_preview_all = log_preview_all + log_1000.decode("gbk")


            if search_type == "keyword_type":
                if keyword.replace(" ","") != "":
                    log_1000 = services.search_log(log_type,log_file,keyword)
                    log_preview_all = log_1000

    #print chardet.detect(log_preview_all)
    #return HttpResponse(log_preview_all)
    #print log_preview_all
    return render(request, "plugin/log_copy_remote.html",{"context":log_preview_all})