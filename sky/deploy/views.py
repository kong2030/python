# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.utils.safestring import mark_safe
import os
import sys
import datetime
import random
import string
import traceback
import logging

from django.db import transaction
import json
from models import *
import services
import cmdb.services


# Create your views here.

# 全局变量定义
global DEPLOY_FILE_PATH
DEPLOY_FILE_PATH = r"D:\backup\deploy"


# 发布单列表
@login_required
def list_order_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "fbd"
    sub_menu = "fbd_lb"

    #orders = Order.objects.all()
    app_systems = cmdb.services.get_apps_by_user(request.user)
    orders = Order.objects.filter(app_system__in=app_systems)

    return render(request, "deploy/order_list.html", {"main_memu": main_memu, "sub_menu": sub_menu, "orders": orders})


# 发布单新增页面
@login_required
def add_order_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "fbd"
    sub_menu = "fbd_xjfbd"

    #app_systems = AppSystem.objects.all()
    app_systems = cmdb.services.get_apps_by_user(request.user)
    return render(request, "deploy/order_add.html", {"main_memu": main_memu, "sub_menu": sub_menu, "appSystems": app_systems})


# 发布单新增页面 sql
@login_required
def add_order_sql_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "fbd"
    sub_menu = "fbd_xjfbd_sql"

    #app_systems = AppSystem.objects.all()
    app_systems = cmdb.services.get_apps_by_user(request.user)
    return render(request, "deploy/order_add_sql.html", {"main_memu": main_memu, "sub_menu": sub_menu, "appSystems": app_systems})


# 发布单入库
@login_required
@csrf_exempt
def save_order(request):
    try:
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        order_code = (now_time + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)).upper()
        app_name = request.POST["appSystem"].replace(" ", "")
        app_system = AppSystem.objects.filter(app_name=app_name)[0]
        module_name = request.POST["module"].replace(" ", "")
        module = Module.objects.filter(module_name=module_name)[0]
        order_type = request.POST["orderType"].replace(" ", "")
        creator = request.user
        create_time = datetime.datetime.now()
        update_time = create_time
        remark = request.POST["remark"]

        # 获取上传文件并保存
        update_file = request.FILES.get("updateFile")
        upload_path = DEPLOY_FILE_PATH
        if not os.path.exists(upload_path):
            os.mkdir(upload_path)
        # file_name = order_code + "." + update_file.name.split(".")[-1]
        file_name = order_code + ".zip"
        upload_file = os.path.join(upload_path, file_name)
        with open(upload_file, "wb") as f:
            for chunk in update_file.chunks():
                f.write(chunk)

        order = Order(order_code=order_code, app_system=app_system, module=module, type=order_type, creator=creator,
                      create_time=create_time, deploy_args=upload_file, update_time=update_time, remark=remark)
        # 发布单入库保存
        order.save()
        return HttpResponse("success")
    except Exception as e:
        print e
        return HttpResponse("error")


# 环境流转页
@login_required
def change_order_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "bsfb"
    sub_menu = "bsfb_hjlz"

    #orders = Order.objects.all().exclude(Q(env_1=1) | Q(env_2=1) | Q(env_3=1) | Q(env_4=1) | Q(env_5=1))
    app_systems = cmdb.services.get_apps_by_user(request.user)
    orders = Order.objects.filter(app_system__in=app_systems).exclude(Q(env_1=1) | Q(env_2=1) | Q(env_3=1) | Q(env_4=1) | Q(env_5=1))
    envs = Environment.objects.all()
    return render(request, "deploy/order_status.html", {"main_memu": main_memu, "sub_menu": sub_menu, "orders": orders, "envs": envs})


# 环境流转
@login_required
@csrf_exempt
def change_order(request):
    try:
        env_id = int(request.POST["env_id"])
        order_code = request.POST["order_code"]

        order = Order.objects.filter(order_code=order_code)[0]
        order.update_time = datetime.datetime.now()
        order.current_env = env_id
        # 获取对应的环境，使用反射功能
        arg_name = "env_" + str(env_id)
        setattr(order, arg_name, 1)
        # 更新数据库
        order.save()
        return HttpResponse("success")
    except Exception as e:
        print e
        return HttpResponse("error")


# 开始发布页列表
@login_required
@csrf_exempt
def list_deploy_order_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "bsfb"
    sub_menu = "bsfb_ksfb"

    # 过滤刚新建还没流转的发布单
    #orders = Order.objects.all().exclude(env_1=0, env_2=0, env_3=0, env_4=0, env_5=0)
    app_systems = cmdb.services.get_apps_by_user(request.user)
    orders = Order.objects.filter(app_system__in=app_systems).exclude(env_1=0, env_2=0, env_3=0, env_4=0, env_5=0)
    for order in orders:
        env_id = order.current_env
        env_name = Environment.objects.filter(env_id=env_id)[0].env_name
        # 获取对应的环境，使得反射技术
        arg_name = "env_" + str(env_id)
        arg_name_value = getattr(order, arg_name)
        if arg_name_value == 1:
            order.env_status = env_name + " 待发布"
            order.deploy_status = 1
        if arg_name_value == 2:
            order.env_status = env_name + " 已发布"
            order.deploy_status = 2

    return render(request, "deploy/order_deploy_list.html", {"main_memu": main_memu, "sub_menu": sub_menu, "orders": orders})


# 开始发布页面
@login_required
@csrf_exempt
def deploy_order_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "bsfb"
    sub_menu = "bsfb_ksfb"

    order_code = request.GET["orderCode"]
    order = Order.objects.filter(order_code=order_code)[0]
    module = order.module
    current_env = order.current_env
    env_name = Environment.objects.filter(env_id=current_env)[0].env_name
    module_name = module.module_name
    # 获取组件某个环境下包含的主机
    env = Environment.objects.filter(env_id=current_env)[0]
    # ManyToMany取值
    hosts = module.host_set.filter(environment=env)

    # 获取此order完整状态
    order_status_all = mark_safe(services.get_order_status_all(order_code))

    # 发布页的页面封装类
    class DeployModel(object):
        pass

    deploy_model_list = []
    # 使用反射获取对应环境
    arg_name = "env_" + str(current_env)
    order_status = getattr(order, arg_name)
    # 1：表示此发布单还没发布过
    if order_status == 1:
        for host in hosts:
            deploy_model = DeployModel()
            deploy_model.host_ip = host.ip
            deploy_model.deploy_status = mark_safe('<span class="label label-primary">未发布</span>')
            deploy_model_list.append(deploy_model)
    # 2：表示此发布单发布过，但不一定是所有主机都有发布
    if order_status == 2:
        for host in hosts:
            host_ip = host.ip
            deploy_model = DeployModel()
            deploy_model.host_ip = host_ip
            # 取最新发布状态
            order_host = OrderHost.objects.filter(order_code=order_code, host_ip=host_ip).order_by("-deploy_time")
            if order_host.exists():
                deploy_model.deploy_time = order_host[0].deploy_time
                deploy_model.deploy_log = order_host[0].deploy_log
                if order_host[0].deploy_status == 0:
                    deploy_model.deploy_status = mark_safe('<span class="label label-danger">部署失败</span>')
                elif order_host[0].deploy_status == 1:
                    deploy_model.deploy_status = mark_safe('<span class="label label-success">部署成功</span>')
                elif order_host[0].deploy_status == 2:
                    deploy_model.deploy_status = mark_safe('<span class="label label-danger">回滚失败</span>')
                else:
                    deploy_model.deploy_status = mark_safe('<span class="label label-info">回滚成功</span>')

            else:
                deploy_model.deploy_status = mark_safe('<span class="label label-primary">未发布</span>')
            deploy_model_list.append(deploy_model)

    return render(request, "deploy/order_deploy.html", {"main_memu": main_memu, "sub_menu": sub_menu, "deploy_model_list": deploy_model_list,
                                                        "order_code":order_code, "module_name": module_name, "env_name":env_name, "current_env":current_env, "order_status_all":order_status_all})


# sql发布页面
@login_required
@csrf_exempt
def deploy_order_sql_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "bsfb"
    sub_menu = "bsfb_ksfb"

    order_code = request.GET["orderCode"]
    sql_file_list = services.get_order_sql_files(order_code)
    order = Order.objects.filter(order_code=order_code)[0]
    module = order.module
    current_env = order.current_env
    env_name = Environment.objects.filter(env_id=current_env)[0].env_name
    module_name = module.module_name
    # 获取组件某个环境下包含的主机
    env = Environment.objects.filter(env_id=current_env)[0]
    # ManyToMany取值
    hosts = module.host_set.filter(environment=env)

    # 发布页的页面封装类
    class DeployModel(object):
        pass

    deploy_model_list = []
    # 使用反射获取对应环境
    arg_name = "env_" + str(current_env)
    order_status = getattr(order, arg_name)
    # 1：表示此发布单还没发布过
    if order_status == 1:
        for host in hosts:
            deploy_model = DeployModel()
            deploy_model.host_ip = host.ip
            deploy_model.deploy_status = mark_safe('<span class="label label-primary">未发布</span>')
            # 还没发布过的，部署按键才可用
            deploy_btn_status = 1
            deploy_model_list.append(deploy_model)
    # 2：表示此发布单发布过，但不一定是所有主机都有发布
    if order_status == 2:
        for host in hosts:
            host_ip = host.ip
            deploy_model = DeployModel()
            deploy_model.host_ip = host_ip
            # 取最新发布状态
            order_host = OrderHost.objects.filter(order_code=order_code, host_ip=host_ip).order_by("-deploy_time")
            if order_host.exists():
                deploy_model.deploy_time = order_host[0].deploy_time
                deploy_model.deploy_log = order_host[0].deploy_log
                # 还没发布过的，部署按键才可用
                deploy_btn_status = 0
                if order_host[0].deploy_status == 1:
                    deploy_model.deploy_status = mark_safe('<span class="label label-success">部署成功</span>')
                else:
                    deploy_model.deploy_status = mark_safe('<span class="label label-danger">部署失败</span>')
            else:
                deploy_model.deploy_status = mark_safe('<span class="label label-primary">未发布</span>')
            deploy_model_list.append(deploy_model)

    return render(request, "deploy/order_deploy_sql.html", {"main_memu": main_memu, "sub_menu": sub_menu, "deploy_model_list": deploy_model_list,
                                                        "order_code": order_code, "module_name": module_name,"deploy_btn_status": deploy_btn_status,
                                                        "env_name": env_name, "current_env": current_env, "sql_file_list":sql_file_list})


# 开始发布
@login_required
@csrf_exempt
def save_deploy(request):
    try:
        # 获取前端传过来的数组
        deploy_checked = request.POST.getlist("deployChecked")
        order_code = request.POST["orderCode"]
        current_env = request.POST["currentEnv"]
        module_name = request.POST["moduleName"]
        # 先取对应发布单
        order = Order.objects.filter(order_code=order_code)[0]

        # 事务操作，一起更新数据库
        with transaction.atomic():
            for host_ip in deploy_checked:
                # 对应主机
                host = Host.objects.filter(ip=host_ip)[0]

                # 发布函数
                flag, log_str = services.deploy(order, host)

                # 数据库更新
                order_host = OrderHost()
                order_host.order_code = order_code
                order_host.host_ip = host_ip
                order_host.module_name = module_name
                if flag == 0:
                    order_host.deploy_status = 1
                else:
                    order_host.deploy_status = 0
                order_host.deploy_time = datetime.datetime.now()
                order_host.deploy_log = log_str
                # 发布记录入库
                order_host.save()
            # 发布单表状态更新
            arg_name = "env_" + str(current_env)
            setattr(order, arg_name, 2)
            order.update_time = datetime.datetime.now()
            order.save()

        if flag == 0:
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    except Exception as e:
        print e
        logging.exception("EXCEPTION")
        return HttpResponse("error")


# 开始发布sql
@login_required
@csrf_exempt
def save_deploy_sql(request):
    try:
        order_code = request.POST["orderCode"]
        host_ip = request.POST["hostIp"]
        current_env = request.POST["currentEnv"]
        module_name = request.POST["moduleName"]
        # 先取对应发布单
        order = Order.objects.filter(order_code=order_code)[0]

        # 事务操作，一起更新数据库
        with transaction.atomic():
            # 对应主机
            host = Host.objects.filter(ip=host_ip)[0]

            # 发布函数
            flag, log_str = services.deploy(order, host)

            # 数据库更新
            order_host = OrderHost()
            order_host.order_code = order_code
            order_host.host_ip = host_ip
            order_host.module_name = module_name
            if flag == 0:
                order_host.deploy_status = 1
            else:
                order_host.deploy_status = 0
            order_host.deploy_time = datetime.datetime.now()
            order_host.deploy_log = log_str
            # 发布记录入库
            order_host.save()
            # 发布单表状态更新
        arg_name = "env_" + str(current_env)
        setattr(order, arg_name, 2)
        order.update_time = datetime.datetime.now()
        order.save()

        if flag == 0:
            return HttpResponse("success")
        else:
            return HttpResponse("error")

    except Exception as e:
        traceback.print_exc()
        logging.exception("EXCEPTION")
        return HttpResponse("error")


# 回滚入库
@login_required
@csrf_exempt
def save_rollback(request):
    try:
        # 获取前端传过来的数组
        deploy_checked = request.POST.getlist("deployChecked")
        order_code = request.POST["orderCode"]
        current_env = request.POST["currentEnv"]
        module_name = request.POST["moduleName"]
        # 先取对应发布单
        order = Order.objects.filter(order_code=order_code)[0]

        # 事务操作，一起更新数据库
        with transaction.atomic():
            for host_ip in deploy_checked:
                # 对应主机
                host = Host.objects.filter(ip=host_ip)[0]

                # 回滚函数
                flag, log_str = services.rollback(order, host)

                # 数据库更新
                order_host = OrderHost()
                order_host.order_code = order_code
                order_host.host_ip = host_ip
                order_host.module_name = module_name
                if flag == 0:
                    order_host.deploy_status = 3
                else:
                    order_host.deploy_status = 2
                order_host.deploy_time = datetime.datetime.now()
                order_host.deploy_log = log_str
                # 发布记录入库
                order_host.save()

        if flag == 0:
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    except Exception as e:
        print e
        return HttpResponse("error")


# md5校验
@login_required
@csrf_exempt
def md5_check(request):
    # 获取前端传过来的数据
    host_ip = request.POST["hostIp"]
    order_code = request.POST["orderCode"]

    host = Host.objects.filter(ip=host_ip)[0]
    order = Order.objects.filter(order_code=order_code)[0]

    md5_form_list, result_all = services.md5_check(order, host)

    result = {"md5_form_list": md5_form_list, "result_all": result_all}

    return HttpResponse(json.dumps(result), content_type="application/json")