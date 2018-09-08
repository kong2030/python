# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import json

from models import *
from . import services

# Create your views here.


# ------------------------------ 新股日历栏目相关 begin -------------------------------

# 打开新股 新建页面
@login_required
def add_stock(request):
    underwriters = Underwriter.objects.all()
    return render(request, "stock/stock_add.html", {"underwriters": underwriters})


# 显示所有新股信息
@login_required
def list_stock(request):
    stocks = Stock.objects.all()
    for stock in stocks:
        if stock.current_status == 0:
            stock.current_status_str = "刚刚录入"
        if stock.current_status == 1:
            stock.current_status_str = "招股公告"
        if stock.current_status == 2:
            stock.current_status_str = "提交材料"
        if stock.current_status == 3:
            stock.current_status_str = "初步询价"
        if stock.current_status == 4:
            stock.current_status_str = "网下申购"
        if stock.current_status == 5:
            stock.current_status_str = "配售缴款"
        if stock.current_status == 6:
            stock.current_status_str = "等待上市"
        if stock.current_status == 7:
            stock.current_status_str = "已经上市"

    return render(request, "stock/stock_list.html", {"stocks": stocks})


# 打开新股编辑页面
@login_required
def edit_stock(request, stock_code):
    stock = Stock.objects.filter(stock_code=stock_code)[0]
    underwriters = Underwriter.objects.all()
    return render(request, "stock/stock_edit.html", {"stock": stock, "underwriters": underwriters})


# 保存新股
@login_required
@csrf_exempt
def save_stock(request):
    # 获取参数
    stock_code = request.POST["stockCode"]
    stock_name = request.POST["stockName"]
    stock_type = request.POST["stockType"]
    underwriter = Underwriter.objects.filter(underwriter=request.POST["underwriter"])[0]
    zg_start_date = datetime.datetime.strptime(request.POST["zgStartDate"], "%Y-%m-%d").date()
    zg_end_date = datetime.datetime.strptime(request.POST["zgEndDate"], "%Y-%m-%d").date()
    cl_start_date = datetime.datetime.strptime(request.POST["clStartDate"], "%Y-%m-%d").date()
    cl_end_date = datetime.datetime.strptime(request.POST["clEndDate"], "%Y-%m-%d").date()
    xj_start_date = datetime.datetime.strptime(request.POST["xjStartDate"], "%Y-%m-%d").date()
    xj_end_date = datetime.datetime.strptime(request.POST["xjEndDate"], "%Y-%m-%d").date()
    sg_start_date = datetime.datetime.strptime(request.POST["sgStartDate"], "%Y-%m-%d").date()
    sg_end_date = datetime.datetime.strptime(request.POST["sgEndDate"], "%Y-%m-%d").date()
    jk_start_date = datetime.datetime.strptime(request.POST["jkStartDate"], "%Y-%m-%d").date()
    jk_end_date = datetime.datetime.strptime(request.POST["jkEndDate"], "%Y-%m-%d").date()
    # 上市时间如果还没确定，延迟录入
    if request.POST["ssDate"] is not None and request.POST["ssDate"] != "":
        ss_date = datetime.datetime.strptime(request.POST["ssDate"], "%Y-%m-%d").date()
    else:
        ss_date = None

    # 需要更新的字段
    update_field = {"stock_name":stock_name,"stock_type":stock_type,"underwriter":underwriter,"zg_start_date":zg_start_date,\
                    "zg_end_date":zg_end_date,"cl_start_date":cl_start_date,"cl_end_date":cl_end_date,"xj_start_date":xj_start_date,\
                    "xj_end_date":xj_end_date,"sg_start_date":sg_start_date,"sg_end_date":sg_end_date,"jk_start_date":jk_start_date,\
                    "jk_end_date":jk_end_date,"ss_date":ss_date}

    stock = Stock(**update_field)
    # 设置此只新股的状态
    services.set_stock_status(stock)
    update_field["current_status"] = stock.current_status
    # 新建 或 更新 数据库
    Stock.objects.update_or_create(stock_code=stock_code, defaults=update_field)

    '''
    # 在 operation 表插入记录
    done_time = datetime.datetime.now()
    stock = Stock.objects.filter(stock_code=stock_code)[0]
    operation = Operation(stock=stock,stock_code=stock_code,stock_name=stock_name,step=1,current_status=stock.current_status,done_time=done_time)
    operation.save()

    
    stock = Stock(stock_code=stock_code,stock_name=stock_name,stock_type=stock_type,underwriter=underwriter,zg_start_date=zg_start_date, \
                  zg_end_date=zg_end_date,cl_start_date=cl_start_date,cl_end_date=cl_end_date,xj_start_date=xj_start_date,xj_end_date=xj_end_date, \
                  sg_start_date=sg_start_date,sg_end_date=sg_end_date,jk_start_date=jk_start_date,jk_end_date=jk_end_date)
    stock.save()              
    '''

    return HttpResponseRedirect("/ipoms/stock/listStock")


# 显示所有承销商
@login_required
def list_underwriter(request):
    # 获取所有承销商信息
    underwriters = Underwriter.objects.all()

    return render(request, "stock/underwriter_list.html", {"underwriters": underwriters})


# 新增承销商
@login_required
@csrf_exempt
def add_underwriter(request):
    try:
        # 获取 post 数据
        underwriter = request.POST["underwriter"].replace(" ", "")
        shortname = request.POST["shortname"].replace(" ", "")
        telephone = request.POST["telephone"].replace(" ", "")
        email = request.POST["email"].replace(" ", "")

        # 更新数据库
        Underwriter.objects.update_or_create(underwriter=underwriter, defaults={"shortname":shortname, "telephone":telephone, "email":email})

        return HttpResponse("success")

    except Exception as e:
        print e.message
        return HttpResponse("error")


# 删除承销商
@login_required
@csrf_exempt
def delete_underwriter(request):
    try:
        # 获取 post 数据
        underwriter = request.POST["underwriter"].replace(" ", "")
        shortname = request.POST["shortname"].replace(" ", "")
        telephone = request.POST["telephone"].replace(" ", "")
        email = request.POST["email"].replace(" ", "")

        # 更新数据库
        Underwriter.objects.filter(underwriter=underwriter).delete()

        return HttpResponse("success")
    except Exception as e:
        print e.message
        return HttpResponse("error")


# 显示所有产品
@login_required
def list_product(request):
    # 获取所有产品信息
    products = Product.objects.all()
    return render(request, "stock/product_list.html",{"products":products})


# 打开产品编辑页面，新增或编辑
@login_required
@csrf_exempt
def add_product(request):

    action = request.GET["action"]

    # 如果是编辑
    if action == "edit":
        product_code = request.GET["productCode"]
        products = Product.objects.filter(product_code=product_code)

        if products.exists():
            return render(request, "stock/product_add.html", {"product": products[0]})

    # 如果是新增
    return render(request, "stock/product_add.html")


# 保存 新增或编辑 后的产品信息
@login_required
@csrf_exempt
def save_product(request):
    try:
        # 先获取参数
        product_code = request.POST["productCode"]
        record_code = request.POST["recordCode"]
        product_name = request.POST["productName"]
        shortname = request.POST["shortname"]
        sz_account = request.POST["szAccount"]
        sh_account = request.POST["shAccount"]
        status = request.POST["status"]

        # 更新数据库
        update_field = {"record_code": record_code, "product_name": product_name, "shortname":shortname,\
                        "sz_account": sz_account, "sh_account": sh_account, "status": status}
        Product.objects.update_or_create(product_code=product_code, defaults=update_field)

    except Exception as e:
        print e.message

    finally:
        return HttpResponseRedirect("/ipoms/stock/listProduct")


# 删除产品
@login_required
@csrf_exempt
def delete_product(request):
    try:
        # 获取前端传过来的数组
        product_checked = request.POST.getlist("productChecked")

        # 遍历删除记录
        for product_code in product_checked:
            # 去除空格
            product_code = product_code.replace(" ", "")
            # 删除记录
            Product.objects.filter(product_code=product_code).delete()
        return HttpResponse("success")

    except Exception as e:
        print e.message
        return HttpResponse("error")

# ---------------------------------- 新股日历栏目相关 end   --------------------------


# ---------------------------------- 新股申购栏目相关 begin --------------------------

@login_required
def status_stock(request, status):
    # 获取
    records = Operation.objects.filter(current_status=status).distinct()

    for record in records:
        if int(status) == 1:
            record.start_date = record.stock.zg_start_date.strftime("%Y-%m-%d")
            record.end_date = record.stock.zg_end_date.strftime("%Y-%m-%d")
        elif int(status) == 2:
            record.start_date = record.stock.cl_start_date.strftime("%Y-%m-%d")
            record.end_date = record.stock.cl_end_date.strftime("%Y-%m-%d")
        elif int(status) == 3:
            record.start_date = record.stock.xj_start_date.strftime("%Y-%m-%d")
            record.end_date = record.stock.xj_end_date.strftime("%Y-%m-%d")
        elif int(status) == 4:
            record.start_date = record.stock.sg_start_date.strftime("%Y-%m-%d")
            record.end_date = record.stock.sg_end_date.strftime("%Y-%m-%d")
        elif int(status) == 5:
            record.start_date = record.stock.jk_start_date.strftime("%Y-%m-%d")
            record.end_date = record.stock.jk_end_date.strftime("%Y-%m-%d")
        elif int(status) == 6:
            record.start_date = "--"
            record.end_date = "--"

    zg_count = Operation.objects.filter(current_status=1).distinct().count()
    cl_count = Operation.objects.filter(current_status=2).distinct().count()
    xj_count = Operation.objects.filter(current_status=3).distinct().count()
    sg_count = Operation.objects.filter(current_status=4).distinct().count()
    jk_count = Operation.objects.filter(current_status=5).distinct().count()

    result = {"records": records, "status": int(status), "zg_count": zg_count,\
              "cl_count": cl_count, "xj_count": xj_count, "sg_count": sg_count, "jk_count": jk_count}
    return render(request, "stock/stock_status.html", result)


@login_required
@csrf_exempt
def operation_stock(request):
    today = datetime.datetime.today().date()

    zg_stocks = Stock.objects.filter(zg_start_date__lte=today, zg_end_date__gte=today)
    cl_stocks = Stock.objects.filter(cl_start_date__lte=today, cl_end_date__gte=today)
    xj_stocks = Stock.objects.filter(xj_start_date__lte=today, xj_end_date__gte=today)
    sg_stocks = Stock.objects.filter(sg_start_date__lte=today, sg_end_date__gte=today)
    jk_stocks = Stock.objects.filter(jk_start_date__lte=today, jk_end_date__gte=today)

    result = {"zg_stocks":zg_stocks,"cl_stocks":cl_stocks,"xj_stocks":xj_stocks,"sg_stocks":sg_stocks,"jk_stocks":jk_stocks}

    return render(request, "stock/stock_operation.html",result)


@login_required
def operation_detail(request, stock_code):
    stock = Stock.objects.filter(stock_code=stock_code)[0]
    return render(request, "stock/operation_detail.html", {"stock": stock})


# ---------------------------------- 新股申购栏目相关 end --------------------------



