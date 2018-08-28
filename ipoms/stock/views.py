# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from models import *

# Create your views here.


@login_required
def add_stock(request):
    return render(request, "stock/stock_add.html")


@login_required
def list_stock(request):
    return render(request, "stock/stock_list.html")


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

        # 更新数据库
        update_field = {"record_code": record_code, "product_name": product_name, "shortname":shortname, "sz_account": sz_account, "sh_account": sh_account}
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