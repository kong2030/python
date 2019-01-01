# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
import os
import datetime
import random
import string

from models import *

# Create your views here.


# 发布单列表
@login_required
def list_order(request):
    orders = Order.objects.all()

    return render(request, "deploy/order_list.html", {"orders": orders})


# 发布单新增页面
@login_required
def add_order(request):
    app_systems = AppSystem.objects.all()
    return render(request, "deploy/order_add.html", {"appSystems": app_systems})


# 发布单入库
@login_required
@csrf_exempt
def save_order(request):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    order_code = (now_time + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)).upper()
    app_name = request.POST["appSystem"].replace(" ", "")
    app_system = AppSystem.objects.filter(app_name=app_name)[0]
    module_name = request.POST["module"].replace(" ", "")
    module = Module.objects.filter(module_name=module_name)[0]
    creator = request.user
    create_time = datetime.datetime.now()
    update_time = create_time

    # 获取上传文件并保存
    update_file = request.FILES.get("updateFile")
    upload_path = "/Users/yangwenren/Desktop/install/upload"
    if not os.path.exists(upload_path):
        os.mkdir(upload_path)
    file_name = order_code + "." + update_file.name.split(".")[1]
    upload_file = os.path.join(upload_path, file_name)
    with open(upload_file, "wb") as f:
        for chunk in update_file.chunks():
            f.write(chunk)

    order = Order(order_code=order_code, app_system=app_system, module=module, type=1, creator=creator,
                  create_time=create_time, deploy_args=upload_file, update_time=update_time)
    order.save()

    return HttpResponseRedirect("/sky/deploy/listOrder")


# 环境流转页
@login_required
def change_order_page(request):
    orders = Order.objects.all().exclude(Q(env_1=1) | Q(env_2=1) | Q(env_3=1) | Q(env_4=1) | Q(env_5=1))
    envs = Environment.objects.all()
    return render(request, "deploy/order_status.html", {"orders": orders, "envs": envs})


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
        # 获取对应的环境
        if env_id == 1:
            order.env_1 = 1
        elif env_id == 2:
            order.env_2 = 1
        elif env_id == 3:
            order.env_3 = 1
        elif env_id == 4:
            order.env_4 = 1
        elif env_id == 5:
            order.env_5 = 1
        # 更新数据库
        order.save()
        return HttpResponse("success")
    except Exception as e:
        print e
        return HttpResponse("error")


# 开始发布页
@login_required
@csrf_exempt
def list_deploy_order(request):
    # 过滤刚新建还没流转的发布单
    orders = Order.objects.all().exclude(env_1=0, env_2=0, env_3=0, env_4=0, env_5=0)
    for order in orders:
        env_id = order.current_env
        env_name = Environment.objects.filter(env_id=env_id)[0].env_name
        # 获取对应的环境
        if env_id == 1:
            if order.env_1 == 1:
                order.env_status = "测试环境 待发布"
                order.deploy_status = 1
            if order.env_1 == 2:
                order.env_status = "测试环境 已发布"
                order.deploy_status = 2
        elif env_id == 2:
            if order.env_2 == 1:
                order.env_status = "预发环境 待发布"
                order.deploy_status = 1
            if order.env_2 == 2:
                order.env_status = "预发环境 已发布"
                order.deploy_status = 2
        elif env_id == 3:
            if order.env_3 == 1:
                order.env_status = "生产环境 待发布"
                order.deploy_status = 1
            if order.env_3 == 2:
                order.env_status = "生产环境 已发布"
                order.deploy_status = 2
        elif env_id == 4:
            if order.env_4 == 1:
                order.env_status = "同城灾备 待发布"
                order.deploy_status = 1
            if order.env_4 == 2:
                order.env_status = "同城灾备 已发布"
                order.deploy_status = 2
        elif env_id == 5:
            if order.env_5 == 1:
                order.env_status = "异地灾备 待发布"
                order.deploy_status = 1
            if order.env_5 == 2:
                order.env_status = "异地灾备 已发布"
                order.deploy_status = 2

    return render(request, "deploy/order_deploy_list.html", {"orders": orders})