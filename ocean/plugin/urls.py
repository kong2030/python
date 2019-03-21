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

    # 常用工具
    url(r'^searchLogLocal$', views.search_log_local_page, name='searchLogLocal'),
    url(r'^searchLogRemote$', views.search_log_remote_page, name='searchLogRemote'),
    url(r'^copyLogRemote$', views.copy_log_remote_page, name='copyLogRemote'),
    url(r'^getLogLocal$', views.get_log_local, name='getLogLocal'),
    url(r'^getLogRemote$', views.get_log_remote, name='getLogRemote'),
]