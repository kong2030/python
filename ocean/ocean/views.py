# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from config.models import *

# Create your views here.


# 加载首页
@login_required
def index_page(request):
    # 初始化菜单css，表示选中哪个主菜单、子菜单
    main_memu = "index"
    sub_menu = ""

    websites = Website.objects.all()
    return render(request, 'index.html', {"main_memu":main_memu, "sub_menu": sub_menu, "websites": websites})


# 加载登录页面
def login_page(request):
    return render(request, 'login.html')


# 登录验证
@csrf_exempt
def login_check(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)

            # Redirect to a success page.

            return HttpResponse("ok")
        else:
            # Return a 'disabled account' error message
            return HttpResponse("your account is locked")
    else:
        # return HttpResponse("the username or password is error")
        return HttpResponse("username or password is error, please check")


# 注销
def logout_check(request):
    logout(request)
    return HttpResponseRedirect("/ocean/login")


