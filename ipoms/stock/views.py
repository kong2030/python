# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def add_stock(request):
    return render(request, "stock/stock_add.html")


@login_required
def list_stock(request):
    return render(request, "stock/stock_list.html")


@login_required
def list_securitiesCo(request):
    return render(request, "stock/securitiesCo_list.html")


@login_required
def list_product(request):
    return render(request, "stock/product_list.html")