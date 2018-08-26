# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models import *

# Create your views here.


@login_required
def add_stock(request):
    return render(request, "stock/stock_add.html")


@login_required
def list_stock(request):
    return render(request, "stock/stock_list.html")


@login_required
def list_underwriter(request):
    # 获取所有承销商信息
    underwriters = Underwriter.objects.all()

    return render(request, "stock/underwriter_list.html", {"underwriters": underwriters})


@login_required
@csrf_exempt
def add_underwriter(request):
    try:
        # 获取 post 数据
        underwriter = request.POST["underwriter"]
        shortname = request.POST["shortname"]
        telephone = request.POST["telephone"]
        email = request.POST["email"]

        # 更新数据库
        Underwriter.objects.update_or_create(underwriter=underwriter, defaults={"shortname":shortname, "telephone":telephone, "email":email})

        return HttpResponse("success")

    except Exception as e:
        print e.message
        return HttpResponse("error")


@login_required
@csrf_exempt
def delete_underwriter(request):
    # 获取 post 数据
    underwriter = request.POST["underwriter"].replace(" ", "")
    shortname = request.POST["shortname"].replace(" ", "")
    telephone = request.POST["telephone"].replace(" ", "")
    email = request.POST["email"].replace(" ", "")

    # 更新数据库
    Underwriter.objects.filter(underwriter=underwriter).delete()

    return HttpResponse("success")


@login_required
def list_product(request):
    return render(request, "stock/product_list.html")