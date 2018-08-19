# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

##加载首页
def default_page(request):
	return HttpResponseRedirect("/ipoms/index.html")

def index_page(request):
	result={'login':1};
	return render(request,'index.html',result)

##加载登录页面
def login_page(request):
	return render(request,'login.html')

##登录验证
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
		#return HttpResponse("the username or password is error")
		return HttpResponse("the username or password is error")

##注销
def logout_check(request):
	logout(request)
	return HttpResponseRedirect("/ywms/index")


