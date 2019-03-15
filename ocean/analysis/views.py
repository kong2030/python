# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

from models import *
from services import *
# Create your views here.


# 统计分析页面
@login_required
def analysis_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "tjfx"
    sub_menu = "tjfx_page"
    return render(request, 'analysis/analysis_page.html', {"main_memu":main_memu, "sub_menu": sub_menu})


# 加载数据
@login_required
@csrf_exempt
def load_data(request):

    sql = "select * from opt_stds..OPT_ORDER"
    datasource = "qzqqjy"

    result = collect_data_qq(datasource, sql)

    return HttpResponse(result)


# 采集主机资源使用率数据
@login_required
@csrf_exempt
def collect_data(request):
    collect_path = r"D:\backup\collect_cpu"
    result = collect_data_host(collect_path)

    return HttpResponse(result)