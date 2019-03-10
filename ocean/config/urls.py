# -*- coding: utf-8 -*-

"""ipoms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url



from . import views

urlpatterns = [

    # 修改密码
    url(r'^pwdPage$', views.pwd_change_page, name='pwdPage'),
    url(r'^savePwd$', views.save_password, name='savePwd'),

    # 常用网址管理
    url(r'^listWebsite$', views.list_website_page, name='listWebsite'),
    url(r'^addWebsite$', views.add_website_page, name='addWebsite'),
    url(r'^editWebsite$', views.edit_website_page, name='editWebsite'),
    url(r'^saveWebsite$', views.save_website, name='saveWebsite'),

    # 常用工具
    url(r'^searchLog$', views.search_log_page, name='searchLog'),
    url(r'^getLog$', views.get_log, name='getLog'),

]