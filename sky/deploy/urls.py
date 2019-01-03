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

    # 发布单增删改查
    url(r'^listOrder$', views.list_order, name='listOrder'),
    url(r'^addOrder$', views.add_order, name='addOrder'),
    url(r'^saveOrder$', views.save_order, name='saveOrder'),

    # 环境流转
    url(r'^changeOrderPage$', views.change_order_page, name='changeOrderPage'),
    url(r'^changeOrder$', views.change_order, name='changeOrder'),

    # 部署发布
    url(r'^listDeployOrder$', views.list_deploy_order, name='listDeployOrder'),
    url(r'^deployOrder$', views.deploy_order, name='deployOrder'),
    url(r'^saveDeploy$', views.save_deploy, name='saveDeploy'),


]