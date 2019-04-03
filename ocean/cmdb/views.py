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
from config.models import *
import services


reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.


# 加密工具页面
@login_required
def encrypt_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "rcwh"
    sub_menu = "rcwh_mmgj"
    return render(request, 'cmdb/encrypt.html', {"main_memu":main_memu, "sub_menu": sub_menu})


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
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "rcwh"
    sub_menu = "rcwh_zjpz"

    app_systems = services.get_apps_by_user(request.user)
    modules = Module.objects.filter(app_system__in=app_systems)
    return render(request, "cmdb/module_list.html", {"main_memu":main_memu, "sub_menu": sub_menu, "modules": modules})


# 组件新增页面
@login_required
def add_module_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "rcwh"
    sub_menu = "rcwh_zjpz"

    app_systems = services.get_apps_by_user(request.user)
    return render(request, "cmdb/module_add.html", {"main_memu":main_memu, "sub_menu": sub_menu, "appSystems": app_systems})


# 组件编辑页面
@login_required
def edit_module_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "rcwh"
    sub_menu = "rcwh_zjpz"

    module_id = request.GET["moduleId"]
    module = Module.objects.filter(id=module_id)[0]

    app_systems = services.get_apps_by_user(request.user)

    # ManyToMany取值
    hosts = module.host_set.all()

    return render(request, "cmdb/module_edit.html", {"main_memu":main_memu, "sub_menu": sub_menu, "module": module, "appSystems": app_systems, "hosts": hosts})


# 组件信息入库
@login_required
@csrf_exempt
def save_module(request):
    try:
        # 先获取参数
        module_name = request.POST["moduleName"].upper().replace(" ", "")
        chinese_name = request.POST["chineseName"].replace(" ", "")
        app_name = request.POST["appSystem"].replace(" ", "")
        app_system = AppSystem.objects.filter(app_name=app_name)[0]

        module = Module(module_name=module_name,chinese_name=chinese_name, app_system=app_system)

        # 如果是编辑就加上id,
        if request.POST.has_key("moduleId"):
            module_id = request.POST["moduleId"]
            module.id = module_id

        # 更新数据库
        module.save()

    except Exception as e:
        print e

    finally:
        return HttpResponseRedirect("/ocean/cmdb/listModule")


# 通过系统名来查询组件
@login_required
@csrf_exempt
def get_modules_by_app(request):
    app_name = request.POST["app_name"]
    app_system = AppSystem.objects.filter(app_name=app_name)
    modules = Module.objects.filter(app_system=app_system)

    result = ""
    for obj in modules:
        module_name = obj.module_name
        result = result + module_name + ","

    # 去除最后一个逗号
    result = result[:-1]
    return HttpResponse(result)


# 通过组件名来查询主机
@login_required
@csrf_exempt
def get_hosts_by_module(request):
    module_name = request.POST["module_name"]
    env_id = request.POST["env_id"]
    module = Module.objects.filter(module_name=module_name)[0]

    # ManyToMany取值
    hosts = module.host_set.filter(environment=env_id)

    result = ""
    for obj in hosts:
        host_ip = obj.ip
        result = result + host_ip + ","

    # 去除最后一个逗号
    result = result[:-1]
    return HttpResponse(result)


# 用户-系统列表
@login_required
@csrf_exempt
def list_app_user_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "xtgl"
    sub_menu = "xtgl_qxgl"

    # 先把已经有记录的用户查出来
    app_users = list(UserApp.objects.all())

    #app_user_ids= UserApp.objects.values("user_id")
    app_user_ids = UserApp.objects.values_list("user_id")
    # 再把还没有记录的用户合并进来
    users = User.objects.filter(is_superuser=0).exclude(id__in=app_user_ids)
    for user in users:
        app_user = UserApp()
        app_user.user_id = user.id
        app_user.user_name = user.username
        app_user.user_code = user.userinfo.user_code
        app_users.append(app_user)

    return render(request, "cmdb/app_user_list.html", {"main_memu":main_memu, "sub_menu": sub_menu, "appUsers": app_users})


# 增加 用户-系统
@login_required
@csrf_exempt
def add_app_user_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "xtgl"
    sub_menu = "xtgl_qxgl"

    user_id = request.GET["id"]
    user = User.objects.filter(id=user_id)[0]
    app_systems = AppSystem.objects.all()

    app_users = UserApp.objects.filter(user_id=user_id)
    # 已选择与未选择
    app_selected = []
    app_unselected = []
    if app_users:
        app_user = app_users[0]
        app_ids = app_user.app_id
        app_id_selected_list = app_ids.split(",")
        for app_system in app_systems:
            if str(app_system.id) in app_id_selected_list:
                app_selected.append(app_system)
            else:
                app_unselected.append(app_system)
    else:
        app_unselected = app_systems
    return render(request, "cmdb/app_user_add.html", {"main_memu":main_memu, "sub_menu": sub_menu, "user": user, "appSelected": app_selected, "appUnselected": app_unselected})


# 用户-系统 入库
@login_required
@csrf_exempt
def save_app_user(request):
    user_id = request.POST["userId"]
    user_name = request.POST["userName"]
    user_code = request.POST["userCode"]
    app_select_list = request.POST.getlist("app_multi_selects")

    app_id = ""
    app_name = ""
    for app_select in app_select_list:
        app_system = AppSystem.objects.filter(id=app_select)[0]
        app_id = app_id + "," + app_select
        app_name = app_name + "," + app_system.chinese_name
    # 去掉第一个 ","
    app_id = app_id[1:]
    app_name = app_name[1:]

    update_field = {"user_id": user_id, "user_code": user_code, "user_name": user_name, "app_id":app_id, "app_name":app_name}

    UserApp.objects.update_or_create(user_id=user_id, defaults=update_field)

    return HttpResponseRedirect("/ocean/cmdb/listAppUser")