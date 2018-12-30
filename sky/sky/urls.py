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
from django.conf.urls import url,include
from django.contrib import admin


from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # login and index page url
    url(r'^sky/login$', views.login_page, name='login'),
    url(r'^sky/index$', views.index_page, name='index'),
    url(r'^sky/$', views.index_page),
    url(r'^sky/loginCheck$', views.login_check),
    url(r'^sky/logout$', views.logout_check, name='logout'),

    # sub module url
    url(r'^sky/cmdb/',include('cmdb.urls', namespace='cmdb')),

    # sub module url
    url(r'^sky/deploy/',include('deploy.urls', namespace='deploy')),
]