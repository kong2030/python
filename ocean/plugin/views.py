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
from cmdb.models import *
import json

# Create your views here.

# 日志搜索（本地）-页面
@login_required
@csrf_exempt
def search_log_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "cygj"
    sub_menu = "cygj_rzss_local"

    app_systems = AppSystem.objects.all()

    return render(request, "plugin/log_search.html", {"main_memu": main_memu, "sub_menu": sub_menu, "appSystems":app_systems})


# 日志拷贝-页面
@login_required
@csrf_exempt
def copy_log_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "cygj"
    sub_menu = "cygj_rzkb"

    return render(request, "plugin/log_copy.html", {"main_memu": main_memu, "sub_menu": sub_menu, })


# 获取日志
@login_required
@csrf_exempt
def get_log_local(request):
    try:
        log_path = request.POST["logPath"]
        output_path = request.POST["outputPath"]
        log_type = request.POST["logType"]
        search_type = request.POST["searchType"]
        time_begin = request.POST["timeBegin"]
        interval = request.POST["interval"]
        keyword = request.POST["keyword"]

        #print log_path,output_path,log_type,search_type,time_begin,interval,keyword

        log_preview_all = ""
        for root, dirs, files in os.walk(log_path):
            for file_ in files:
                try:
                    log_file = os.path.join(root, file_)
                    log_1000 = ""
                    count = 0
                    if search_type == "time_type":
                        if time_begin.replace(" ","") != "":
                            log_1000, count = services.cut_log(log_type,log_file,time_begin,int(interval), output_path)

                    if search_type == "keyword_type":
                        if keyword.replace(" ","") != "":
                            log_1000, count = services.search_log(log_type,log_file,keyword, output_path)

                    log_preview_all = log_preview_all + file_ + "  count:"+ str(count) +"<br><br>"
                    if chardet.detect(log_1000)["encoding"] is not None:
                        if chardet.detect(log_1000)["encoding"].lower() == "iso-8859-1":
                            log_preview_all = log_preview_all + log_1000.decode("iso-8859-1")
                        elif chardet.detect(log_1000)["encoding"].lower() == "utf-8":
                            log_preview_all = log_preview_all + log_1000.decode("utf-8")
                        else:
                            log_preview_all = log_preview_all + log_1000.decode("gbk")
                    else:
                        log_preview_all = log_preview_all + log_1000.decode("iso-8859-1")

                    log_preview_all = log_preview_all + "<br><br>"

                except Exception as e:
                    log_preview_all = log_preview_all + str(e) + "<br><br>"
        #print chardet.detect(log_preview_all)
    except Exception as e:
        log_preview_all = str(e)
    finally:
        return render(request, "plugin/log_detail.html",{"content":log_preview_all})


# 获取日志
@login_required
@csrf_exempt
def get_log_remote(request):
    try:
        module_name = request.POST["module"]
        output_path = request.POST["outputPath"]
        log_type = request.POST["logType"]
        search_type = request.POST["searchType"]
        datetime_str = request.POST["timeBegin"]

        interval = request.POST["interval"]
        keyword = request.POST["keyword"]

        #print module_name,output_path,log_type,search_type,datetime_str,interval,keyword

        module = Module.objects.filter(module_name=module_name)[0]
        module_kwargs = json.loads(module.kwargs)
        log_path = module_kwargs["log_path"]
        # ManyToMany取值
        hosts = module.host_set.all()

        log_preview_all = ""
        for host in hosts:
            try:
                log_1000 = ""
                count = 0
                if search_type == "time_type":
                    if datetime_str.replace(" ", "") != "":
                        log_1000, count = services.cut_log_remote(log_type,host,log_path, datetime_str, int(interval),output_path)

                if search_type == "keyword_type":
                    if keyword.replace(" ", "") != "":
                        pass

                log_preview_all = log_preview_all + host.ip + "  count:" + str(count) + "<br><br>"
                if chardet.detect(log_1000)["encoding"] is not None:
                    if chardet.detect(log_1000)["encoding"].lower() == "iso-8859-1":
                        log_preview_all = log_preview_all + log_1000.decode("iso-8859-1")
                    elif chardet.detect(log_1000)["encoding"].lower() == "utf-8":
                        log_preview_all = log_preview_all + log_1000.decode("utf-8")
                    else:
                        log_preview_all = log_preview_all + log_1000.decode("gbk")
                else:
                    log_preview_all = log_preview_all + log_1000.decode("iso-8859-1")

                log_preview_all = log_preview_all + "<br><br>"

            except Exception as e:
                log_preview_all = log_preview_all + str(e) + "<br><br>"

    except Exception as e:
        log_preview_all = str(e)
    finally:
        return render(request, "plugin/log_detail.html",{"content":log_preview_all})