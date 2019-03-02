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
from article.models import *
# Create your views here.


# 监控状态页面
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


# 监控配置页面
@login_required
def list_task_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "ywjk"
    sub_menu = "ywjk_jkpz"

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
        else:
            task_state_form["last_run_time"] = task.last_run_at

        task_state_form_list.append(task_state_form)

    return render(request, "monitor/task_list.html",{"main_memu": main_memu, "sub_menu": sub_menu, "tasks": task_state_form_list})


# 新增监控页面
@login_required
def add_task_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "ywjk"
    sub_menu = "ywjk_jkpz"

    datasources = DataBaseInfo.objects.all()
    crontabs = CrontabSchedule.objects.all()
    return render(request, "monitor/task_add.html",{"main_memu": main_memu, "sub_menu": sub_menu, 'crontabs':crontabs, 'datasources':datasources })


# 编辑监控页面
@login_required
@csrf_exempt
def edit_task_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "ywjk"
    sub_menu = "ywjk_jkpz"

    # 获取任务参数
    task_id = request.GET["taskId"]
    task = PeriodicTask.objects.filter(id=task_id)[0]
    task_kwargs = None
    articles = None
    if task.kwargs != "{}":
        task_kwargs = eval(task.kwargs)
        task_kwargs["crontab_id"] = task.crontab_id
        task_kwargs["enabled"] = task.enabled
        task_kwargs["id"] = task_id

        # 获取所有文章列表
        datasource = task_kwargs["datasource"]
        database_infos = DataBaseInfo.objects.filter(name=datasource)
        if database_infos.exists():
            app_system = database_infos[0].app_system
            articles = Article.objects.filter(app_system=app_system)
    else:
        task_kwargs = dict()
        task_kwargs["crontab_id"] = task.crontab_id
        task_kwargs["enabled"] = task.enabled
        task_kwargs["id"] = task_id
        task_kwargs["name"] = task.name


    # 获取数据源列表
    datasources = DataBaseInfo.objects.all()
    # 获取 执行时间 列表
    crontabs = CrontabSchedule.objects.all()
    return render(request, "monitor/task_edit.html",{"main_memu": main_memu, "sub_menu": sub_menu,"task":task_kwargs, 'crontabs': crontabs, 'datasources': datasources, "articles":articles})


# 保存监控任务
@login_required
@csrf_exempt
def save_task(request):
    try:
        # 先获取参数
        task_name = request.POST["taskName"].replace(" ", "")
        crontab_id = request.POST["crontab"]
        datasource = request.POST["datasource"]
        sql = request.POST["sql"]
        operator = request.POST["operator"]
        threshold = request.POST["threshold"]

        # 任务模板，默认先取这个
        monitor_task = "monitor.tasks.monitor_sql"

        kwargs = dict()
        kwargs["name"] = task_name
        kwargs["datasource"] = datasource
        kwargs["sql"] = sql
        kwargs["operator"] = operator
        kwargs["threshold"] = int(threshold)

        # 编辑页面 还可以关联文章
        if request.POST.has_key("article"):
            article = request.POST["article"]
            if article != "" and article is not None:
                kwargs["article"] = int(article)

        json_str = json.dumps(kwargs, ensure_ascii=False)

        periodic_task = PeriodicTask(name=task_name, task=monitor_task, kwargs=json_str, crontab_id=crontab_id)

        # 如果是编辑就加上id,
        if request.POST.has_key("taskId"):
            task_id = request.POST["taskId"]
            periodic_task.id = task_id
            if request.POST.has_key("enabled"):
                enabled = request.POST["enabled"]
                periodic_task.enabled = enabled
            else:
                periodic_task.enabled = 0

        # 更新数据库
        periodic_task.save()

    except Exception as e:
        print e

    finally:
        return HttpResponseRedirect("/ocean/monitor/listTask")


@login_required
def view_monitor(request, id):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "ywjk"
    sub_menu = "ywjk_jkzt"

    task = PeriodicTask.objects.filter(id=id)[0]
    task_kwargs = json.loads(task.kwargs)
    task_form = dict()
    task_form["name"] = task.name
    if task_kwargs.has_key("datasource"):
        task_form["datasource"] = task_kwargs["datasource"]
    if task_kwargs.has_key("sql"):
        task_form["sql"] = task_kwargs["sql"]
    if task_kwargs.has_key("operator"):
        if task_kwargs["operator"] == "==":
            task_form["operator"] = "查询结果不变"
        elif task_kwargs["operator"] == ">=":
            task_form["operator"] = "符合记录数达到阈值"
        elif task_kwargs["operator"] == "<":
            task_form["operator"] = "符合记录数小于阈值"
    if task_kwargs.has_key("threshold"):
        task_form["threshold"] = task_kwargs["threshold"]
    if task_kwargs.has_key("article"):
        articles = Article.objects.filter(id=task_kwargs["article"])
        if articles.exists():
            article = articles[0]
            task_form["article_title"] = article.title
            task_form["article_id"] = article.id

    #today_str = datetime.datetime.today().strftime("%Y-%m-%d")
    today_str =(datetime.datetime.today() + datetime.timedelta(days=-2)).strftime("%Y-%m-%d")
    tomorrow_str = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    time_1 = datetime.datetime.strptime(today_str, '%Y-%m-%d')
    time_2 = datetime.datetime.strptime(tomorrow_str, '%Y-%m-%d')

    task_monitor_graph_data = dict()
    x_data_list_time = list(TaskResult.objects.filter(task_id=id,last_run_time__gt=time_1,last_run_time__lt=time_2).values_list('last_run_time', flat=True).order_by('last_run_time'))
    task_monitor_graph_data["x_data"] = [obj.strftime("%H:%M") for obj in x_data_list_time]
    task_monitor_graph_data["y_data"] = list(TaskResult.objects.filter(task_id=id,last_run_time__gt=time_1,last_run_time__lt=time_2).values_list('monitor_result', flat=True).order_by('last_run_time'))



    return render(request, "monitor/task_monitor_detail.html",
                  {"main_memu": main_memu, "sub_menu": sub_menu, "task": task_form, "task_monitor_graph_data":task_monitor_graph_data})