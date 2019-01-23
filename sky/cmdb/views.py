# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import base64
import json

from models import *


reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.


# 加密工具页面
@login_required
def encrypt_page(request):
    return render(request, 'cmdb/encrypt.html')


# 返回加密后的密码串，再保存数据库
@login_required
@csrf_exempt
def encrypt(request):
    password = request.POST["password"]
    if len(password) >= 8:
        # 加密
        new_password = password[-1] + password[-2] + password[2:-2] + password[1] + password[0]
        encrypt_str = base64.encodestring(new_password)

        # 解密
        decode_str = base64.decodestring(encrypt_str)
        password = decode_str[-1] + decode_str[-2] + decode_str[2:-2] + decode_str[1] + decode_str[0]
    else:
        password = "the password is too simple"
        encrypt_str = ""

    result = {"password": password, "encrypt_str": encrypt_str}
    return HttpResponse(json.dumps(result), content_type="application/json")


# 组件列表
@login_required
def list_module_page(request):
    modules = Module.objects.all()

    return render(request, "cmdb/module_list.html", {"modules": modules})


# 组件新增页面
@login_required
def add_module_page(request):
    app_systems = AppSystem.objects.all()
    return render(request, "cmdb/module_add.html", {"appSystems": app_systems})


# 组件编辑页面
@login_required
def edit_module_page(request):
    module_id = request.GET["moduleId"]
    module = Module.objects.filter(id=module_id)[0]

    app_systems = AppSystem.objects.all()

    # ManyToMany取值
    hosts = module.host_set.all()

    return render(request, "cmdb/module_edit.html", {"module": module, "appSystems": app_systems, "hosts": hosts})


# 组件信息入库
@login_required
@csrf_exempt
def save_module(request):
    try:
        # 先获取参数
        module_id = request.POST["moduleId"]
        module_name = request.POST["moduleName"].upper().replace(" ", "")
        chinese_name = request.POST["chineseName"].replace(" ", "")
        program_path = request.POST["programPath"].replace(" ", "")
        script_path = request.POST["scriptPath"].replace(" ", "")
        app_name = request.POST["appSystem"].replace(" ", "")
        app_system = AppSystem.objects.filter(app_name=app_name)[0]

        # 更新数据库
        update_field = {"module_name": module_name, "chinese_name": chinese_name, "program_path": program_path,\
                        "script_path": script_path, "app_system": app_system}
        Module.objects.update_or_create(id=module_id, defaults=update_field)

    except Exception as e:
        print e

    finally:
        return HttpResponseRedirect("/sky/cmdb/listModule")


# 通过系统名来查询组件
@login_required
@csrf_exempt
def get_modules_by_app(request):
    app_name = request.POST["app_name"]
    order_type = request.POST["order_type"]
    app_system = AppSystem.objects.filter(app_name=app_name)
    modules = Module.objects.filter(app_system=app_system)

    # 如果是Sql发布单，就只列出对应的组件供选择
    result = ""
    for obj in modules:
        module_name = obj.module_name
        if order_type == "1":
            if not module_name.endswith("SQL"):
                result = result + module_name + ","
        elif order_type == "2":
            if module_name.endswith("SQL"):
                result = result + module_name + ","

    # 去除最后一个逗号
    result = result[:-1]
    return HttpResponse(result)