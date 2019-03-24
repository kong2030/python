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

    # 密码加密
    url(r'^encryptPage$', views.encrypt_page, name='encryptPage'),
    url(r'^encrypt$', views.encrypt, name='encrypt'),

    # 组件增删改查
    url(r'^listModule$', views.list_module_page, name='listModule'),
    url(r'^addModule$', views.add_module_page, name='addModule'),
    url(r'^editModule$', views.edit_module_page, name='editModule'),
    url(r'^saveModule$', views.save_module, name='saveModule'),

    # 用户-系统增删改查
    url(r'^listAppUser$', views.list_app_user_page, name='listAppUser'),
    url(r'^addAppUser$', views.add_app_user_page, name='addAppUser'),
    url(r'^saveAppUser$', views.save_app_user, name='saveAppUser'),

    # 通过系统名来查询组件
    url(r'^getModulesByApp$', views.get_modules_by_app, name='getModulesByApp'),

    # 通过组件名来查询主机
    url(r'^getHostsByModule$', views.get_hosts_by_module, name='getHostsByModule'),

]