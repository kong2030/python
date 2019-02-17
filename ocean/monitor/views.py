# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from djcelery.models import PeriodicTask, CrontabSchedule

# Create your views here.


@login_required
def task_status_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "ywjk"
    sub_menu = "ywjk_jkzt"

    tasks = PeriodicTask.objects.all()
    return render(request, "monitor/task_status.html",{"main_memu": main_memu, "sub_menu": sub_menu, "tasks": tasks})

@login_required
def list_task_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "ywjk"
    sub_menu = "ywjk_jkzt"

    tasks = PeriodicTask.objects.all()
    return render(request, "monitor/task_list.html",{"main_memu": main_memu, "sub_menu": sub_menu, "tasks": tasks})


def add_task_page(request):
    pass


def edit_task_page(request):
    pass


def save_task(request):
    pass
