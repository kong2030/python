# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import traceback
import logging


# Create your views here.
# 修改密码页
def pwd_change_page(request):
    return render(request, "config/pwd_change.html")


# 修改密码
@login_required
@csrf_exempt
def save_password(request):
    try:
        old_password = request.POST["oldPwd"].replace(" ", "")
        new_password = request.POST["newPwd"].replace(" ", "")
        user = request.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return HttpResponse("success")
        else:
            return HttpResponse("old password is not right!")
    except Exception as e:
        traceback.print_exc()
        logging.error("save password has an error!")
        logging.exception("EXCEPTION")
        return HttpResponse("Sorry! save error.")

