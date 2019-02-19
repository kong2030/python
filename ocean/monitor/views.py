# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from djcelery.models import PeriodicTask, CrontabSchedule
import json
from django.utils.safestring import mark_safe
import datetime

from models import *
# Create your views here.


@login_required
def task_status_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "ywjk"
    sub_menu = "ywjk_jkzt"

    tasks = PeriodicTask.objects.all()
    task_state_form_list = []
    for task in tasks:
        task_state_form = dict()
        task_state_form["id"] = task.id
        task_state_form["name"] = task.name
        task_state_form["crontab"] = task.crontab
        task_kwargs = json.loads(task.kwargs)
        if task_kwargs.has_key("datasource"):
            datasource = task_kwargs["datasource"]
            database_infos = DataBaseInfo.objects.filter(name=datasource)
            if database_infos.exists():
                task_state_form["app_system"] = database_infos[0].app_system.chinese_name
        if task.enabled == 1:
            task_state_form["enabled"] = mark_safe('<span class="label label-success">启用</span>')
        else:
            task_state_form["enabled"] = mark_safe('<span class="label label-primary">禁用</span>')
        task_results = TaskResult.objects.filter(task_id=task.id)
        if task_results.exists():
            task_result = task_results.latest('last_run_time')
            task_state_form["last_run_time"] = task_result.last_run_time
            if task_result.monitor_result == 0:
                task_state_form["monitor_result"] = mark_safe('<span class="label label-success">正常</span>')
            elif task_result.monitor_result == 1:
                task_state_form["monitor_result"] = mark_safe('<span class="label label-danger">异常</span>')
            elif task_result.monitor_result == -1:
                task_state_form["monitor_result"] = mark_safe('<span class="label label-primary">未知</span>')

        else:
            task_state_form["last_run_time"] = task.last_run_at

        task_state_form_list.append(task_state_form)


    return render(request, "monitor/task_status.html",{"main_memu": main_memu, "sub_menu": sub_menu, "tasks": task_state_form_list})

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


@login_required
def view_monitor(request, id):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "ywjk"
    sub_menu = "ywjk_jkzt"

    task = PeriodicTask.objects.filter(id=id)[0]

    #today_str = datetime.datetime.today().strftime("%Y-%m-%d")
    today_str =(datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    tomorrow_str = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    time_1 = datetime.datetime.strptime(today_str, '%Y-%m-%d')
    time_2 = datetime.datetime.strptime(tomorrow_str, '%Y-%m-%d')
    print time_1

    task_monitor_graph_data = dict()
    x_data_list_time = list(TaskResult.objects.filter(task_id=id,last_run_time__gt=time_1,last_run_time__lt=time_2).values_list('last_run_time', flat=True).order_by('last_run_time'))
    task_monitor_graph_data["x_data"] = [obj.strftime("%H:%M") for obj in x_data_list_time]
    task_monitor_graph_data["y_data"] = list(TaskResult.objects.filter(task_id=id,last_run_time__gt=time_1,last_run_time__lt=time_2).values_list('monitor_result', flat=True).order_by('last_run_time'))

    return render(request, "monitor/task_monitor_detail.html",
                  {"main_memu": main_memu, "sub_menu": sub_menu, "task":task, "task_monitor_graph_data":task_monitor_graph_data})