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

    # 监控任务列表管理
    url(r'^taskStatus$', views.task_status_page, name='taskStatus'),
    url(r'^listTask$', views.list_task_page, name='listTask'),
    url(r'^addTask$', views.add_task_page, name='addTask'),
    url(r'^editTask$', views.edit_task_page, name='editTask'),
    url(r'^saveTask$', views.save_task, name='saveTask'),

    url(r'^viewMonitor/(?P<id>(\d+))$', views.view_monitor, name='viewMonitor'),

]