"""ocean URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from django.views.static import serve
from . import settings

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # login and index page url
    url(r'^ocean/login$', views.login_page, name='login'),
    url(r'^ocean/index$', views.index_page, name='index'),
    url(r'^ocean/$', views.index_page),
    url(r'^ocean/loginCheck$', views.login_check),
    url(r'^ocean/logout$', views.logout_check, name='logout'),

    # sub module url
    url(r'^ocean/config/', include('config.urls', namespace='config')),
    url(r'^ocean/cmdb/', include('cmdb.urls', namespace='cmdb')),
    url(r'^ocean/article/', include('article.urls', namespace='article')),
    url(r'^ocean/monitor/', include('monitor.urls', namespace='monitor')),
    url(r'^ocean/analysis/', include('analysis.urls', namespace='analysis')),
    url(r'^ocean/plugin/', include('plugin.urls', namespace='plugin')),

    # ckeditor upload image
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
