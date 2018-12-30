# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
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
                  create_time=create_time, deploy_args=upload_file)
    order.save()

    return HttpResponseRedirect("/sky/deploy/listOrder")

